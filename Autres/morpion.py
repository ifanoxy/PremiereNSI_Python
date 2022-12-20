plateau = ["   ","   ","   ","   ","   ","   ","   ","   ","   "]
winer = "personne"
end = False
i = 0

print(f"{'|'.join(plateau[0:3])}\n---|---|---\n{'|'.join(plateau[3:6])}\n---|---|---\n{'|'.join(plateau[6:9])}")


while end == False:
	validReponse = False
	if i%2 :
		while validReponse == False:
			play = input("Les croix c'est à vous de jouer, entrez un nombre de 1 à 9 : ")
			try:
				play = int(play)
			except ValueError:
				print('Entrez un nombre !')
				continue
			if 0 <= play <= 9 and plateau[play-1] == "   ":
				validReponse == True
				break
			else :
				print("Réponse invalide !")
		player = " X "
	else :
		while validReponse == False:
			play = input("Les ronds c'est à vous de jouer, entrez un nombre de 1 à 9 : ")
			try:
				play = int(play)
			except ValueError:
				print('Entrez un nombre !')
				continue
			if 0 <= play <= 9 and plateau[play-1] == "   ":
				validReponse == True
				break
			else :
				print("Réponse invalide !")
		player = " O "
	
	plateau[play-1] = player

	for n in range(1,8,3):
		if plateau[n] == "   ":
			continue
		if plateau[n-1] == plateau[n] and plateau[n+1] == plateau[n]:
			end = True
			winer = plateau[n]
			break
	for n in range(3,6,1):
		if plateau[n] == "   ":
			continue
		if plateau[n-3] == plateau[n] and plateau[n+3] == plateau[n]:
			end = True
			winer = plateau[n]
			break
	if plateau[4] == plateau[0] and plateau[4] == plateau[8] and plateau[4] !=  "   " or plateau[4] == plateau[2] and plateau[4] == plateau[6] and plateau[4] != "   ":
		end = True
		winer = plateau[4]

	print(f"{'|'.join(plateau[0:3])}\n---|---|---\n{'|'.join(plateau[3:6])}\n---|---|---\n{'|'.join(plateau[6:9])}")
	i += 1

if winer == "personne":
	print("Personne n'a gagné, c'est une égalité")
elif winer == " O ":
	print("Les ronds ont gagnés bien joué")
else:
	print("Les croix ont gagnées bien joué")
