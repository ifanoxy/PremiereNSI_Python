# Écrivez un programme qui crée automatiquement la liste des sinus des angles de 0° à 90°, par pas de 5°.
# Attention : la fonction sin() du module math considère que les angles sont fournis en radians (360° = 2 π radians). 
import math

sinAngles = list()

for i in range(0, 90, 5):
    sinAngles.append(math.sin(math.radians(i)))

print(sinAngles)
