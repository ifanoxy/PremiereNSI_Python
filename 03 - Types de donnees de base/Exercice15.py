# Écrivez un script qui recopie une chaîne (dans une nouvelle variable) en l’inversant.
# Ainsi par exemple, « frivole » deviendra « elovirf ».

phrase = "aeeyui"
newPhrase = ""

for i in range(len(phrase)):
    i += 1
    newPhrase += phrase[len(phrase)-i]

print(newPhrase)
