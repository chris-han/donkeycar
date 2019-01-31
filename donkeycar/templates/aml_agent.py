# -------------------------------------------------------------------------
# Access Azure File Share with SAS
# --------------------------------------------------------------------------
from azure.common import (
    AzureConflictHttpError,
    AzureMissingResourceHttpError,
)
from azure.storage.common import (
    AccessPolicy,
    ResourceTypes,
    AccountPermissions,
)
from azure.storage.file import (
    FileService,
    SharePermissions,
    FilePermissions,
)

import sys
from os import listdir
from os.path import isfile, join


class AmlAgent():

    file_service=None

    def __init__(self):
        self.file_service = FileService(account_name='mtcautonstoragegpdxmrdy', 
            sas_token='?sv=2018-03-28&ss=bfqt&srt=sco&sp=rwdlacup&se=2029-01-30T22:29:29Z&st=2019-01-30T14:29:29Z&sip=0.0.0.0-255.255.255.255&spr=https,http&sig=xSaBujPYpwAw%2FejgY%2FxFyuK4PK6Vfh3Pw6isJ7DK4bg%3D',
            protocol='https')
        self.share_name ='azureml-filestore-3c6c3e55-de73-4e41-a9ed-bb06bb9f26cc'
    '''
        # Basic
        # List from root
        root_file_dir = list(self.file_service.list_directories_and_files(share_name))
        for res in root_file_dir:
            print(res.name)  # dir1, dir2, rootfile

        # Num results
        root_file_dir = list(self.file_service.list_directories_and_files(share_name, num_results=2))
        for res in root_file_dir:
            print(res.name)  # dir1, dir2

        # List from directory
        dir1 = list(self.file_service.list_directories_and_files(share_name, 'test data'))
        for res in dir1:
            print(res.name)  # file1, file2
    '''
    def upload_data(self):
        print("uploading data...")
        source_folder_name='test data'
        source_path = 'C:\\Users\\chha\\Documents\\DonkeyCarFiles'
        self.copy_files(source_path,source_folder_name)                  



    def copy_files(self,source_path,source_folder_name):
            
            dest_folder_name = 'test2/' #source_folder_name
            if self.file_service.exists(share_name=self.share_name ,directory_name=dest_folder_name)==False:
                self.file_service.create_directory(self.share_name, dest_folder_name)

            full_source_path=join(source_path,source_folder_name)
            print ('full_source_path: {}'.format(full_source_path))
            #files_in_source_dir = [f for f in listdir(data_dir_name) if isfile(join(data_dir_name, f))]
            files_in_source_folder = [f for f in listdir(full_source_path) if isfile(join(full_source_path, f))]

            for file_name in files_in_source_folder:
                full_source_file_name = join(full_source_path, file_name)
                print(file_name)  # file1, file2
                #source = self.file_service.make_file_url(self.share_name, dest_directory_name, file_name)
                #copy = self.file_service.copy_file(self.share_name, None, 'file1copy', source)
                self.file_service.create_file_from_path(
                    self.share_name,              # share name
                    source_folder_name,                   # directory path - root path if none
                    file_name,               # destination file name
                    full_source_file_name,      # full source path with file name
                    progress_callback=self.generate_progress_callback(file_name)) #report progress


    def generate_progress_callback(self,file_name):
        def progress_callback(current, total):
            print('({}, {}, {})'.format(file_name, current, total))
        return progress_callback


    def download_model():
        print("downloading model...")


if __name__ == '__main__':
    args = sys.argv
    myagent = AmlAgent()
    
    if args[0]=='download':
        myagent.download_model()
    else:
        myagent.upload_data()

     