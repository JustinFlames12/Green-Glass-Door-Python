def play():
    print('Example: A civic can go through, but a corvette cannot go through.')
    print('Recognize the pattern? Type a word that can go through the Green Glass Door.')
    answer = input('Answer: ').lower()
    try:
        if(Palindrome(answer)):
            pali = answer
            print('Correct! ' + answer + ' can go through the door.\n')
            return None
        else:
            print('Sorry, ' + answer + ' cannot go through the door. Please try again.\n')    
            play()
    except:
        print('BLANK ANSWER! Please put in an answer.\n')
        play()
    
def Palindrome(example):
    a = 0
    for a in range(len(example)//2):
        if(example[a] != example[len(example) - a - 1]):
            return False
    return True