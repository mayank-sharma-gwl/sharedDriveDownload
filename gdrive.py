import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

# Google Drive API scope
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
FOLDER_ID = ''

def authenticate():
    flow = InstalledAppFlow.from_client_secrets_file(
        'cred.json', SCOPES)
    credentials = flow.run_local_server(port=0)
    return credentials

def export_and_download_file(file, service, folder_path):
    mime_type = file['mimeType']
    filename = f"{file['name']}"

    if 'application/vnd.google-apps' in mime_type:
        if 'document' in mime_type:
            export_mimetype = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
            filename += '.docx'
        elif 'spreadsheet' in mime_type:
            export_mimetype = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            filename += '.xlsx'
        elif 'presentation' in mime_type:
            export_mimetype = 'application/vnd.openxmlformats-officedocument.presentationml.presentation'
            filename += '.pptx'
        else:
            print(f"Unsupported Google Docs format: {mime_type}")
            return

        request = service.files().export_media(fileId=file['id'], mimeType=export_mimetype)
    else:
        request = service.files().get_media(fileId=file['id'])

    file_path = os.path.join(folder_path, filename)

    with open(file_path, 'wb') as f:
        downloader = MediaIoBaseDownload(f, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print(f"Download {int(status.progress() * 100)}%")

def download_folder(folder_id, service, parent_path="."):
    results = service.files().list(q=f"'{folder_id}' in parents").execute()
    items = results.get('files', [])

    for item in items:
        if item['mimeType'] == 'application/vnd.google-apps.folder':
            subfolder_path = os.path.join(parent_path, item['name'])
            os.makedirs(subfolder_path, exist_ok=True)
            download_folder(item['id'], service, parent_path=subfolder_path)
        else:
            export_and_download_file(item, service, parent_path)

def main():
    creds = authenticate()
    service = build('drive', 'v3', credentials=creds)

    parent_folder = 'downloads'
    if not os.path.exists(parent_folder):
        print("The specified parent folder does not exist.")
        return

    download_folder(FOLDER_ID, service, parent_path=parent_folder)

if __name__ == '__main__':
    main()