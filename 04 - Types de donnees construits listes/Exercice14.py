# Soit la liste suivante : 
# ['Jean-Michel’, ’Marc’, ’Vanessa’, ’Anne’, ’Maximilien’, ’Alexandre-Benoît’, ’Louise’]
# Écrivez un script qui affiche chacun de ces noms avec le nombre de caractères correspondant. 

liste = ['Jean-Michel', 'Marc', 'Vanessa', 'Anne', 'Maximilien', 'Alexandre-Benoît', 'Louise']
for i in liste:
    print(f'{i} contient {len(i)} caractères')
