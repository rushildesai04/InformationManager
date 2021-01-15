def encryptedPassword(len):
    import random
    list = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    result = ''.join((random.choice(list) for i in range(len)))
    return result



def newFile():
    import os
    import os.path
    from datetime import datetime
    fileName = input("What do you want the name of the file to be?")
    instant = datetime.instant()
    instant = instant.strftime("%B %d, %Y  %H:%M:%S")
    path = os.path.join(os.getcwd(), fileName)
    print("This is the path of the created file:\n" + path)
    return path


def newDirectory():
    import os
    import os.path
    try:
        directoryName = input("What do you want the name of the directory to be?\n")
        dir = "/" + directoryName
        path = os.path.join(os.getcwd(),dir)
        os.mkdir(path)
    except:
        print("Error: The directory was not created. Try entering another directory name.")
    print("This is the path of the created directory:\n" + path)
    newFile()



def searchDir():
    import os
    import os.path
    a = 1
    print("Type in the name of the directory you want to search.")
    path = os.getcwd()
    dirs = os.listdir(os.getcwd())
    for dir in dirs:
        if os.path.isdir(dir):
            print(dir)
    dirName = input()
    if os.path.isdir(dirName):
        path = os.path.join(path, dirName)
        print("This is the path of the current directory:\n" + path)
    else:
        while a == 1:
            print("Error: Directory Not Found.\nPlease type in another direcory.")
            dirName = input()
            if os.path.isdir(dirName):
                path = os.path.join(path, dirName)
                print("This is the path of the current directory:\n" + path)
                a = 0
            else:
                a = 1
    fileOrDir(path)



def fileOrDir(path):
    import os
    import os.path
    Decision = ""
    print("Do you want to select a file in this directory or search a subdirectory?\n(Type \"File\" to open a file and \"Subdirectory\" to search a subdirectory)")
    Decision = input()
    if Decision == "FILE" or Decision == "file" or Decision == "File":
        print("Type in the name of the file you want to open.\n")
        dirs = os.listdir(path)
        for file in dirs:
            if os.path.isfile(file):
                print(file)
        a = 1
        fName = input()
        if os.path.isfile(fName):
            path = os.path.join(path, fName)
            print(path)
            print("This is the path of the selected file:\n" + path)
            return path
        else:
            while a == 1:
                print("Error: File Not Found.\nPlease type in another file.")
                fName = input()
                if os.path.isfile(fName):
                    path = os.path.join(path, fName)
                    print(path)
                    print("This is the path of the selected file:\n" + path)
                    a = 0
                    return path
                else:
                    a = 1
    elif Decision == "SUBDIRECTORY" or Decision == "subdirectory" or Decision == "Subdirectory":
        b = 1
        print("Type in the name of the subdirectory you want to search.")
        path = input()
        dirs = os.listdir(path)
        for dir in dirs:
            if os.path.isdir(dir):
                print(dir)
        dirName = input()
        if os.path.isdir(dirName):
            path = os.path.join(path, dirName)
            print("This is the path of the current directory:\n" + path)
            fileOrDir(path)
        else:
            while b == 1:
                print("Error: Directory Not Found.\nPlease type in another direcory.")
                dirName = input()
                if os.path.isdir(dirName):
                    path = os.path.join(path, dirName)
                    print("This is the path of the current directory:\n" + path)
                    fileOrDir(path)
                    b = 0
                else:
                    b = 1



def openFile():
    import os
    import os.path
    decision = ""
    while decision == "":
        print("Do you want to open a file or search a directory?\n(Type \"File\" to open a file or \"directory\" to search a directory.)\n")
        print("Files:\n")
        for root, dirs, files in os.walk("."):
            for filename in files:
                print(filename)
        print("\nDirectories:\n")
        for root, dirs, files in os.walk("."):
            for dirname in dirs:
                print(dirname)
        decision = input()
        if decision == "FILE" or decision == "file" or decision == "File":
            print("Type in the name of the file you want to open.\n")
            dirs = os.listdir(os.getcwd())
            for file in dirs:
                if os.path.isfile(file):
                    print(file)
            a = 1
            fName = input()
            if os.path.isfile(fName):
                path = os.path.join(os.getcwd(), fName)
                print("This is the path of the selected file:\n" + path)
                return path
            else:
                while a == 1:
                    print("Error: File Not Found.\nPlease type in another file.")
                    fName = input()
                    if os.path.isfile(fName):
                        path = os.path.join(os.getcwd(), fName)
                        print("This is the path of the selected file:\n" + path)
                        a = 0
                        return path
                    else:
                        a = 1
        elif decision == "DIRECTORY" or decision == "directory" or decision == "Directory":
            searchDir()
        else:
            print("Error: Unknown Command.\nPlease enter either \"File\" or \"Directory\".")
            decision = ""



def enterText(path):
    from cryptography.fernet import Fernet
    fileOpen = open(path, "a")
    file = open("accountID.txt")
    lines = file.readlines()
    keyCheck = lines[31]
    encryptCode = Fernet(keyCheck)
    a = 1
    print("Please enter the text that you want to input into the chosen file.\n(If you want to start text on the next line, put a \"***\" at the end of the current line.)")
    while a == 1:
        txt = input()
        if txt[len(txt) - 3:len(txt)] == "***":
            a = 1
            txt = txt[0:len(txt)-3]
        else:
            a = 0
        Newtxt = txt.encode()
        Newtxt = encryptCode.encrypt(Newtxt)
        Newtxt = Newtxt.decode()
        fileOpen.write(Newtxt)
        fileOpen.write("\n")



def createOrOpen():
    import os
    import os.path
    txtfile = os.path.join(os.getcwd(), "accountID.txt")
    if os.path.isfile(txtfile):
        from logIn import logIn
        logIn()
    else:
        from accountCreation import accountCreation
        accountCreation()



def decision():
    decision = ""
    while decision == "":
        print(
            "Do you want to create a brand new file, make a brand new directory, or open a file from your file system?\n(Type \"Create\" to open a file, \"Make\" to open a directory, or \"Open\" to search a directory.)\n")
        decision = input()
        if decision == "CREATE" or decision == "create" or decision == "Create":
            path = newFile()
            enterText(path)
        elif decision == "MAKE" or decision == "make" or decision == "Make":
            path = newDirectory()
        elif decision == "OPEN" or decision == "open" or decision == "Open":
            path = openFile()
            enterText(path)
        else:
            print("Error: Unknown Command.\nPlease enter either \"Create\", \"Make\", or \"Open\".")
            decision = ""


