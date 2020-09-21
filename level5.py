import random
def play():
    print('30 => 6\n6 => 3\n3 => 5\n5 => 4\n4 => cosmic')
    print('Recognize the pattern? Type the next numbers in the correct order that goes through the GGD. *Only use numbers*.')
    chosennum = random.randint(0, 101)
    CosmicGame(chosennum * 2 + 1)

def CosmicGame(number):
    try:
        pickednum = ''
        with open("Number 1-100 (spelled out).txt", "r") as nspel:
            for lines in range(number):
                pickednum = nspel.readline()
                lines += 1
        phraselength = pickednum[pickednum.index('=') + 2:]
        pickednum = pickednum[0:pickednum.index('=') - 1]
        pickednum += ' => '
        print(pickednum + "", end='')
        cosnum = int(input())
        if(cosnum == int(len(phraselength) - 1)):
            if(cosnum == 4):
                cosmic = input('4 => ')
                if(cosmic == 'cosmic'):
                    print('CORRECT! The order above can go through the door.\n')
                    return None
                else:
                    print('Sorry, the order above cannot go the door. Please try again. \n')
                    play()
            CosmicGame(cosnum * 2 + 1)
        else:
            print('Sorry, the order above cannot go the door. Please try again. \n')
            play()
    except EnvironmentError:
        print('Sorry, could not find the file \n')
    except ValueError:
        print('NOT A NUMBER! Please input a number as your number. \n')
        play()