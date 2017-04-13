import getpass, os.path, sys, functionFinal


version = '0.1'

print('Welcome to PyPassword Manager Version: ' + version)

ask_usr = int(input('Are you a return user(1)? or a new user(2)? '))

fileCheck = os.path.isfile('test.txt')

if ask_usr == 1: # Returning User.

    print('Welcome back returning user.')
    usrName = input('Username: ')
    passwd = getpass.getpass("Password: ") # Only shows up when running in terminal. Not in PyCharm.

    # Add Code here to make sure the Username and Password is valid

    addorReview = int(input('Would you like to view usernames and passwords(1) or add new ones(2)'))

    if addorReview == 1: # User is reviewing usernames and passwords

        if fileCheck == True: # If user has previously saved a file, this is where it should be.

            usr_passFile = open('test.txt', 'r')
            print(usr_passFile.read())
            cont = int(input('Would you like to add to this(1) or exit the program(2)?')) # Needs to send be sent to a while loop.

        elif fileCheck == False: # Users first time signing in, should not have any information

            print('You do not have anything related to this account.')

        else: # We should never be here, this is bad. Break the code to ensure integrity.

            print('Something went very wrong. Panic.')
            sys.out()

    elif addorReview == 2: # User wants to add a username/password set

        if fileCheck == True: # User's file has been created already. Append instead of write.

            usr_passFile = open('test.txt', 'a')
            usr = str(input('What is the username: '))
            password = getpass.getpass('Password for that username: ')
            password2 = getpass.getpass('Re-enter the password: ')

            if password == password2: # Password check.
                usr_passFile.write('Username: ' + usr + 'Password: ' + password2)
                usr_passFile.close()

        elif fileCheck == False: # Users first time. Create a new file.

            usr_passFile = open('test.txt', 'w')

        else:

            print('Something went wrong, please panic!')

        print('We made it to two')

    else:

        print('One does not comprehend.')

elif ask_usr == 2: # New user, registration control

    print('We made it to 2!')
    print('Welcome new user, please follow this wizard to create a new account!')
    newUsr = str(input('Please enter a Username: '))
    newPass = getpass.getpass('Please enter your password: ')
    newPassCheck = getpass.getpass('Please reenter your password: ')

    if newPass == newPassCheck:
        functionFinal.createDBUser()


else: # Broken, we should never be here.

    print('We broke it! :D')
