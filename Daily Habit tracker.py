sName = input('What is your name: ')


iMood = int(input('Hello, ' + sName + '. What is your mood like today? (1/10): '))

if iMood <= 5:
    sCode = input('Oh thats a shame ' + sName + '. Hopefully your day tomorrow is better. Have you coded today (Yes/No): ')

elif iMood > 5 and iMood < 10:
    sCode = input('Oh thats great ' + sName + '! At least you had a wonderful day. Have you coded today (Yes/No): ')

else:
    print('Error! Please restart the programme as you did not pick a number between 1-10')

sClean = input('Alright, have you stayed clean today? (Yes/No): ')

print('=== Todays Summary ===')
print('Name: ' + sName)
print('Mood: ' + str(iMood))
print('Coded: ' + sCode)
print('Clean: ' + sClean)

if sClean.lower() == 'yes' and sCode.lower() == 'yes':
    print('Wow, you did great today. It shows great decipline. You did good today.')

else:
    print('Its not perfect but nobody is. What matters is that you tried.')