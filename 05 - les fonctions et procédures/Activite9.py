# Ecrire une fonction indice_maximum qui reçoit une liste en paramètre
# et qui retourne l’indice de la plus grande valeur de la liste. 
# Vous résoudrez ce problème avec la méthode index() puis sans.

listeNbr = [1,2,4,6,2,1,5,7,8,10,9,6]

def indice_maximum1(liste: list):
    max =  liste[0]
    for nbr in liste:
        if nbr > max:
            max = nbr
    return liste.index(max)

def indice_maximum2(liste: list):
    max = [liste[0], 0]
    for i in range(len(liste)):
        if liste[i] > max[0]:
            max = [liste[i], i]
    return max[1]

print(indice_maximum1(listeNbr))
print(indice_maximum2(listeNbr))
