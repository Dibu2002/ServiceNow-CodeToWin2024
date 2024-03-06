# import os

# def sort_files_by_name(folder_path):
#     # List all files and directories in the folder
#     files = os.listdir(folder_path)
    
#     # Sort the files alphabetically
#     sorted_files = sorted(files)
    
#     return sorted_files

# folder_path = "/Users/divysang/Desktop/SERVICENOW/traffic_data/labels/test"

# sorted_files = sort_files_by_name(folder_path)

# print("Sorted files in the folder:")
# for file_name in sorted_files:
#     print(file_name)

import os
import shutil

def move_last_files(source_folder, destination_folder, num_files_to_move):
    # List all files in the source folder
    files = os.listdir(source_folder)
    
    # Sort files alphabetically
    sorted_files = sorted(files)
    
    # Get the last num_files_to_move files
    # files_to_move = sorted_files
    files_to_move = sorted_files

    
    # Move files to destination folder
    for file_name in files_to_move:
        source_file_path = os.path.join(source_folder, file_name)
        destination_file_path = os.path.join(destination_folder, file_name)
        shutil.move(source_file_path, destination_file_path)

# Define paths
source_folder = "/Users/divysang/Desktop/SERVICENOW/trafic_data/train/labels"
destination_folder = "/Users/divysang/Desktop/SERVICENOW/traffic_dataset/labels/train"
num_files_to_move = 301

# Move the last 1135 files from source folder to destination folder
move_last_files(source_folder, destination_folder, num_files_to_move)


# print("Files moved successfully!")

