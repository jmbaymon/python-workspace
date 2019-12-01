import os.path, time


# print(os.walk('~/home'))
# print("Last Access: %s" % time.ctime(os.path.getatime("comma.py")))
# print("Last modified: %s" % time.ctime(os.path.getmtime("comma.py")))


for (root,dirs,files) in os.walk('/run/media/jmbaymon/6163-3831/DCIM/100CANON', topdown=True): 
    # print(root)
    # print(dirs)
    # fileList = []
    # fileList = files
    # print('--------------------------------')
    print(type(files))
