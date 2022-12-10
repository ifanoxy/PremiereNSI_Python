# Ecrire une fonction moyenne qui reçoit une liste de nombres en paramètre
# et qui retourne la moyenne puis tester son fonctionnement par l’affichage de cette valeur.

# Vous donnerez une première solution utilisant une boucle for_ in range_,
# puis une seconde utilisant une boucle for_in_.

def moyenne1(listNombre: list):
    """
    Retourne la moyenne d'une liste de nombre
    """
    somme = 0
    for i in range(len(listNombre)):
        somme += listNombre[i]
    
    return somme/len(listNombre)

def moyenne2(listNombre: list):
    """
    Retourne la moyenne d'une liste de nombre
    """
    somme = 0
    for nbr in listNombre:
        somme += nbr
    
    return somme/len(listNombre)


liste = [12,23,8,12,3]

print(moyenne1(liste))
print(moyenne2(liste))
