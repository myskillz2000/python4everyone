def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

greet(input('What language do you speak?'))

""" Multiple Parameters """

def addtwo(a, b):
    added = a + b
    return added

x = addtwo(3, 5)
print(x)