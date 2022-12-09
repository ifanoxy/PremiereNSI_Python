# Ecrivez un programme qui calcule les 50 premiers termes de la table de multiplication par 13,
# mais n'affiche que ceux qui sont des multiples de 7.

i = 0
while i < 50:
  i += 1
  if i * 13 % 7 == 0:
    print(f'{i} x 13 = {i*13}')
