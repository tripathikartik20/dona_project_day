import os
import shutil
def getListOfFiles(dirName):
    listOfFile = os.listdir(dirName)
    allFiles = []
    for entry in listOfFile:
        fullPath = os.path.join(dirName, entry)
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        elif (fullPath.endswith('.webp')):
            allFiles.append(fullPath)

    return allFiles

dirname = 'C:/Users/PREDATOR/Desktop/dona/dona_project_day' #Your Full Path of Projects Folder
dest="C:/Users/PREDATOR/Desktop/dona/dona_project_day/gif_data/"

data=getListOfFiles(dirname)
for i in range(len(data)):
    fname=dest+str(i)+".webp"
    shutil.copyfile(data[i], fname)