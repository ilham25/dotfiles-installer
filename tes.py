import os
import shutil

workingDir = os.getcwd() + '/'
src_files = os.listdir(workingDir + "tes")
for file_name in src_files:
    print(src_files)
    full_file_name = os.path.join(workingDir + "tes", file_name)
    print(full_file_name)
    if os.path.isfile(full_file_name):
        shutil.copy(full_file_name, workingDir)
