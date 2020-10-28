#Initiialization
print("Welcome to the Information Manager.")
print("Here you can manage all your information in a secure and organized space")
print("If you have an account, you will need to verify yourself")
print("If you are new, You will need to create an account\n")

#Account Info
def accountIDfile(info):
    addInfo = open("accountID.txt", "a")
    addInfo.write(info)

#import pathlib
#import os.path
#import filecmp
#import tempfile
#import shutil
#import pickle
#import zipfile
#import getpass
#import sys
#import os


