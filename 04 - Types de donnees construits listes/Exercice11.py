# Écrivez un programme qui génère la liste des carrés et des cubes des nombres de 20 à 40.

carres = list()
cubes = list()
for i in range(20, 40):
    carres.append(i**2)
    cubes.append(i**3)

print(f'liste des carrées de 20 à 40 : {carres}')
print(f'liste des cubes de 20 à 40 : {cubes}')
