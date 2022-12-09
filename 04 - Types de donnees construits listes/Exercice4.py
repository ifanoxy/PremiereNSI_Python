# Ecrivez un programme qui stocke dans une liste appelée « results » 
# les différentes valeurs de A avec A = n² + 5 et n allant de 0 à 1000. 
# Vous ferez afficher la liste.

results = list()

for n in range(1000):
    results.append(n**2+5)

print(results)
