print ("The official guest list includes:")
new_list1 = ['Gabriel Mns', 'Mark Gie Bgy', 'McDaniel Drn', 'Jermaine Crpn', 'Kenneth Llgn']
print (new_list1)
print()

print ("Due to certain problem, we had to make some adjustments. Here is the modified list:")

new_list2 = ['Gabriel Mns', 'Mark Gie Bgy', 'McDaniel Drn', 'Jermaine Crpn', 'Kenneth Llgn']
new_list2.pop(0)
new_list2.pop(1)
new_list2.pop(2) 
print (new_list2)
print()

print ("GUESTS WHO HAVE BEEN REMOVED:")
new_list3 = ['Gabriel Mns', 'McDaniel Drn', 'Kenneth Llgn']
msg = (''', 
Due to a certain problem with the table arrangement we made significant changes to the guest list,
we regret to inform you that all the seats are occupied and we can no longer invite you to the dinner. 
Thank you for your understanding; we hope to make amends in the near future.''')
print (f'Dear {new_list3 [0] + msg }\n')
print (f'Dear {new_list3 [1] + msg }\n')
print (f'Dear {new_list3 [2] + msg }\n')

print ("GUESTS WHO ARE STILL INVITED:")
new_list4 = ['Mark Gie Bgy', 'Jermaine Crpn']
msg = (''', 
Due to a certain problem with the table arrangement we made significant changes to the guest list,
but we are delighted to inform you that you are still invited to the dinner. See you there!''')
print (f'Dear {new_list4 [0] + msg }\n')
print (f'Dear {new_list4 [1] + msg }')
