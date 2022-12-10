# En vous servant des fonctions précédentes,
# écrire un programme qui trie une liste de nombres dans l’ordre décroissant.
# Dans une première solution, vous utiliserez la fonction del
# et dans une seconde la méthode remove().

listeNbr1 = [1,2,4,6,2,1,5,7,8,10,9,6]
listeNbr2 = [1,2,4,6,2,1,5,7,8,10,9,6]


def TrieurDecroissant1(liste: list):
    endListe = []
    while len(liste) > 0 :
        max = [liste[0], 0]
        for i in range(len(liste)):
            if liste[i] > max[0]:
                max = [liste[i], i]
        endListe.append(max[0])
        del liste[max[1]]
    return endListe

def TrieurDecroissant2(liste: list):
    endListe = []
    while len(liste) > 0 :
        max = liste[0]
        for i in range(len(liste)):
            if liste[i] > max:
                max = liste[i]
        endListe.append(max)
        liste.remove(max)
    return endListe

print(TrieurDecroissant1(listeNbr1))
print(TrieurDecroissant2(listeNbr2))
