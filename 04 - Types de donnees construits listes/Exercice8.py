# Écrivez un programme qui recherche le plus grand élément présent dans une liste donnée. 
# Par exemple, si on l’appliquait à la liste [32, 5, 12, 8, 3, 75, 2, 15],
# ce programme devrait afficher : le plus grand élément de cette liste a la valeur 75. 

list = [32, 5, 12, 8, 3, 75, 2, 15]
list.sort()
print(f'le plus grand élément de cette liste est {list[-1]}')
