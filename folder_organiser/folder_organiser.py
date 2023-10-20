# Simple Python Script to automate folder organization
import os
import shutil

from folder_organiser.utils_json import UtilsJson


class FolderOrganiser:
    def __init__(self, path):
        self.path = path
        self.utils_json = UtilsJson()
        self.folder_names = self.utils_json.get_folder_names()

    # Initialise all folders based on config file
    def init_folders(self):
        for folder in self.folder_names:
            folder_path = f'{self.path}/{folder}'
            # Make directory if it doesn't exist
            if not os.path.isdir(folder_path):
                os.mkdir(folder_path)

    def run(self):
        for folder in self.folder_names:
            folder_path = f'{self.path}/{folder}'
            extensions = self.utils_json.get_extension_names(folder)
            for file in self.get_all_files():
                file_path = f'{self.path}/{file}'
                # Get file extension
                extension = file[file.rfind('.') + 1:]
                if extension in self.utils_json.get_extension_names(folder):
                    # Move file to dedicated directory
                    shutil.move(file_path, folder_path)

    def get_all_files(self):
        file_list = os.listdir(self.path)
        # Filter only files (exclude directories)
        file_list = [f for f in file_list if os.path.isfile(os.path.join(self.path, f))]
        return file_list

    # Util method for debugging
    def delete_all_folders(self):
        for folder in self.folder_names:
            folder_path = f'{self.path}/{folder}'
            if os.path.isdir(folder_path):
                os.rmdir(folder_path)
