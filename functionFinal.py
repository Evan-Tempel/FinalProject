import getpass
import bcrypt
import pymysql


def passCheck(string1, string2):
    if (string1 == string2) == True:
        return True
    if (string1 == string2) == False:
        return False

def login():

    ask = input('What is your username?')
    askPass = getpass.getpass('Please enter your password: ')
    salt = bcrypt.gensalt()
    hash_PW = bcrypt.hashpw(askPass, salt)

    # Connect to DB to select username and to select password hash

    hashEval = (hash_PW == bcrypt.hashpw(askPass, hash_PW))
    return hashEval

def createDBUser(username, usrPassword):
    conn = pymysql.connect(host='putIPhere', unix_socket='/tmp/mysql.sock', user='root', passwd=None, db='mysql')