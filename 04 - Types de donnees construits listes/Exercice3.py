# Ecrivez un programme Python qui :
# Demande à l’utilisateur son nom et son prénom, séparés par un espace (ils peuvent être écrits en minuscules)
# Affiche « Votre prénom est : » suivi du prénom avec la 1ère lettre en majuscule
# Affiche « Votre nom est : » suivi du nom avec la 1ère lettre en majuscule
# Affiche « Vos initiales sont : » suivi des initiales du nom et du prénom en majuscules
# Vous utiliserez la méthode split() sur la chaîne de caractères saisie par l’utilisateur pour la séparer en 2 chaînes appelées respectivement nom et prenom.

FullName = input('Entrez votre prénom puis votre nom séparer par une virgule et un espace : ')

Prenom = FullName.split(', ')[0]
Nom = FullName.split(', ')[1]

print(f'Votre prénom est : {Prenom[0].upper()+Prenom[1:]}')
print(f'Votre nom est : {Nom[0].upper()+Nom[1:]}')
print(f'Vos initiales sont : {Prenom[0].upper() + Nom[0].upper()}')
