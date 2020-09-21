def play():
    print('Example: A bat can go through, but a beaver cannot go through.')
    print('Recognize the pattern? Type a word that can go through the Green Glass Door.')
    answer = input('Answer: ').lower()
    try:
        if(Isogram(answer)):
            print('Correct! ' + answer + ' can go through the door.\n')
            return None
        else:
            print('Sorry, ' + answer + ' cannot go through the door. Please try again.\n')    
            play()
    except:
        print('BLANK ANSWER! Please put in an answer.\n')
        play()

def Isogram(example):
    example = list(example)   
    example.sort()
    for a in range(0, len(example) - 1):
        if(example[a] == example[a + 1]):
            return False
    return True