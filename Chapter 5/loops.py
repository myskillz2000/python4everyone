while True:
    line = input('> ')
    if line[0] == '#' :
        continue # Stops and goes to the top of the loop again.
    if line == 'done' :
        break # Stops and exits the loop
    print(line)
print('Done!')


for i in [5, 4, 3, 2, 1 ] : # Would have been better or easier to use range here.
    print(i)
print('Blastoff!')

friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends :
    print('Hi my friend', friend)
print('Done!')