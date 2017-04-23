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

def createDBUser():
    conn = pymysql.connect(host='localhost', user='root', passwd='Badguy2112', db='test')

    user1 = input('PLease enter the username: ')

    userPasswd = getpass.getpass('Please enter the password: ')
    userPasswdcheck = getpass.getpass('Please confirm the password: ')
    if userPasswd == userPasswdcheck:
        cur = conn.cursor()
        cur.execute('CREATE USER %s@localhost IDENTIFIED BY %s', (user1, userPasswd))

        cur.execute('CREATE TABLE %s (username VARCHAR(50) DEFAULT NULL, usrpassword CHAR(61))' % user1)


        cur.execute('GRANT ALL PRIVILEGES ON user.%s TO %s@localhost' % (user1, user1))


    print('Account creation successful!')

def createUsr():

    print('We made it to 2!')
    print('Welcome new user, please follow this wizard to create a new account!')
    newUsr = str(input('Please enter a Username: '))
    newPass = getpass.getpass('Please enter your password: ')
    newPassCheck = getpass.getpass('Please reenter your password: ')

