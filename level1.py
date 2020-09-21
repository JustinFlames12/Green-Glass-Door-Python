def play():
    print('Example: A dell can go through, but an acer cannot go through.')
    print('Recognize the pattern? Type a word that can go through the Green Glass Door.')   
    answer = input('Answer: ').lower()
    if(DoubleLetters(answer)):
        print('Correct! ' + answer + ' can go through the door.\n')
        return None
    else:
        print('Sorry, ' + answer + ' cannot go through the door. Please try again.\n')    
        return play()

def DoubleLetters(example):
    a = 0
    for a in range(len(example) - 1):
        b = str(example[a])
        c = str(example[a + 1])
        if( b == c):
            return True
    return False

