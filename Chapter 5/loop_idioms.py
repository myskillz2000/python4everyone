my_list = [9, 41, 12, 3, 74, 15]

print('Before')
for thing in my_list : # Could have used the random library here if we don't care about the numbers
    print(thing)

print('After')

largest_so_far = None
print('Before', largest_so_far)
for the_num in my_list :
    if largest_so_far is None:
        largest_so_far = the_num
    elif the_num > largest_so_far:
        largest_so_far = the_num

print('After', largest_so_far)

""" Counting """

pork = 0
print('Before', pork)
for thing in my_list :
    pork = pork +1
print('After', pork)

total = 0
print('Before', total)
for thing in my_list :
    total = total + thing
print('After', total)

count = 0
sum = 0
print('Before', count, sum)
for value in my_list :
    count = count + 1
    sum = sum + value
print('After', count, sum, sum / count)

""" Filter in a loop """

print('Before')
for value in my_list :
    if value > 20:
        print('Large Number: ', value)
print('After')

""" Boolean Variables to see if items is in list """

found = False
print('Before', found)
for value in my_list :
    if value == 3 :
        found = True
        break
print('After', found)