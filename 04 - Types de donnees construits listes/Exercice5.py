# Ecrire un programme Python permettant de :

# a) Définir une liste nommée listeNombres contenant les nombres : 45, 17 , 89, 38, 10 et 74
# b) Trier et afficher la liste obtenue.
# c) Ajoutez l’élément 12 à la liste et afficher la liste.
# d) Inverser l’ordre de la liste et l’afficher.
# e) Afficher l’indice de l’élément 10.
# f) Enlever l’item 38 et afficher la liste. On suppose que l’on ne connaît pas son index.
# g) Afficher la sous-liste du 2ème au 3ème élément.
# h) Afficher la sous-liste du début au 2ème élément non compris.
# i) Afficher la sous-liste du 3ème élément à la fin de la liste.
# j) Afficher le dernier élément de deux façons un indiçage négatif. On suppose que l’on ne connaît pas son index.

# a)
listeNombres = [45, 17, 89, 38, 10, 74]
# b)
listeNombres.sort()
print(listeNombres)
# c)
listeNombres.append(12)
print(listeNombres)
# d)
listeNombres.reverse()
print(listeNombres)
# e)
print(listeNombres.index(10))
# f)
listeNombres.remove(38)
print(listeNombres)
# g)
print(listeNombres[1:3])
# h)
print(listeNombres[:2])
# i)
print(listeNombres[2:])
# j)
print(listeNombres[-1])
