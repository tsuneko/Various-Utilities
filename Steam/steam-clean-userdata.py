import os
import shutil

path = "C:\\Program Files (x86)\\Steam\\userdata"

filesToDelete = []
for filename in os.listdir(path):
        if not os.path.isdir(path+"\\"+filename+"\\760\\remote\\730\\screenshots"):
                filesToDelete.append(path+"\\"+filename)

for f in filesToDelete:
        print("Deleting: " + f)
        shutil.rmtree(f)
