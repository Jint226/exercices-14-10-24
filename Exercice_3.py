# Exercice 3 : Table de Multiplication

# Demandez à l'utilisateur d'entrer un nombre entier.
# Utilisez une boucle for pour afficher la table de multiplication de ce nombre de 1 à 10.
# Demander à l'utilisateur d'entrer un nombre entier
nombre = int(input("Entrez un nombre entier : "))

# Utiliser une boucle for pour afficher la table de multiplication
print(f"Table de multiplication de {nombre} :")
for i in range(1, 11):
    # Calculer le résultat de la multiplication
    resultat = nombre * i
    # Afficher le résultat
    print(f"{nombre} x {i} = {resultat}")