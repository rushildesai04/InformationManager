def logIn():
    #Imports
    from cryptography.fernet import Fernet
    import sys
    import smtplib
    import ssl
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from creation import encryptedPassword

    #Encryption Conversions
    file = open("accountID.txt")
    lines = file.readlines()
    keyCheck = lines[31]
    unameCheck = lines[33]
    pwordCheck = lines[35]
    emailcheck = lines[37]
    decryptCode = Fernet(keyCheck)
    unameCheck = unameCheck.encode()
    pwordCheck = pwordCheck.encode()
    emailcheck = emailcheck.encode()
    decryptUname = decryptCode.decrypt(unameCheck)
    decryptUname = decryptUname.decode()
    decryptPword = decryptCode.decrypt(pwordCheck)
    decryptPword = decryptPword.decode()
    decryptemail = decryptCode.decrypt(emailcheck)
    decryptemail = decryptemail.decode()
    code = encryptedPassword(6)

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

    #Password
    print("Type in you password to start logging in to your account.")
    pCount = 3
    while True:
        if pCount > 0:
            password = input()
            if (password == decryptPword):
                print("Great!")
                break
            else:
                print("Error: Passwords do not match.")
                if pCount != 1:
                    tries = "tries"
                else:
                    tries = "try"
                print("You have {} {} left...".format(pCount - 1, tries))
                pCount = pCount - 1
        else:
            print("The password was not successfully entered in the given amount of attempts.")
            sys.exit()

    #E-mail Creation
    message = MIMEMultipart("alternative")
    message["Subject"] = "Log in to Information manager!"
    message["From"] = "theinformationmanager@gmail.com"
    message["To"] = decryptemail
    plaintext = "Welcome back! Someone is trying to sign into your infomation manager account. To enter your account and access your information, enter this code into the program."
    htmltext = """
                <html>
                  <body>
                    <p style="color:rgb(0,200,255)";"font-family:'Calibri'";"font-size:12px">Hello!<br><br>
                       Welcome back!
                       Someone is trying to sign into your infomation manager account.
                       To enter your account and access your information, enter this code into the program.<br>
                    </p>
                    <p style="font-family:'Garamond'";"font-size:20px">
                        <strong>{code}</strong><br>
                    </p>
                    <p style="color:rgb(0,200,255)";"font-family:'Calibri'";"font-size:12px">
                       Thank for using the information manager.<br><br>
                    </p>
                    <p>
                       <img src="https://europeanbusinessmagazine.com/wp-content/uploads/2020/11/0_QxsWlMTDGmTebavF.jpg" alt="Information Manager"> 
                    </p>
                  </body>
                </html>
                """.format(code=code)
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
    server.sendmail("theinformationmanager@gmail.com", decryptemail, message.as_string())
    server.quit()

    #E-mail
    print("Type in your 6-digit code from the email to start logging in to your account.")
    cCount = 2
    while True:
        if cCount > 0:
            Code = input()
            if (Code == code):
                print("Great!")
                break
            else:
                print("Error: The code does not match.")
                if cCount != 1:
                    tries = "tries"
                else:
                    tries = "try"
                print("You have {} {} left...".format(cCount - 1, tries))
                cCount = cCount - 1
        else:
            print("The code was not successfully entered in the given amount of attempts.")
            sys.exit()

