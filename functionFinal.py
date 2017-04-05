import getpass
import bcrypt

def passCheck(string1, string2):
    if (string1 == string2) == True:
        return True
    if (string1 == string2) == False:
        return False

def login(usrName, usrPassword):
    ask = input('What is your username?')
    askPass = getpass.getpass('Please enter your password: ')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(askPass, salt)
    hash.find(salt)
