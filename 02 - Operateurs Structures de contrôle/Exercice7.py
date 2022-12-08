def Date(seconde):
    """Affiche le nombre d'années, de mois, de jours, d'heures, de minutes et de secondes dans les secondes données"""
    annees = seconde // 3.154e+7
    seconde %= 3.154e+7
    mois = seconde // 2.628e+6
    seconde %= 2.628e+6
    jours = seconde // 86400
    seconde %= 86400
    heures = seconde // 3600
    seconde %= 3600
    minutes = seconde // 60
    seconde %= 60
    print(f'{int(annees)} an(s) {int(mois)} mois {int(jours)} jour(s) {int(heures)} heure(s) {int(minutes)} minute(s) {int(seconde)} seconde(s)')
