import os
import shutil
path = "/home/jmbaymon"
a = os.path.join(path, "Downloads")
dst = "/run/media/jmbaymon/myfiles"
for dirpath, dirname, files in os.walk(a):
    for file_name in files:
        if file_name.endswith(".pdf"):
            fullPath = os.path.join(a,file_name)
            shutil.move(fullPath, dst)
            print(f'File moved:{file_name}')
