# Vous disposez d’une liste de nombres entiers quelconques,
# certains d’entre eux étant présents en plusieurs exemplaires.
# Écrivez un script qui recopie cette liste dans une autre,
# en omettant les doublons. La liste finale devra être triée. 

liste = [83, 82, 123, 1, 76, 91, 82, 16, 58, 39, 1, 6, 178, 63, 28, 12, 74, 91, 78, 28, 58, 39, 1, 78, 48, 1, 48]
listeSansDoublon = list()

for i in liste:
    stop = False
    for n in listeSansDoublon:
        if i == n:
            stop = True
            break
    if stop == True:
        continue
    listeSansDoublon.append(i)

listeSansDoublon.sort()

print(listeSansDoublon)
