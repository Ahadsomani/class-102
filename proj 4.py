import os
import shutil

from_dir = "/path/to/Downloads"  # Change this to the actual path of your Downloads folder
to_dir = "/path/to/Document_Files"  # Change this to the actual path of your Document_Files folder

list_of_files = os.listdir(from_dir)
print("List of files in source directory:", list_of_files)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    
    if not extension:  # Skip files with no extension
        continue

    allowed_extensions = ['.txt', '.doc', '.docx', '.pdf']
    
    if extension in allowed_extensions:
        path1 = os.path.join(from_dir, file_name)
        path2 = os.path.join(to_dir, "Document_Files")
        path3 = os.path.join(path2, file_name)
        
        if os.path.exists(path2):
            print("Moving", file_name)
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("Moving", file_name)
            shutil.move(path1, path3)
