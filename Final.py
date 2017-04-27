import getpass, os.path, sys, functionFinal, bcrypt
import functionFinal


version = '1.0'

print('Welcome to PyPassword Manager Version: ' + version)

ask_usr = str(input('Are you a return user(1)? or a new user(2)? '))

check = True

username, password = functionFinal.login()

while check == True:
    print('We made it!')


    if ask_usr == '1':

        functionFinal.returningUsr(username, password)

        ask = input('Would you like to exit?(y/n) ')

        if ask == 'y':
            check = False
        elif ask == 'n':
            check == True
            ask_usr = '1'

    elif ask_usr == '2':

        functionFinal.createDBUser()

        ask = input('Would you like to exit?(y/n) ')

        if ask == 'y':
            check = False
        elif ask == 'n':
            check == True
            ask_usr = '1'
        else:
            print('You broke me')
