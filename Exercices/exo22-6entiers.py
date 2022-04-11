# Exercice 22
# Écrivez un algorithme qui saisit 6 entiers 
# et les stocke dans un tableau, puis affiche 
# le contenu de ce tableau une fois qu’il est rempli.

array = []

# Déclaration + initialisation
i = 0

# Condition
while i < 6:
    array.append(int(input("Entrez un nombre entier : ")))

    # Incrémentation
    i += 1

print(array)

i = 0
while i < 6:
    print(array[i], end=" ")
    i += 1
