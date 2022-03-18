lotto = [2, 14, 26, 41, 63]
print(lotto)
lotto[2] = 29
print(lotto)

for i in range(len(lotto)):
    num = lotto[i]
    print(num)

stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)
stuff.append('cookie')
print(9 in stuff)

friends = ['Justin','Jared', 'Nate']
print(friends)
friends.sort()
print(friends)

numlist = list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print('Average: ', average)
