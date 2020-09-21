def play():
    print('Example: A tambourine can go through, but a banjo cannot go through.')
    print('Recognize the pattern? Type a word that can go through the Green Glass Door.')
    answer = input('Answer: ')
    try:
        if(all_vowel_check(answer)):
            print('Correct! ' + answer + ' can go through the door.\n')
            return None
        else:
            print('Sorry, ' + answer + ' cannot go through the door. Please try again.\n')    
            return play()
    except:
        print('BLANK ANSWER! Please put in an answer.\n')
        return play()

    
def all_vowel_check(example):
    if 'a' and 'e' and 'i' and 'o' and 'u' in example:
        return True     
    return False