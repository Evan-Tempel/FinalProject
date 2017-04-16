import getpass
import bcrypt
import pymysql


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

    # Create the user inside of the database.
    print('Account creation successful!')

def createUsr():

    print('We made it to 2!')
    print('Welcome new user, please follow this wizard to create a new account!')
    newUsr = str(input('Please enter a Username: '))
    newPass = getpass.getpass('Please enter your password: ')
    newPassCheck = getpass.getpass('Please reenter your password: ')

