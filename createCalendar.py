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
