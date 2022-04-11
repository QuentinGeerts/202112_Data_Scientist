array = [3, 6, 9, 2, 5, 8, 1, 4, 7]

#region for avec une élément itérable
print("Structure", end=" : ")
for digit in array:
    print(digit, end=" ")
#endregion

print("")

#region range avec un paramètre
print("Range avec un paramètre", end=" : \n")
for iterator in range(len(array)):
    print(iterator, end=" : ")
    print(array[iterator])
#endregion
print("")

#region range avec deux paramètres
print("Range avec 2 paramètres", end=" : \n")
for iterator in range(3, len(array)):
    print(iterator, end=" : ")
    print(array[iterator])
#endregion
print("")

#region range avec trois paramètres
print("Range avec 3 paramètres", end=" : \n")
for iterator in range(3, len(array), 2):
    print(iterator, end=" : ")
    print(array[iterator])
#endregion
print("")

#region enumerate
print("Enumerate", end=" : \n")
for iterator, value in enumerate(array):
    print(iterator, end=" : ")
    print(value)
    print(array[iterator])
#endregion

print("")

for letter in "Bonjour":
    if letter == "o": 
        print(letter, end="")
    else:
        print(' - ', end="")