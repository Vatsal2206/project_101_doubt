import dropbox
import os
import random
class TransferData(object):
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dropbox_address = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dropbox_address.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode.overwrite )

def uploading():
    access_token = 'sl.Ayxj45Hs6wAfYrrMWT4A7tclXJHxeNnqvSyYKK-1kwyd5n4xZ4zyMEropWkdFMitR8BoTp3zYaUotwuSy_jnCo6OQp0p0IOZtb1WXwyR3sjbszKEOQDH-GHkodd_gAcrufvSSslT'
    transferData = TransferData(access_token)
    randomNumber = random.randint(1,100)
#C:\Users\Shashwat Varenya\Pictures\Screenshots\Screenshot (323).png
    while 1 < 2 :
        file_from = input('Enter your file path here :')
        file_name, file_extension = os.path.splitext(file_from)
        file_to = '/Cloud_Storage_/uploadedFile'+str(randomNumber) +file_extension
        if(os.path.exists(file_from)):
            transferData.upload_file(file_from, file_to)
            print('FILE MOVED!!')
        else:
            print('The path you entered does not exist, please try again!')

uploading()    