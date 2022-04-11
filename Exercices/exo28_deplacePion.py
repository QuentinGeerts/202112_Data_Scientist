# exo27
# Réalisez un algorithme nous permettant de déplacer un pion dans un 
# tableau de 10 éléments. Au début, le pion se trouve dans la première
# case du tableau. Nous pouvons ensuite le déplacer par la gauche (g), 
# par la droite (d) ou de stopper l'algorithme (q) (Indice : l'exo doit 
# être exécuté dans la console Windows). 

import msvcrt
import os

tab = [' '] * 10
indice = 0
tab[indice] = "X"

print(tab)

key = msvcrt.getch()
char = key.decode("ascii")

while char != "w":
    os.system('cls')
    # Gauche
    if char == "q":
        if indice > 0:
            tab[indice] = " "
            indice -= 1
            tab[indice] = "X"
        else:
            print("Vous ne pouvez pas aller plus loin.")
        
    # Droite
    if char == "d":
        if indice < len(tab) - 1:
            tab[indice] = " "
            indice += 1
            tab[indice] = "X"
        else:
            print("Vous ne pouvez pas aller plus loin.")

    
    print(tab)
    key = msvcrt.getch()
    char = key.decode("ascii")


