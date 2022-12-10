# Ecrire une fonction maximum qui reçoit une 
# liste d’entiers relatifs en paramètre et qui retourne la plus grande valeur celle-ci.

def maximum(listeInt: list):
    max = listeInt[0]
    for int in listeInt:
        if(int > max):
            max = int
    return max
