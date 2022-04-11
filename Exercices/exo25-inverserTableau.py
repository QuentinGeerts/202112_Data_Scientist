# Exercice 25
# Inversez un tableau : soit un tableau T. Saisissez ce tableau. Changez de
# place les éléments de ce tableau de façon à ce que le nouveau tableau soit une
# sorte de miroir de l'ancien et affichez le nouveau tableau.

array = [3, 1, 2, 4, 5]
print(array)

# Première façon
array_reversed1 = array[::-1]
print(array_reversed1)

# Deuxième façon
array_reversed2 = array[:]
array_reversed2.reverse() # Modifie directement le tableau
print(array_reversed2)

# Troisième façon
array_reversed3 = []
i = len(array) - 1
while i >= 0:
    array_reversed3.append(array[i])
    i -= 1
print(array_reversed3)

# Quatrième façon
array_reversed4 = []
i = 0
while i < len(array):
    array_reversed4.append(array[len(array) - 1 - i])
    i += 1
print(array_reversed4)