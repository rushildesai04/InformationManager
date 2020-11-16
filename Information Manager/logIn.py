def logIn():
    #Imports
    from cryptography.fernet import Fernet
    import sys

    #Encryption Conversions
    file = open("accountID.txt")
    lines = file.readlines()
    keyCheck = lines[31]
    unameCheck = lines[33]
    pwordCheck = lines[35]
    decryptCode = Fernet(keyCheck)
    unameCheck = unameCheck.encode()
    pwordCheck = pwordCheck.encode()
    decryptUname = decryptCode.decrypt(unameCheck)
    decryptUname = decryptUname.decode()
    decryptPword = decryptCode.decrypt(pwordCheck)
    decryptPword = decryptPword.decode()
    #Username
    print("Welcome Back!\nType in you username to start logging in to your account.")
    uCount = 3
    while True:
        if uCount > 0:
            username = input()
            if (username == decryptUname):
                print("Great!")
                break
            else:
                print("Error: Usernames do not match.")
                if uCount != 1:
                    tries = "tries"
                else:
                    tries = "try"
                print("You have {} {} left...".format(uCount-1,tries))
                uCount = uCount - 1
        else:
            print("The username was not successfully entered in the given amount of attempts.")
            sys.exit()



logIn()




