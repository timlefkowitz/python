#counting in a loop
zork = 0
print('Before', zork)
for thing in [9, 42, 53, 2, 4, 12] :
    zork = zork + thing
    print(zork, thing)
print('After', zork)
