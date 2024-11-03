# Exercice 8 : Calculer la Factorielle


#  Demandez à l'utilisateur d'entrer un nombre entier positif.
#  Utilisez une boucle while ou for pour calculer la factorielle de ce nombre.
#  Affichez le résultat.
# Demander à l'utilisateur d'entrer un nombre entier positif
n = int(input("Entrez un nombre entier positif : "))

# Initialiser la variable pour la factorielle
factorielle = 1

# Utiliser une boucle for pour calculer la factorielle
for i in range(1, n + 1):
    factorielle *= i  # Multiplier la variable factorielle par chaque nombre de 1 à n

# Afficher le résultat
print(f"La factorielle de {n} est : {factorielle}")