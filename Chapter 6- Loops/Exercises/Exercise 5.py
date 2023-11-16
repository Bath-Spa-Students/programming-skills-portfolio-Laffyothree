sandwich_orders = ['Grilled Cheese', 'Pastrami', 'Egg Sandwich', 'Pastrami', 
                   'Avocado Toast', 'Pastrami', 'Tuna Sandwich']
finished_sandwiches = []

print ('I am sorry, but the Deli has run out of Pastrami.')
while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')
print()

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print (f'We are currently making your {current_sandwich}, please wait thank you.')
    finished_sandwiches.append(current_sandwich)
print()

for sandwich in finished_sandwiches:
    print (f'Your {sandwich} is done! Enjoy!')
