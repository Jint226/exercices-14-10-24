# Exercice 4 : Somme des Entiers


#  Demandez à l'utilisateur d'entrer un nombre entier positif n.
#  Utilisez une boucle for pour calculer la somme des nombres de 1 à n.
#  Affichez la somme totale.
# Demander à l'utilisateur d'entrer un nombre entier positif
n = int(input("Entrez un nombre entier positif : "))

# Initialiser la somme à 0
somme = 0

# Utiliser une boucle for pour calculer la somme des nombres de 1 à n
for i in range(1, n + 1):
    somme += i  # Ajouter i à la somme à chaque itération

# Afficher la somme totale
print(f"La somme des nombres de 1 à {n} est : {somme}")