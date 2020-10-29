def accountCreation():
    import os
    import os.path
    print("Thank you for choosing the Information Manager")
    print("This is a great tool for staying organized and keeping Infomation Secure")
    print("Lets get started with creating your account\n")

    print("What is your full name?")
    name = input()
    while True:
        print("Please type in the username that you want to use")
        username = input()
        if len(username) >= 7:
            print("Great username!")
            break
        else:
            print("Error: " + username + " should be greater than or eaual to 7 characters")
            continue



accountCreation()

#while True:
    #print("Please type in the full file path for the directory location that you would like to store your information")
    #path = input()
    #goodPath = os.path.isdir(path)
    #if goodPath == True:
        #print("Great! All your files will be saved into this directory ")
        #break
    #else:
        #print("Error: " + path + " is not recognized as a directory in the file system.\n")
        #continue


#appendAccount = open("accountID.txt", "a")
    #appendAccount.write("")
