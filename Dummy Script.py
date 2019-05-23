
def final_score(johns_testscore):
    n = 0
    while n<5:
        johns_testscore= johns_testscore+10
        n+=1
    print('final score', johns_testscore)



def countdown():
    n=10
    print('Start the countdown')
    while n!=0:
        print(n)
        n=n-1
    print('Blastoff!')

    

#infinite loop keeps running until correct name is entered
#break command allows that vs a timed loop
'''
while True:
    print('Please type your name.')
    name = input()
    if name == 'your name':
        break
print('Thank you!')
'''

#Ctrl+C to stop infinite loop
''' 
while True:
    print('Hello World')
'''


#continue - revert back to the beginning of program until
#correct name is entered
'''
while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')
'''

'''
name = ''
#Makes you enter some value other than blank, otherwise, it will repeat
while not name:
    print('Enter your name:')
    name=input()
print('How many guests will you have?')
numOfGuests = int(input())
if numOfGuests >= 8:
    print('Be sure to have enough room for all your guests.')
elif numOfGuests > 4:
    print('You may have room')
else:
    print('There is room')
print('Done')
'''

'''
total = 0
for num in range(101):
    total = total + num
print(total)
'''

'''
import random
def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'

r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)
'''
#quicker way to get a response by running command
# print(getAnswer(random.randint(1, 9)))

import random
def guessthenumber():
    guesses=0
    secret_number= random.randint(1,9)
    print('Choose a number between 1-9')
    while True:
        print('What number is it?')
        guess= int(input())
        if guess < secret_number:
            print('guess higher')
            guesses+=1
            continue
        elif guess > secret_number:
            print('guess lower')
            guesses+=1
            continue
        else:
            print('You got it!')
            guesses+=1
            break
    print('it took you ' + str(guesses) + ' guesses!')



def collatz():
    print('Enter number:')
    num=int(input())
    while num != 1:
        if num % 2==0:
            num=num//2
            print(num)
        else: #odd number
            num= (num*3)+1
            print(num)
    

def birthday():
    birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
    while True:
        print('What is your name: (Blank to exit program)')
        name = input()
        if name == '':
            break

        if name in birthdays:
            print(birthdays[name] + ' is the birthday of ' + name)
        else:
            print('No birthday listed for ' + name)
            print('What is his birthday?')
            bday = input()
            birthdays[name]=bday
            print('Birthday database updated')

'''
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printBoard(theBoard)
'''

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
def displayInventory(inventory):
    print('Inventory:')
    total = 0
    for k,v in inventory.items():
        print(str(v) + ' ' + k)
    for t in inventory.values():
        total += t
    print('Total number of items:', total)  
    
picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}    
def PrintItems(things, leftwidth, rightwidth):
    print('PICNIC ITEMS'.center(leftwidth + rightwidth, '-'))
    for k,v in things.items():
        print(k.ljust(leftwidth,'.') + str(v).rjust(rightwidth))
        

        
