print('\nMAKE YOUR OWN PIZZA :)')
prompt= 'Please add your desired toppings & type "Quit" when finish:'


while True:
    toppings = input(prompt)
    if toppings != "quit" :
        print (f'You added {toppings} on your pizza.')

    else:
        print ('Your pizza is ready!')
        break
