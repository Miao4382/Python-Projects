import os


# this function will navigate a pre-selected folder containing student submissions
# and will print out their names. This function is used to get the list declaration
# so we can store the name of student
def printStudentName(dirName):
    for dirPath, dirNames, files in os.walk(dirName):
        print(dirPath)
        for fileName in files:
            print('\t"' + fileName[0:fileName.find('_')] + '\",')


