#An_interesting_loop_2
numlist = list()
while True :
 //   inp = input('Enter a number: ')
    inp = input('Enter a String: ')
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value)
    
average = sum(numlist) / len(numlist)
