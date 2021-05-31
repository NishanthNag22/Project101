import dropbox
import os
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,accessToken):
        self.accessToken=accessToken

    def uploadFile(self,fileFrom,fileTo):
        dbx=dropbox.Dropbox(self.accessToken)
        for root, dirs, files in os.walk(fileFrom):
            for filename in files:
                localPath = os.path.join(root, filename)
                relativePath = os.path.relpath(localPath, fileFrom)
                dropboxPath = os.path.join(fileTo, relativePath)
                with open(localPath, 'rb') as f:
                    dbx.files_upload(f.read(), dropboxPath, mode=WriteMode('overwrite'))

def main():
    accessToken='JntOspNNS4sAAAAAAAAAAYo9momkxh1XqhVfcbx3Nhy9wpSTIBzCfUfq0vb-cQ5L'
    transferData=TransferData(accessToken)

    fileFrom=str(input("Enter the folder path to transfer : "))
    fileTo=input("Enter the full path to add the files to the dropbox : ")

    transferData.uploadFile(fileFrom,fileTo)
    print("File has been moved successfully")

main()