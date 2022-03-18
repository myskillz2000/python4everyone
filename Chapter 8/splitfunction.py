abc = 'With three words'
stuff = abc.split()
print(stuff)
print(len(stuff))
print(stuff[0])

line = 'first;second;third'
thing = line.split(';')
print(thing)

fhand = open('../Chapter 7/sample.txt')
for line in fhand:
    email = list()
    dow = list()
    mon = list()
    dom = list()
    the_time = list()
    the_year = list()
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    email = words[1]
    dow = words[2]
    mon = words[3]
    dom = words[4]
    the_time = words[5]
    the_year = words[6]
    print(email)
    print(dow)
    print(mon, dom, the_year)
    print(the_time)