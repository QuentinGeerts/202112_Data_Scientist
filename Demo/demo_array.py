tab = ["a", "b", 1, 2, 3, "abc"]
#       0    1   2  3  4    5

# print(tab)
# print(tab[6])
# print(tab[-3])
# print(tab[2:5])
# print(tab[2:])
# print(tab[:2])
# print(tab[:]) # ['a', 'b', 1, 2, 3, 'abc']
# Une lecture avant et une lecture après (maximum)
# Si on dépasse : list index out of range
# index_start : index_end (non compris) : pas
# print(tab[::-1]) # ['abc', 3, 2, 1, 'b', 'a']

# Initialisation
i = 0

# Condition
while i < len(tab):
    print(tab[i], end="")
    if (i != len(tab)-1): print(end=", ")

    # Incrémentation / Modification
    # A ne pas oublier sinon boucle infinie
    i = i + 1
    # i += 1

tab.append(int(input("")))