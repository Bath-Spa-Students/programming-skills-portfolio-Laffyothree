print ("Here is the previous guest list:")
prev_list = ['Gabriel Mns', 'Mark Gie Bgy', 'McDaniel Drn', 'Jermaine Crpn', 'Ashley Cbg']
print (f'''{prev_list [0]}
{prev_list [1]}
{prev_list [2]}
{prev_list [3]}
{prev_list [4]}''') 
print()

print (f"but {prev_list [4]} informed me that he can't make it to the party, so we made a new one.")
print()

print ("And here is the new official guest list:")
prev_list.remove(prev_list [4]) 
new_list = ['Gabriel Mns', 'Mark Gie Bgy', 'McDaniel Drn', 'Jermaine Crpn', 'Kenneth Llgn']
print (f'''{new_list [0]}
{new_list [1]}
{new_list [2]}
{new_list [3]}
{new_list [4]}''') 
