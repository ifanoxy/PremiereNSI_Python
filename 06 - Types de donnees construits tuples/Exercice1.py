# Ecrire la fonction triangle_rectangle
# permettant lorsqu’on lui entre en paramètres un triplet de type n-upplet <
# contenant en items, la longueur au carré de chacun des côtés d’un triangle,
# d’afficher si ce dernier est rectangle ou non.

def triangle_rectangle(longueur: tuple):
    for i in range(3):
        if longueur[i] == longueur[i-1] + longueur[i-2]:
            return print("C'est un triangle rectangle")
    return print("Ce n'est pas un triangle rectangle")

triangle_rectangle((50,60,10))
