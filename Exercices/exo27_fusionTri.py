# Exercice 26
# En considérant deux tableaux d'entiers (non triés), 
# réalisez un algorithme qui place tous les éléments des deux 
# tableaux dans un troisième. Ce dernier doit être trié une fois 
# l'algorithme terminé. Notez que le tri doit être fait en même 
# temps que la fusion des deux tableaux et pas après.

array1 = [9, 4, 6, 1, 8]
array2 = [7, 0, 2, 5, 3]
array3 = []
# [9]
# [4, 9]
# [4, 6, 9]
# [1, 4, 6, 9]
# [1, 4, 6, 8, 9]

i = 0
while i < len(array1):
    save_index = 0
    for index, element in enumerate(array3):
        if array1[i] > element:
            save_index = index + 1
        else: break
    
    array3.insert(save_index, array1[i])
    i += 1

i = 0
while i < len(array2):
    save_index = 0
    for index, element in enumerate(array3):
        if array2[i] > element:
            save_index = index + 1
        else: break
    
    array3.insert(save_index, array2[i])
    i += 1


# PAS ACCEPTABLE POUR L'ÉNONCÉ
# # Modifie directement le tableau 3
# array3.sort() 

# # sorted va te renvoyer un tableau trié des deux tableaux fusionné en paramètre
# array3 = sorted(array1 + array2) 

print(array3) # tableau trié
