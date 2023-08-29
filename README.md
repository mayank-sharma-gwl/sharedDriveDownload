
# Download All Contents of Shared Google Drive Folder

It downloads all the contents of the Shared Google Drive link. It helps users download the files without creating zip.

# Usage:
- Step1- Download the project either using the ``` Download ZIP ``` inside ```< > Code``` button and extract it or you can clone it using ``` git clone https://github.com/mayank-sharma-gwl/sharedDriveDownload.git ```
- Step2- Run command ```cd sharedDriveDownload```
- Step3- Run command ```pip install -r requirements.txt``` || if this doesn't works use ```pip3 install -r requirements.txt```
- Step4- To use the script, enter ```FOLDER_ID``` which can be found in the shared google drive link. For example if the link is ```https://drive.google.com/drive/folders/169iaKQclsC3FripZ5BtcsZNQ0j683SGE```, then the ```FOLDER ID```is ```169iaKQclsC3FripZ5BtcsZNQ0j683SGE```.
- Step5- Copy the id and paste it inside the file gDrive.py at line number 9 as shown  
  ```
  FOLDER_ID = '169iaKQclsC3FripZ5BtcsZNQ0j683SGE'
  ```
  > 
  > Make sure that the ```FOLDER_ID``` is inside the single quotation marks.

- Step6- Create a folder named as ```downloads``` inside the folder where the script is present.
- Step7- Run the python file using command ```python3 gDrive.py```

- All the downloaded contents will be available in downloadd folder inside the current directory i.e. sharedDriveDownload
  > The 'cred.json' file will only be functional until August 30, 2023, and is intended for BITS Pilani users ONLY.
- Make sure you have Python installed on your system
