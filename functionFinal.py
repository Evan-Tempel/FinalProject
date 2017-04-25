import getpass, bcrypt, pymysql, random, string


saltpass = bcrypt.gensalt()

def login():

    username = input('Please enter a username')
    password = getpass.getpass('Please enter the password: ')

    enpass = password.encode('utf-8')
    hash_PW = bcrypt.hashpw(enpass, saltpass)
    depass = hash_PW.decode('utf-8')

    conn = pymysql.connect(host='192.168.1.9', user=username, passwd=depass, db=username)

    return username,depass

def createDBUser():
    conn = pymysql.connect(host='192.168.1.9', user='Linux_Admin_Evan', passwd=getpass.getpass('Please enter password: '))

    createUsr = input('Please enter username: ')

    createPass = getpass.getpass('Please enter password: ')

    enpass = createPass.encode('utf-8')
    hash_PW = bcrypt.hashpw(enpass, saltpass)

    depass = hash_PW.decode('utf-8')


    cur = conn.cursor()
    cur.execute('CREATE DATABASE %s' % createUsr)
    cur.execute('USE %s' % createUsr)

    cur.execute('CREATE USER %s@192.168.1.9 IDENTIFIED BY %s', (createUsr, depass))
    cur.execute('CREATE TABLE %s (username VARCHAR(50) DEFAULT NULL, userpassword CHAR(76))' % createUsr)
    cur.execute('GRANT ALL PRIVILEGES ON *.* TO %s@192.168.1.9', createUsr)

    print('Account creation successful!')

    return createUsr, depass


def returningUsr(username, password):

    conn = pymysql.connect(host='192.168.1.9', user=username, passwd=password, db=username)

    print('Welcome new user, please follow this wizard to create a new account!')

    askPass = str(input('Would you like to (1) add your own password or (2) use our random string generation or (3) View accounts and passwords?'))

    cur = conn.cursor()

    if askPass == '1':

        askAccnt = str(input('Please give an account name: '))

        newPass = getpass.getpass('Please enter a password: ')
        newPassCheck = getpass.getpass('Please re-enter the password: ')
        if newPass == newPassCheck:
            enpass = newPass.encode('utf-8')
            hash_PW = bcrypt.hashpw(enpass, saltpass)

            depass = hash_PW.decode('utf-8')

            cur.execute('INSERT INTO %s VALUES ("%s", "%s")' % (username, askAccnt, depass))
            conn.commit()

    elif askPass == '2':
        askAccnt = str(input('Please give an account name: '))

        ranString = ''.join(
            random.SystemRandom().choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in
            range(24))

        enpass = ranString.encode('utf-8')
        hash_PW = bcrypt.hashpw(enpass, saltpass)

        depass = hash_PW.decode('utf-8')

        cur.execute('INSERT INTO %s VALUES ("%s", "%s")' % (username, askAccnt, depass))
        conn.commit()

    elif askPass == '3':
        cur.execute('SELECT * FROM %s')