#  Écrivez un programme qui analyse un par un tous les éléments d’une liste de mots
#  (par exemple : ['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean-Pierre', 'Sandra'])
#  pour générer deux nouvelles listes. L’une contiendra les mots comportant moins de 6 caractères,
#  l’autre les mots comportant 6 caractères ou davantage.

liste = ['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean-Pierre', 'Sandra']
shortName = list()
longName = list()

for name in liste:
    if len(name) < 6:
        shortName.append(name)
    else:
        longName.append(name)

print(f'Noms court : {shortName}')
print(f'Noms longs : {longName}')
