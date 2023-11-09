#existing glosarry
exst_glossary = {
  "List:\n": "is a data structure in Python that is a mutable, or changeable, ordered sequence of elements.", 
  "F-strings:\n": "provides a concise, readable way to include the value of Python expressions inside strings.", 
  "Variables:\n": "are simply a containers for storing data values.",
  "Def:\n": "is short for “define”. It's a keyword that you need to define a function (aka method).",
  "Concatenating:\n": "is obtaining a new string that contains both of the original strings."
}

#adding 5 more terms
new_key = "Int:\n"
new_value = "Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length."
new_key1 = "Float:\n"
new_value1 = "is a function or reusable code in the Python programming language that converts values into floating point numbers."
new_key2 = "Boolean:\n"
new_value2 = "a result that can only have one of two possible values: true or false."
new_key3 = "Tuple:\n"
new_value3 = "a similar “container” as list with a difference that you cannot update the values in a tuple."
new_key4 = "String:\n"
new_value4 = "is a collection of alphabets, words or other characters."

#making and printing update/changes
updated_glossary = {**exst_glossary, new_key: new_value, new_key1: new_value1, new_key2: new_value2,
 new_key3: new_value3, new_key4: new_value4}
for key, value in updated_glossary.items():
    print(key, value)
