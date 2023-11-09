#simply put down your age
Baby = 1 
Toddler = 2
Kid = 4
Teenager = 13
Adult = 20
Elder = 65
Old = 100

age = int(input("How old are you? "))

if age < Toddler:
    print ("You're still a baby.")

elif age < Kid:
    print ("You're a toddler.") 

elif age < Teenager:
    print ("You're still a kid.") 

elif age < Adult:
    print ("You're a teenager.") 

elif age < Elder:
    print ("You're an adult.") 

elif age < Old:
    print ("You're an elder person.") 

else: 
    print ("Seriously, what's your age?")
