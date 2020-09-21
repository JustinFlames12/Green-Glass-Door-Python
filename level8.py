import random
def play():
    print('Example: (Based on the word "cinema", "iceman" can go through the door.')
    print('Recognize the pattern? Type a word that can go through the Green Glass Door.')
    ana_keywords = ['games', 'coal', 'peek', 'filer']
    rand_ana = random.randint(0, 3)
    answer = input(f'Based on the word "{ana_keywords[rand_ana]}", Answer: ')
    try:
        if(Anagram(answer, ana_keywords[rand_ana])):
            print('Correct! ' + answer + ' can go through the door.\n')
            return None
        else:
            print('Sorry, ' + answer + ' cannot go through the door. Please try again.\n')    
            return play()
    except:
        print('BLANK ANSWER! Please put in an answer.\n')
        return play()

def Anagram(example, anagram_word):
    example = list(example)   
    example.sort()
    anagram_word = list(anagram_word)
    anagram_word.sort()
    for a in range(0, len(example)):
        if(example[a] != anagram_word[a]):
            return False
    return True