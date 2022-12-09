# Écrivez un script qui compte le nombre d’occurrences du caractère « a » dans une chaîne.

phrase = input("Entre une chaine de caractère")
count = 0

for lettre in phrase:
    if lettre.lower() == "a":
        count += 1

if(count == 0):
    print('La chaine de caractère ne contient pas le caractère "a"')
else:
    print(f'La chaine de caractère contient {count}x le caractère "a"')
