import os
import shutil

from_dir = 'C:/Users/donny/Downloads'
to_dir = '"C:/Users/donny/Desktop/Document_files"'

list_of_files = os.listdir(from_dir)

for files in list_of_files:

    name,extension = os.path.splitext(files)
    
    if extension == ' ' :
        continue
    if extension in ['.txt', '.doc', '.pdf']:

        path_1 = from_dir + '/' + files
        path_2 = to_dir + '/' + 'Document_files'
        path_3 = to_dir + '/' + 'Document_files' + '/' + files

        if os.path.exists(path_2):
            print("moving " + files)
            shutil.move(path_1,path_3)

        else:
            os.makedirs(path_2)
            print("moving " + files)
            shutil.move(path_1,path_3)
