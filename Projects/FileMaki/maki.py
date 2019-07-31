import shutil , os, send2trash

"""
Maki will have the following methods:
[ ] recycle file to trash 
[ ] backup/move folders
[ ] Folder/ files Display
[ ] Create files/ folders
"""

class Maki:
    def __init__(self,fPath):
        """
        stores user to selected path.
        """
        self.fPath = fPath
    

    def select_file(self):
        for root, dirs, files in os.walk(self.fPath, topdown=False):
            for name in files:
                print(os.path.join(root, name))
            for name in dirs:
                    print(os.path.join(root, name))


    def trashItem():
        """
        Take name of  file and sends it the trash 
        """
        pass