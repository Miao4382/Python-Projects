from functions import *
from list import *
import shutil

homeworkFolder = "hw1"

# make two sub folders for my section
os.makedirs(homeworkFolder + "/section1")
os.makedirs(homeworkFolder + "/section2")

for dirPath, dirNames, files in os.walk(homeworkFolder):
    # we need to skip hw folder's sub-folder
    if len(dirNames) == 0:
        continue
    # we are in hw folder, move files to sections if file name match section1 or 2
    for fileName in files:
        if fileName[0:fileName.find('_')] in sectionOne:
            shutil.copy2(dirPath + "\\" + fileName, dirPath + "\\section1\\" + fileName)
        if fileName[0:fileName.find('_')] in sectionTwo:
            shutil.copy2(dirPath + "\\" + fileName, dirPath + "\\section2\\" + fileName)
        os.remove(dirPath + "\\" + fileName)
