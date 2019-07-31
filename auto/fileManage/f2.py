import os

for root, dirs, files in os.walk(".", topdown=False):
   for name in files:
       if name != ".*": 
      print(os.path.join(root, name))
   #for name in dirs:
    #  print(os.path.join(root, name))