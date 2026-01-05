sName = input('What is your name: ')

sQues = input('Your name is ' + sName + ', correct? (T/F) ')

names = []
names.append(sName)

    
while sQues == 'F':

    sName = input('Then what is your name: ')

    names.append(sName)

    sQues = input('So your name is ' + sName + ', correct? (T/F) ')

if sQues == 'T':
    print('Wow thats a beautiful name. Welcome ' + sName)
    print()
    print(names)

    if sQues != 'T' and 'F':
        sQues = input('Please enter T/F: ')

if sQues != 'T' and 'F':
        sQues = input('Please enter T/F: ')
                