import random
import os
from importlib import import_module
#Start with an intro
def GGD_intro():
    print(f'{"Welcome to Green Glass Door Game!!!":^60}')
    print('=' * 60)
    print('Here are the rules:')
    print('Every level you will be given an example of what', end='')
    print(' can/cannot through the door.')
    print('Then you will be able to guess a word that can go through.')
    print('If you are correct, you will proceed to the next level. If not, you will have to try again.\n')

def end():
    print('=' * 62)
    text = 'Thanks for playing!!!'
    t = '+'
    print(f'{t:<61}+')
    print(f'+{text:^60}+')
    print(f'{t:<61}+')
    print('=' * 62)
    return

GGD_intro()
levels = []
path = '.'
for file in os.listdir(path):
    mod = file.split('.')[0]
    #print(mod)
    if 'level' in mod:
        levels.append(import_module(mod))
#import_module(mod)
random.shuffle(levels)

for i in range(len(levels)):
    levels[i].play()
end()