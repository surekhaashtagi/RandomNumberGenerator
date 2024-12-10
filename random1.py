import random
target=random.randint(1,100)
while True:
    userchoice=int(input("Guess the number..."))
    if userchoice == 'Q':
        break
    userchoice=int(userchoice)
    if userchoice == target:
        print('Guess is currect Game is over...')
    elif(userchoice<target):
        print('Your guess is to small guess bigger number..')
    else:
        print('your number is to bigg guess the bigger number..')

print('your guess is currect..')
print('-------GAME OVER--------')