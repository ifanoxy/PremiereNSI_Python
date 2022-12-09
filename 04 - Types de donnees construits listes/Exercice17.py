# Écrivez un script capable d’afficher la liste de tous les jours d’une année imaginaire,
# laquelle commencerait un jeudi. Votre script utilisera lui-même trois listes :
# une liste des noms de jours de la semaine,
# une liste des noms des mois,
# et une liste des nombres de jours que comportent chacun des mois (ne pas tenir compte des années bissextiles).
#  Exemple de sortie : jeudi 1 janvier   vendredi 2 janvier   samedi 3 janvier   dimanche 4 janvier ... et ainsi de suite, jusqu’au jeudi 31 décembre. 


jours = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
mois = {'janvier': 31, 'février': 28, 'mars': 31, 'avril': 30, 'mai': 31, 'juin': 30, 'juillet': 31, 'aout': 31, 'septembre': 30, 'octobre': 31, 'novembre': 30, 'décembre': 31}

i = 3
for m in mois:
    for nbr in range(mois[m]):
        nbr +=1
        print(f"{f'{jours[i]}' :<10}{f'{nbr}' :>3}{f'{m}' :>12}")
        if(i >= 6):
            i = 0
        else:
            i += 1
