# Ecrivez un programme qui affiche les 20 premiers termes de la table de multiplication par 7, 
# en signalant au passage (à l'aide d’un astérisque) ceux qui sont des multiples de 3.
# Exemple : 7 14 21 * 28 35 42 * 49

i = 0
while i < 20:
  i += 1
  if i*7%3 == 0:
    print(f'{i} x 7 = {i*7}')
  else:
    print(f'{i} x 7 = {i*7}*')
