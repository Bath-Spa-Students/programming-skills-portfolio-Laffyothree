sandwich_orders = ['Grilled Cheese', 'Egg Sandwich', 'Avocado Toast', 'Tuna Sandwich']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print (f'We are currently making your {current_sandwich}, please wait thank you.')
    finished_sandwiches.append(current_sandwich)
print()

for sandwich in finished_sandwiches:
    print (f'Your {sandwich} is done! Enjoy!')
