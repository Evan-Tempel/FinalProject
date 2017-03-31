import getpass, os.path


version = '0.1'

print('Welcome to PyPassword Manager Version: ' + version)

ask_usr = int(input('Are you a return user(1)? or a new user(2)? '))

fileCheck = os.path.isfile('test.txt')

if ask_usr == 1:

    print('Welcome back returning user.')
    usrName = input('Username: ')
    passwd = getpass.getpass("Password: ") # Only shows up when running in terminal. Not in PyCharm.

    addorReview = int(input('Would you like to view usernames and passwords(1) or add new ones(2)'))

    if addorReview == 1:
        if fileCheck == True:
            usr_passFile = open('test.txt', 'r')
            print(usr_passFile.read())
            cont = int(input('Would you like to add to this(1) or exit the program(2)?'))
        elif fileCheck == False:
            print('You do not have anything related to this account.')
        else:
            print('Something went very wrong. Panic.')
    elif addorReview == 2:
        if fileCheck == True:
            usr_passFile = open('test.txt', 'a')
        elif fileCheck == False:
            usr_passFile = open('test.txt', 'w')
        else:
            print('Something went wrong, please panic!')
        print('We made it to two')

    else:
        print('One does not comprehend.')

elif ask_usr == 2:

    print('We made it to 2!')

else:

    print('We broke it! :D')
