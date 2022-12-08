# Assignez les valeurs respectives 3, 5, 7 à trois variables a, b, c. 
# Effectuez l'opération a - b/c. 
# Le résultat est-il mathématiquement correct ? 
# Si ce n'est pas le cas, comment devez-vous procéder pour qu'il le soit ?

a, b , c = 3, 5, 7
prtin(a - b/c)

# Ce résultat n’est pas correct mathématiquement car il faut le garder sous forme fractionnaire !

from fractions import * 
a, b, c = 3, 5, 7
print(a - Fraction(b/c))
