# Écrivez un script qui recopie une chaîne (dans une nouvelle variable) en l’inversant.
# Ainsi par exemple, « frivole » deviendra « elovirf ».

phrase = input('Entrez une phrase')
newPhrase = ""

for i in range(1,len(phrase)+1):
    newPhrase += phrase[len(phrase)-i]

print(newPhrase)
