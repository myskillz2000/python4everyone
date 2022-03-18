fruit = 'banana'
letter = fruit[1]

print(letter)
print(len(fruit))

index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

for letter in fruit:
    print (letter)

count = 0
for letter in fruit :
    if letter == 'a' :
        count = count + 1
print(count)

s = 'Monty Python'
print(s[0:4])
print(s[6:7])
print(s[6:20])
print(s[:2])
print(s[8:])
print(s[:])

a = 'Hello '
b = a + 'There'
print(b)

if 'a' in fruit:
    print('Found it')

greet = "Hello Bob"
zap = greet.lower()
proper = greet.capitalize()
upper = greet.upper()

print(zap)
print(proper)
print(upper)

nstr = greet.replace('Bob', 'Jane')

print(nstr)

