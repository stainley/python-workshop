# Bot number 1:
print('What is your name?')
name = input()
print('Fascinating.', name, 'is my name too.')
print('Have you thought about black holes today?')
yes_no = input()
print('I am so glad to said', yes_no, '. I was thinking the same thing.')
print('We\'re kindred spirits,', name, '. Talk later.')

# Bot number 2:
print('How intelligent are you? 0 is very dumb. And 10 is a genius')
smarts = input()
smarts = int(smarts)


if smarts <= 3:
    print('I don\'t believe you')
    print('How bad of a day are you having? 0 is the worst, and 10 is the best.')

    day = int(input())
    if day <= 5:
        print('If I was human, I would give you a hug.')
    else:
        print('Maybe I should try your approach.')
elif smarts <= 6:
    print('I think you\re actually smarter.')
    print('How much time do you spend online? 0 is none and 10 is 24 hours a day.')
    hours = int(input())
    if  hours <= 4:
        print('That\'s the problem.')
    else:
        print('And I thought it was only me.')
elif smarts <= 8:
    print('Are you human by change? Wait. Don\'t answer that.')
    print('How human are you? 0 is not at all and 10 is human all the way.')
    human = int(input())
    if human <= 5:
        print('I knew it.')
    else:
        print('I think this courtship is over.')
else:
    print('I see... How many operating systems do you run?')
    os = int(input())
    if os <= 2:
        print('Good thing you\'re taking this course.')
    else:
        print('What is this? A competition?')

