# Ecrire une procédure nommée inverse qui reçoit
# une liste en paramètres et 2 indices (2 entiers)
# et qui inverse les deux nombres de la liste qui correspondent aux indices transmis.

def inverse(liste: list, indice1: int, indice2: int):
    """
    Affiche une liste qui a inversé deux nombres de la liste entrée qui correspondent aux indices transmis.
    """
    liste[indice1], liste[indice2] = liste[indice2], liste[indice1]
    print(liste)

inverse([1,2,3,4,5,6,7,8,9], 2,7)
