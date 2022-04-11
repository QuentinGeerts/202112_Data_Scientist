# Écrivez un algorithme demandant à l’utilisateur le nombre de joueurs (max 10 joueurs). 
# Ensuite, l’algorithme doit demander à l’utilisateur le score de chaque joueur. 
# Une fois ceci fini, il faut afficher la moyenne des scores.

MAX_PLAYERS = 10
scores = []
is_str_ok = False

# Vérification du nombre de joueurs
while not is_str_ok:
    nb_players = input("Entrez le nombre de joueurs (max. 10 joueurs) :")

    if nb_players.isdigit():
        nb_players = int(nb_players)

        if nb_players >= 0 and nb_players <= 10:
            is_str_ok = True
        else: print("Vous ne pouvez entrer un nombre entre 1 et 10.")
    else: print("Vous devez rentrer un nombre.")

i = 0

while i < nb_players:
    # Vérification du score
    is_str_ok = False
    while not is_str_ok:
        # string interpolation
        score = input(f"Entrez la note pour le joueur n° {i + 1} : ")

        if not score.isalpha():
            is_str_ok = True
        else:
            print("Vous ne pouvez pas entrer de caractères alphanumérique.")
    scores.append(float(score))

    i += 1

# Calcul de la somme des scores (pour la moyenne)
sum = 0
for score in scores:
    sum += score

# Calcul de la moyenne
avg = sum / nb_players

print(f"La moyenne des joueurs est de {avg}.")