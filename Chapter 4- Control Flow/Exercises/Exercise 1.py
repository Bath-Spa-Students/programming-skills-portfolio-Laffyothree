#passes the if test
alien_color = ("A green alien just got shot down!")
print (alien_color)

if ("green") in alien_color: 
    print (" You just earned 5 points :)")
print()

#fails the if test
alien_color = ("A green alien just got shot down!")
print (alien_color)

if ("yellow" or "red") in alien_color: 
    print (" You just earned 5 points :)")
