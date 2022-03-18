"""import os

for filename in os.listdir(os.getcwd()):
    with open(os.path.join(os.getcwd(),'sample.txt'), 'r') as f:
        print(f.read())"""

# The above would be able to read the current working directory of the file.

fhand = open('sample.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count: ', count)

fhand = open('sample.txt')
inp = fhand.read()
print(len(inp))
print(inp[:20])

fhand = open('sample.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:') :
        print(line)

fname = input('Enter the file name:  ')
try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    quit()

count = 0
for line in fhand:
    if line.startswith('Subject:') :
        count = count + 1
print('There were ', count, ' subject ines in ', fname)