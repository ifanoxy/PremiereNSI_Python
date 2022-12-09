# Soient les listes suivantes : 
# t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
# t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']

# Écrivez un programme qui crée une nouvelle liste t3. 
# Celle-ci devra contenir tous les éléments des deux listes en les alternant,
# de telle manière que chaque nom de mois soit suivi du nombre de jours correspondant : 
# ['Janvier',31,'Février',28,'Mars',31, ...].

t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
t3 = list()
i = 0

maxlen = [len(t1), len(t2)]
maxlen.sort()

while i < maxlen[-1]:
    t3.append(t2[i])
    t3.append(t1[i])
    i+=1

print(t3)
