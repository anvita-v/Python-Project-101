import dropbox
from dropbox.files import WriteMode
import os


class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_files(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(file_from):
            for filename in files:
                local_path = os.path.join(root, filename)
                relative path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)

                with open(local_path, 'rb') as f:
                     dbx.files_upload(f.read(), dropbox_path, mode = WriteMode('overwrite'))
                    
def main():
    access_token = 'sl.AxP73u6csKwiCI6wqNOUfBTBqy6LjZXz_k6poyUn5cP8GKAfIKcCyCmK0AMwrhg958YSVRvqMLKoyiyUFcMbgeIs-Hgp4JNeHPdMx4QKW3JWy7Xv_v2PGCu35H85-i8wL8Dp5Hg'
    TransferData = TransferData(access_token)

    file_from = str(input("Enter the file path that you want to transfer: "))
    file_to = input("Enter the full path to the dropbox: ")

    TransferData.upload_files(file_from, file_to)

    print("Your files have been moved")

main()