def play():
    print('Example: My name is Justin and I can bring juices through the door.')
    print('However, I cannot bring sodas through the door.')
    print('Recognize the pattern? Type a word that can go through the Green Glass Door.')   
    name = input('What is your name? ').lower()
    answer = input('Hey ' + name + ', what are you bringing through the door? ').lower()
    try:
        if(name[0] == answer[0]):
            party_item = answer
            print('Correct ' + name + ', you can bring ' + answer + ' through the door.\n' )
            return None
        else:
            print('Sorry ' + name + '. ' + answer + ' cannot go through the door. Please try again.\n' )
            play()
    except:
        print('BLANK ANSWER! Please put in an answer.\n')
        play()