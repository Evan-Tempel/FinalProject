import getpass
import bcrypt
import pymysql


def login():

    ask = input('What is your username?')
    askPass = getpass.getpass('Please enter your password: ')
    salt = bcrypt.gensalt()
    hash_PW = bcrypt.hashpw(askPass, salt)
    conn = pymysql.connect(host='putIPhere', unix_socket='/tmp/mysql.sock', user=ask, passwd=hash_PW, db='PasswordManager')

    cur = conn.cursor()
    check = True

    while check == True:


        view = input('Would you like to (1) view your list or (2) add to it or (3) exit')

        if view == '1':
            print('We made it to 1')
            cur.execute("SELECT * FROM users")
        elif view == '2':
            print('We made it to two')

            accnt = str(input('Please enter the username you want to add: '))
            accntPasswd = getpass.getpass('Please enter the password to that account: ')

            cur.execute('INSERT INTO users ( username, passwd) VALUES /s,/s', (accnt, accntPasswd))

        elif view == '3':
            print('We made it to three')
            check = False
        else:
            print('We\'ve ,ade a grave mistake')
            check = False


def createDBUser():

    usrName = str(input('Please enter the desired username: '))
    usrPasswd = getpass.getpass('Please enter the desired password: ')

    conn = pymysql.connect(host='putIPhere', unix_socket='/tmp/mysql.sock', user='root', passwd=None, db='mysql')

    # Create the user inside of the database.
    print('Account creation successful!')

def createUsr():

    print('We made it to 2!')
    print('Welcome new user, please follow this wizard to create a new account!')
    newUsr = str(input('Please enter a Username: '))
    newPass = getpass.getpass('Please enter your password: ')
    newPassCheck = getpass.getpass('Please reenter your password: ')

