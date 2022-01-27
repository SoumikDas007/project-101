from os import access
import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token

    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)

        f=open(file_from,'rb')
        dbx.files_upload(f.read(),file_to)

def main():
    access_token='sl.A_gZLx-fX_BNMBHhjcgkU2BRP2n2QTVJ-kRpFogetka4l08Lxm-eIItz8eqlh6DMR94IcaA7DDfll5GSALxonqhi1mCXhSviEJAKG2NknSIBHbb0sC_fYfZZDWsrcKiBhQ_2C9E'
    transferData=TransferData(access_token)

    file_from=input('ENTER THE FILE TO TRANSFER ')
    file_to=input('ENTER THE FULL PATH TO UPLOAD TO THE DROPBOX')

    transferData.upload_file(file_from,file_to)
    print("FILE HAS ALREADY BEEN MOVED")

main()