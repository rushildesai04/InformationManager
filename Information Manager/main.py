#The Information Manager - Rushil Desai and Yagnesh Veeraraghavan
print("Welcome to the Information Manager.")
print("Here you can manage all your information in a secure and organized space")
print("If you have an account, you will need to verify yourself")
print("If you are new, You will need to create an account")
print("Created By: Rushil Desai and Yagnesh Veeraraghavan\n")
def main():
    from creation import createOrOpen
    from creation import decision
    createOrOpen()
    decision()
main()
