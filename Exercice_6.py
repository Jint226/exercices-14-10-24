 # Exercice 6 : Trouver le Maximum

#  Demandez à l'utilisateur d'entrer une liste de nombres séparés par des espaces.
#  Convertissez cette saisie en une liste d'entiers (utilisez .split() et map(int, ...)).
#  Utilisez une boucle for pour trouver le nombre maximum dans la liste, sans utiliser la fonction max().
#  Affichez le plus grand nombre.
# Demander à l'utilisateur d'entrer une liste de nombres séparés par des espaces
saisie = input("Entrez une liste de nombres séparés par des espaces : ")

# Convertir la saisie en une liste d'entiers
liste_nombres = list(map(int, saisie.split()))

# Initialiser la variable du nombre maximum avec le premier élément de la liste
max_nombre = liste_nombres[0]

# Utiliser une boucle for pour parcourir la liste et trouver le nombre maximum
for nombre in liste_nombres:
    if nombre > max_nombre:
        max_nombre = nombre

# Afficher le plus grand nombre
print("Le plus grand nombre est :", max_nombre)