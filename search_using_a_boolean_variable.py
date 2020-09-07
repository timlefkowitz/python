#search_using_a_boolean_variable
found = False
print('Before', found)
for value in [9, 31, 41, 2, 14, 51] :
  if value == 3 :
    found = True
  print(found, value)
print('after', found)
