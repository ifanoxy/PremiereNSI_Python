# Écrivez un script qui recherche le mot le plus long dans une phrase donnée
# (l’utilisateur du programme doit pouvoir entrer une phrase de son choix). 

phrase = input('Entrez la phrase de votre choix : ')
plusGrandMot = [""]

for mot in phrase.split():
    if len(mot) > len(plusGrandMot[0]):
        plusGrandMot = [mot]
        continue
    if len(mot) == len(plusGrandMot[0]):
        plusGrandMot.append(mot)

print(f'Le(s) mot(s) le(s) plus long sont : {", ".join(plusGrandMot)}')
