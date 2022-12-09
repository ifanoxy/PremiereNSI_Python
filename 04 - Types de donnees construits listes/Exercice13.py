# Écrivez un programme qui permette d’obtenir à l’écran 
# les 15 premiers termes des tables de multiplication par 2, 3, 5, 7, 11, 13, 17, 19 
# (ces nombres seront placés au départ dans une liste)
# sous la forme d’une table similaire à la suivante :  2   4   6   8  10  12  14  16  18  20  22  24  26  28  30  3   6   9  12  15  18  21  24  27  30  33  36  39  42  45  5  10  15  20  25  30  35  40  45  50  55  60  65  70  75    etc. 

tablesMultis = [2,3,5,7,11,13,17,19]

for multi in tablesMultis:
    for i in range(1,16):
        print(i*multi, end=" ")
    print('|', end=" ")
