import random 
# the main strings containing all possible characters are defined here
mainstring = 'abcdefghijklmnopqrstuvwxyz'
upperstring = mainstring.upper()
numstring = '1234567890'
specialstring = '!@#$%^&*|()_+'

def mainmenu():
    print('-- Password generator --')
    print('Choose option:')
    print('1: generate password')
    print('2: exit the program')
    user_choice = int(input('Your choice: '))
    if user_choice == 1:
        return True  
    elif user_choice == 2:
        return False 
    else:
        return 'invalid'
def generator():
    passnumber = int(input('Provide Password Length: '))
    upperchoice = input('Use uppercase letters? (y/n): ')
    numchoice = input('Use digits? (y/n): ')
    specialchoice = input('Use special characters? (y/n): ')
    generator_string = mainstring
    if upperchoice == 'y':
                     generator_string = generator_string + upperstring
    if numchoice == 'y':
                     generator_string = generator_string + numstring
    if specialchoice == 'y':
                     generator_string = generator_string + specialstring
    i=0
    password=''
    while i<passnumber:
        randomletter = random.choice(generator_string)
        password = password + randomletter
        i+=1
    return password
        
def exit():
    print('Bye!')
                    
    
 
main_var = mainmenu()
if main_var == 'invalid':
    print('Please enter a correct value\n\n')
    main_var = mainmenu()
if main_var == True:
          print('Generated password: ',generator())
if main_var == False:
          exit()