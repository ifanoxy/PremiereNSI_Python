# Ecrire une fonction qui retourne une liste de nombres croissants.
# Le minimum de cette liste, son nombre d’éléments ainsi que l’incrément seront transmis en paramètres. 

def croissant(minimum: int | float, nombreElement: int | float, increment: int | float):
    liste = list()
    for i in range(nombreElement):
        liste.append(i * increment + minimum)
    return liste

print(croissant(-7, 10, 5))
