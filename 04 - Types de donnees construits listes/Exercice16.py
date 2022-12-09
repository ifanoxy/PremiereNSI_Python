# Écrivez un script qui recherche le mot le plus long dans une phrase donnée
# (l’utilisateur du programme doit pouvoir entrer une phrase de son choix). 

phrase = input('Entrez la phrase de votre choix : ')

mots = phrase.split()
plusGrandMot = [0]

for mot in mots:
    if len(mot) > plusGrandMot[0]:
        plusGrandMot = [len(mot), mot]

print(plusGrandMot[1])
