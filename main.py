from folder_organiser.folder_organiser import FolderOrganiser
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--path", dest='path', help="Path to the folder you want to organise", type=str)
args = parser.parse_args()

# TODO: OPTIMISE CODE
if __name__ == '__main__':
    folder_organiser = FolderOrganiser(args.path)
    # Initialise all folders
    folder_organiser.init_folders()
    # Organise files into these folders
    folder_organiser.run()
