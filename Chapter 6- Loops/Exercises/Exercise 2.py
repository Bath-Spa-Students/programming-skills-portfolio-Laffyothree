prompt = '\nWelcome to the LA Theaters!'
prompt += '\nMay I ask what is your age?'

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print ("The tickets are free for 3 years old below, enjoy the movie!")

    elif age < 13:
        print ("The ticket will be $10, thank you.")

    else:
        print ("The ticket will be $15, thank you.")
