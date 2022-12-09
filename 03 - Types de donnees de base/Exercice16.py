# En partant de l’exercice précédent,
#  écrivez un script qui détermine si une chaîne de caractères donnée est un palindrome 
# (c’est-à-dire une chaîne qui peut se lire indifféremment dans les deux sens), 
# comme par exemple « radar » ou « s.o.s ».

phrase = input('Entrez une phrase : ')
newPhrase = ""

for i in range(len(phrase)):
    i += 1
    newPhrase += phrase[len(phrase)-i]

if newPhrase == phrase:
    print(f'"{phrase}" est un palindrome')
else: 
    print(newPhrase)
