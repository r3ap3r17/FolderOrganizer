import json

CONFIG_PATH = "./config.json"


class UtilsJson:
    def __init__(self):
        self.config_path = CONFIG_PATH
        self.json_data = self.init_json_config().get("config")
        self.folders = "folderReference"
        self.extensions = "extensionReference"

    # Read from json config and store it in dictionary
    def init_json_config(self):
        config = open(self.config_path)
        return json.load(config)

    # Returns folderReference object
    def get_folder_reference(self):
        return self.json_data.get(self.folders)

    # Returns extensionReference object
    def get_extension_reference(self):
        return self.json_data.get(self.extensions)

    def get_folder_names(self):
        folder_names = list(self.get_folder_reference().keys())
        return folder_names

    def get_extension_names(self, folder_name):
        folder = self.get_folder_reference().get(folder_name)
        folder_extensions = self.get_extension_reference().get(folder)
        return folder_extensions
