def play():
    print('Example: "Hey a bird" can go through, but "Hi I\'m Justin" cannot go through.')
    print('Recognize the pattern? Type a word that can go through the Green Glass Door.')
    print('*Hint.* Think about something that is a dessert and is used as a constant in math.')
    answer = input('Answer: ')
    try:
        if(pi_key_check(answer)):
            print('Correct! ' + answer + ' can go through the door.\n')
            return None
        else:
            print('Sorry, ' + answer + ' cannot go through the door. Please try again.\n')    
            play()
    except:
        print('INCORRECT! Please put in an answer.\n')
        play()

def pi_key_check(example):
    pi_key = [3, 1, 4]
    example = example.split(' ')
    for a in range(0, len(pi_key)):
        if(len(example[a]) != pi_key[a]):
            return False       
    return True