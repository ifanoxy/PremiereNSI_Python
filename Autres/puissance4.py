end = False
jeu = ["⬛️"]*42
winer = "personne"

def afficherJeu(jeu):
    jeuAfficher = ""
    for c in range(6):
        jeuAfficher += "".join(jeu[7*c:c*7+7]) + "\n"
    return jeuAfficher

def checkWin(jeu, position, player):
    win = False
    for condition in range(4):
        wincount = 0
        for i in range(1,4):
            match condition:
                case 0:
                    top = position-i*7
                    if top >= 0 and jeu[top] == player:
                        wincount +=1
                    bottom = position+i*7
                    if bottom <= 41 and jeu[bottom] == player:
                        wincount +=1
                case 1:
                    left = position-i
                    if int(left/7) == int(position/7) and jeu[left] == player:
                        wincount +=1
                    right = position+i
                    if int(right/7) == int(position/7) and jeu[right] == player:
                        wincount +=1
                case 2:
                    top = position-i*7
                    left = position-i
                    if top >= 0 and int(left/7) == int(position/7) and jeu[top-i] == player:
                        wincount +=1
                    bottom = position+i*7
                    right = position+i
                    if bottom <= 41 and int(right/7) == int(position/7) and jeu[bottom+i] == player:
                        wincount +=1
                case 3:
                    top = position-i*7
                    right = position+i
                    if  top >= 0 and int(right/7) == int(position/7) and jeu[top+i] == player:
                        wincount +=1
                    bottom = position+i*7
                    left = position-i
                    if bottom <= 41 and int(left/7) == int(position/7) and jeu[bottom-i] == player:
                        wincount +=1
        if wincount == 3:
            win = True
            break
    return win

print(afficherJeu(jeu))
for i in range(42):
    valideReponse = False
    while valideReponse == False:
        if i%2:
            play = input("Les 🔴 c'est à vous de jouer, entrez un nombre de 1 à 7 : ")
            player = "🔴"
        else: 
            play = input("Les 🟡 c'est à vous de jouer, entrez un nombre de 1 à 7 : ")
            player = "🟡"
        try:
            play = int(play)
        except ValueError:
            print('Entrez un nombre !')
            continue
        if 0 <= play <= 7 and jeu[play-1] == "⬛️":
            validReponse == True
            break
        else :
            print("Réponse invalide !")

    for n in range(6):
        if jeu[play-1+7*n] == "⬛️" and play+7*n < 36:
            continue
        elif jeu[play-1+7*n] != "⬛️":
            jeu[play-1+7*(n-1)] = player
            position = play-1+7*(n-1)
            break
        jeu[play-1+7*n] = player
        position = play-1+7*n

    print(afficherJeu(jeu))
    end = checkWin(jeu, position, player)
    if end:
        winer = player
        break

if winer == "personne":
    print("Il y a une égalitée parfaite !")
else:
    print(f"Bravo les {winer} vous venez de gagner !")
