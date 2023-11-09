#list of "pet" dictionaries
pets = [{"Pet:": "Dog", "Type of pet:": "Male American Bully", 
          "Pet Name:": "Pablo", "Name of Owner/s:": "Fuffy & Fream\n"},
         
        {"Pet:": "Fish", "Type of pet:": "Male Clown Fish", 
         "Pet Name:": "Nemo", "Name of Owner/s:": "Marley\n"},
   
        {"Pet:": "Cat","Type of pet:": "Male Scottish Fold", 
          "Pet Name:": "Spinx", "Name of Owner/s:": "Tres"}]

#printing each pet's information
for dic in pets:
    for x, y in dic.items():
        print(x, y)
