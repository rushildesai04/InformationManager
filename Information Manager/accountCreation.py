def accountCreation():
    #Imports
    import os
    import os.path
    import smtplib
    import ssl
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from encryptedPassword import encryptedPassword

    #Initialization
    print("Thank you for choosing the Information Manager")
    print("This is a great tool for staying organized and keeping Infomation Secure")
    print("Lets get started with creating your account\n")

    #Name
    print("What is your full name?")
    name = input()

    #Username
    while True:
        print("Please type in the username that you want to use")
        username = input()
        if len(username) >= 7:
            print("Great username!")
            break
        else:
            print("Error: " + username + " should be greater than or eaual to 7 characters")
            continue

    print("Please enter your email.")
    email = input()
    activation = encryptedPassword(10)

    message = MIMEMultipart("alternative")
    message["Subject"] = "Welcome to the Information Manager!"
    message["From"] = "theinformationmanager@gmail.com"
    message["To"] = email

    plaintext = "Hello!\nThank you for choosing the information manager to keep track of all your information.\nThere's just one last step in creating your account.\nThe activation code to finish your account creation is below.\nUse this key to verify your account.\n{code}\nThank you for joining the Information Manager!".format(code=activation)
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
    """.format(code=activation,fullname=name,username=username)
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
