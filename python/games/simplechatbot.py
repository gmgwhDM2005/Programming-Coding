while True:
    m=input()
    m=m.lower()
    
    if m=='hello':
        print('Hello!')
    elif m=='help':
        print('Welcome to the chatbot')
    elif m=='how are you':
        print('I guess im doing good, I suppose. And you?')
    elif m=='im good':
        print('Ok great, lets move onto something good. Maybe like social media?')
    elif m=='im not good':
        print('Oh, thats a shame. Why not try talking about something else, eh?')
    elif m=='do you like social media':
        print('No, it is a waste of time. What do you think?')
    elif m=='good':
        print('oh ok')
    elif m=='bad':
        print('Ok.')
    else:
        print('Try saying "help" for something to do')
