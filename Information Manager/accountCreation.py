username = ""
def accountCreation():
    #Imports
    import os
    import os.path
    import time
    import sys
    import smtplib
    import ssl
    import getpass
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from encryptedPassword import encryptedPassword
    from cryptography.fernet import Fernet

    #Initialization
    print("Thank you for choosing the Information Manager")
    print("This is a great tool for staying organized and keeping Infomation Secure")
    print("Lets get started with creating your account\n")

    #Name
    print("What is your full name?")
    name = input()

    #Username
    while True:
        print("Please type in the username that you want to use.\nYou must remember this username so it is recommended that you save it someplace where you can find it later.")
        username = input()
        if len(username) >= 8:
            print("Great username!")
            break
        else:
            print("Error: " + username + " should be greater than or eaual to 8 characters")
            continue
    asterisks = ""
    for i in range(len(username)-4):
        asterisks =  asterisks + "*"
    newUsername = username[0:2] + asterisks + username[len(username)-2:len(username)]

    #Password
    while True:
        print("Please type in the password that you wish to use for the account.\nYou must remember this password so it is recommended that you save it someplace where you can find it later.")
        password = input()
        if len(password) >= 8:
            print("Great password!")
            break
        else:
            print("Error: " + password + " should be greater than or eaual to 8 characters")
            continue
    while True:
        print("Please confirm your password.")
        passwordTwo = input()
        if password == passwordTwo:
            break
        else:
            print("Error: Passwords do not match")
            continue
    for i in range(len(password)-4):
        asterisks =  asterisks + "*"
    newPassword = password[0:2] + asterisks + password[len(password)-2:len(password)]

    #E-mail
    while True:
        try:
            while True:
                try:
                    print("Please enter your email.")
                    email = input()
                    print("Please type in your email again.")
                    emailTwo = input()
                    if email == emailTwo:
                        break
                except:
                    print("Error: emails do not match.")
                    continue
            activation = encryptedPassword(10)
            message = MIMEMultipart("alternative")
            message["Subject"] = "Welcome to the Information Manager!"
            message["From"] = "theinformationmanager@gmail.com"
            message["To"] = email

            plaintext = "Hello!\nThank you for choosing the information manager to keep track of all your information.\nThere's just one last step in creating your account.\nThe activation code to finish your account creation is below.\nUse this key to verify your account.\n{code}\nThank you for joining the Information Manager!"
            htmltext = """
            <html>
              <body>
                <p style="color:rgb(0,200,255)";"font-family:'Calibri'";"font-size:12px">Hello!<br><br>
                   Thank you for choosing the information manager to keep track of all your information.
                   Please double check that all your information is correct.<br>
                </p>
                <p style="color:rgb(0,200,255)";"font-family:'Calibri'";"font-size:12px">
                    Full Name: <Strong>{fullname}</Strong><br>
                    Username: <Strong>{username}</Strong><br>
                    Password: <Strong>{password}</Strong><br>
                </p>
                <p style="color:rgb(0,200,255)";"font-family:'Calibri'";"font-size:12px">
                   There's just one last step in creating your account.<br><br>
                   The activation code to finish your account creation is below.<br>
                   Use this key to verify your account:<br>
                </p>
                <p style="font-family:'Garamond'";"font-size:20px">
                    <strong>{code}</strong><br>
                </p>
                <p style="color:rgb(0,200,255)";"font-family:'Calibri'";"font-size:12px">
                   Thank you for joining the Information Manager!<br><br>
                </p>
                <p>
                   <img src="https://europeanbusinessmagazine.com/wp-content/uploads/2020/11/0_QxsWlMTDGmTebavF.jpg" alt="Information Manager"> 
                </p>
              </body>
            </html>
            """.format(code=activation,fullname=name,username=newUsername,password=newPassword)
            part1 = MIMEText(plaintext, "plain")
            part2 = MIMEText(htmltext, "html")
            message.attach(part1)
            message.attach(part2)

            server = smtplib.SMTP("smtp.gmail.com", port=587)
            context = ssl.create_default_context()
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login("theinformationmanager@gmail.com", "inf0RulZ!")
            server.sendmail("theinformationmanager@gmail.com", email, message.as_string())
            server.quit()
            break
        except:
            print("There was an error. Please try inputting your email again.")
            continue

    #Verification
    print("An email has been sent to you with an activation code for your account.\nPlease enter that activation code exactly how it is displayed below.")
    codeCount = 3
    while codeCount != 0:
        code = input()
        if code == activation:
            codeCount = -1
            break
        else:
            if codeCount == 1:
                tries = "try"
            else:
                tries = "tries"
            codeCount = codeCount - 1
            print("The provided activation code provided is not the same as the one in the email.\nYou have {tryNum} {tries} left".format(tryNum=codeCount, tries=tries))
            continue
    if codeCount == 0:
        print("Failed to provide the correct activation code in 3 attempts. System will shut down due to security purposes. Please redownload the program and try again")
        time.sleep(1)
        print("3...")
        time.sleep(1)
        print("2...")
        time.sleep(1)
        print("1...")
        time.sleep(1)
        sys.exit()

    #Information Encryption
    uName = username.encode()
    pWord = password.encode()
    key = Fernet.generate_key()
    StrKey = key.decode()
    fernetCode = Fernet(key)
    uName = fernetCode.encrypt(uName)
    uName = uName.decode()
    pWord = fernetCode.encrypt(pWord)
    pWord = pWord.decode()

    #Information Append
    def accountidWrite(info):
        idOpen = open("accountID.txt", "a")
        idOpen.write(info)
    os.mkdir(os.path.join(os.getcwd(),"Information Files"))
    infopath = os.path.join(os.getcwd(),"Information Files")
    idpath = os.path.join(os.getcwd(),"accountID.txt")
    accountidWrite("\n----------           ----------\nInformation Manager Account ID\n          -----------          \n\n")
    accountidWrite("Name:\n " + name + "\n\n\n")
    accountidWrite("Username:\n " + newUsername + "\n\n\n")
    accountidWrite("Password:\n " + newPassword + "\n\n\n")
    accountidWrite("E-mail:\n " + email + "\n\n\n")
    accountidWrite("Account ID File Path:\n " + idpath + "\n\n\n")
    accountidWrite("Information Files Path:\n " + infopath + "\n\n\n")
    accountidWrite("Source Code:\n\n" + StrKey + "\n\n")
    accountidWrite(uName + "\n\n")
    accountidWrite(pWord + "\n\n")

    #End
    print("Congratulations!\nYou're Information Manager Account has been created!\nWhenever you need to log in, you will need your username and your password. You will get an email with a login code.\nRestart the program and log in to start inputting information.\nThank you for registering and we hope this program helps you.")



accountCreation()
print(username)

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
