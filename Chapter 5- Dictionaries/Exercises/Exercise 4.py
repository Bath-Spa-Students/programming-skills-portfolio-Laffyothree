rivers = {"Río Grande de Cagayán": "Philippines", "Amazon River": "South America", "Zaire River": "Africa"}

#printing each river as a sentence
for x, y in rivers.items():
  print (x, "can be found in the", y + ".")
print()

#printing each river names/keys
for x in rivers.keys():
  print(x)
print()

#printing each country/values
for y in rivers.values():
  print(y)
