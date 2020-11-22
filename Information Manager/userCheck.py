#Imports
import os
import os.path


#Variables
pathcheck = os.path.join(os.getcwd(), "accountID.txt")
print(os.getcwd())
try:
    file = open("accountID.txt")
    from logIn import logIn
except:
    from accountCreation import accountCreation





