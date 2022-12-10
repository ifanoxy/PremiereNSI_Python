# Ecrire un programme qui génère aléatoirement une liste de 50 nombres
# compris entre 0 et 100. Ces nombres seront stockés dans une liste
# puis une question sera posée à l’utilisateur pour trier
# puis afficher la liste soit dans l’ordre croissant,
# soit dans l’ordre décroissant.

import random

rdmListe = list()

for i in range(50):
    rdmListe.append(random.randint(0,100))

def demandeChoix():
    return input("Comment voulez vous trier cette liste ?\n1 - Ordre croissant\n2 - Ordre décroissant\n")

def TrieurCroissant(liste: list):
    endListe = []
    while len(liste) > 0 :
        min = liste[0]
        for i in range(len(liste)):
            if liste[i] < min:
                min = liste[i]
        endListe.append(min)
        liste.remove(min)
    return endListe

def TrieurDecroissant(liste: list):
    endListe = []
    while len(liste) > 0 :
        max = liste[0]
        for i in range(len(liste)):
            if liste[i] > max:
                max = liste[i]
        endListe.append(max)
        liste.remove(max)
    return endListe

response = False
while response == False:
    choix = demandeChoix()
    if choix == "1":
        response = True
        print(TrieurCroissant(rdmListe))
    elif choix == "2":
        response = True
        print(TrieurDecroissant(rdmListe))
    else:
        print("\nIl y a une erreur :\n  Votre choix n'a pas été reconnu.\n\n  Essayer de saisir un nombre entre 1 ou 2")
        response = False
