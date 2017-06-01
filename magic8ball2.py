"""Magic 8 ball using lists"""
import random


# The question
seed_num = input('Speak your mind. What do you wish to know?')



answers = ['It will be a long road before you get there',
'This does not matter. Look beyond, and you will find what you really need',
'Maybe someday',
'Only after you become who you must be',
'You will never obtain this desire',
'Yes, but not here. You must go to a distant land.',
'Let a little more time pass, ask again later.',
'nah sucka']


if seed_num .startswith('Will'):
    output = answers[:4]
elif seed_num .startswith('Do'):
    output = answers [4:]
else:
    output = answers[:]

#sprint(output)


print(output[random.randint(0, len(answers) - 1)])
