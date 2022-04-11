# Exercice 23
# Initialisez un tableau de 10 entiers avec les 
# valeurs 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024 
# à l’aide d’une boucle. 
# Ensuite, à l’aide d’une boucle affichez la valeur 
# de chaque cellule du tableau avec l’opération Ecrire().

#  Initialisation
i = 0
array = []
MAX_VALUES = 10
value = 2

# Remplissage du tableau
while i < MAX_VALUES:
    array.append(value ** (i + 1))
    i += 1

# Affichage du tableau
i = 0
while i < MAX_VALUES:
    print(array[i], end=" ")
    i += 1
