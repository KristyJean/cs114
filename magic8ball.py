print('Giiiirl you wanna know how good you look today? Lemme tell ya')

from time import sleep


sleep(2)
print('Now let me get a good look at you')
sleep(3)


import random
def getanswer(answerNumber):
    if answerNumber == 1:
        return 'Look like poo'
    elif answerNumber == 2:
        return 'Potato-esk..'
    elif answerNumber == 3:
        return 'Your hair looks good.. Your outfit however...'
    elif answerNumber == 4:
        return 'You look okay... JUST ok'
    elif answerNumber == 5:
        return 'I like your shoes'
    elif answerNumber == 6:
        return 'You look pretty today'
    elif answerNumber == 7:
        return 'You look fantastic'
    elif answerNumber == 8:
        return 'You are so beautiful!'
    elif answerNumber == 9:
        return 'You are a goddess!'

r = random.randint(1,9)

fortune = getanswer(r)

print(fortune)
