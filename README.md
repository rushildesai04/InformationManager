# InformationManager


Hi! Welcome to the Information Manager. 
The Information Manager is an application where a person can input and store any type of data (Passwords, Documents, etc.) in a place that can be accessed anywhere and at any time in a safe and secure manner.

***The entirity of this program is written in python.***

Thank you for using the Information Manager.

-  rush-bot


**Introduction**
Stealing someone’s personal information online has become very easy and much more common in recent years.
Our goal is to create an application using the python programming language that can successfully store a user’s information in a safe space that no one else can access except for the owner 
There have been many previous attempts at trying to secure a user’s information, but they all store that user’s information in a place that can still be accessed by someone

**Design**
When designing the program, we had a couple of design requirements and constraints:
The program needed to successfully provide a way of logging in so that the only person who could access the account was only the account owner
The program needed to store the information in a way that a person couldn't understand it if they did get access to it through an unethical way
The program needed to distinguish if an account was already created every time it was initialized
The program needed to make it easy to pick a way to store the information for the user

**Solution - 1**
We created a program that can make sure that information can be stored in a space that no one can access except for the owner using many different security measures and encryptions.
We designed our program so that there were four different files that perform different functions and were used for different things. When combined they would create a well functioning program.
We tested our program by testing each file separately to make sure they each worked as intended and then tested the whole program multiple times after the code was finished to make sure every part worked perfectly.
Solution - 2
There are four main parts (files) to the program:

**Account Creation**
This file creates a new user account, sets up all the user info in the system, and creates a reference file for all the information
Login
This file is called every time a user tries to enter the program. It makes sure that the user enters the correct login credentials that they created and verifies if the person trying to log on is actually the user. It will automatically shut down the whole system if any credential is incorrect.
Creation
This file controls everything with the information. The user picks a file or creates a new one. Then they enter their information into the file and it will all be encrypted using a random generated key. This key can also be used to decrypt the file later if the user wants to look at the contents

**Main**
This is the file that takes all the other files and combines them into one big program that runs smoothly

**Account Creation - 1**
The user is automatically redirected here when they open up the program for the first time
Gathers the user’s information by asking for their name, username, password, and email.
Sends a verification email with a 10-digit security code that needs to be inputted in order for the account to be activated
Sets up the account by adding the information previously gathered into the system for login later
Creates a reference file with all the user’s information encrypted so no one can see the user’s private details
Initializes a random encryption key that will be used to encrypt and decrypt all the user’s information when entered or when read.

**Login**
The user is automatically redirected here every time the program is initialized after the first time opened
The user must type in their username correctly in three tries or the program will automatically shut down
The user must type in their password correctly in three tries or the program will automatically shut down
The user will get a verification email with a 6-digit code that needs to be inputted into the program correctly in at least three times or the program will automatically shut down
The user will automatically be redirected to the creation file if they successfully make it past all the security checks

**Creation**
The user will pick if they want to create a file, create a directory or open a file.
If the user wants to create a file, they will provide a file name and be redirected to the next step
If the user wants to create a directory, they will provide a directory name and make a new file inside that directory
If the user wants to open a file, they can choose to open a file in the current directory or continue to browse subdirectories until they find a file
The user can now select if they want to add and encrypt text to the chosen file or read and decrypt it

**Main**
Combines all the other three pieces of the program so the program flows and functions smoothly
Decides whether the user has made an account and executes the Account Creation file if not. Otherwise, it will execute the Login file
Executes the Creation file after so that the user can pick their file
Redirects the user to entering or reading the text in a file after they have chosen one
Closes and shuts down the program when the user has finished 

**Documentation**
We wanted to create a program that had multiple layers of security for logging in so we decided to make the user make a username and password as usual; on top of that though, we added a verification email service that will send an automated email with a random code to the user
We wanted the user to have multiple options when selecting their files, so we made options for creating new files, creating new directories, opening files, and opening files in deeper subdirectories
We wanted the text file containing information to be completely unreadable to anyone without the program so we made the program so that every time a user enters information into a file, it will automatically be encrypted using a randomly generated key and then added to the file so no one can read what the contents are.

**Development**
The program meets our requirement of having a secure way of logging in with a username, password, and an email security code
The program meets our requirement of making sure no one can access files with information in them without logging in with the app because all the files are automatically encrypted into text that isn't understandable to anyone.
Our program is better than current information manager technology because we have much more security layers and protection against stolen information. We also make the process of logging on and entering information as quick and simple as possible.

**Evaluation**
Our engineering goal for the program was to make a safe and secure place where a user could store their information and no one else could access it. The program also had to be easy to use and make the process of entering information quick.
We did meet and accomplish our engineering goal because we added three security features when logging in, made the whole process easy and fast for the user, and encrypted all the files so the information could only be accessed using our program.




