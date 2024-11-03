# Exercice 1 : Compter les Voyelles

# Demandez à l'utilisateur d'entrer une phrase.
# Utilisez une boucle for pour parcourir chaque caractère de la phrase
# et comptez le nombre de voyelles (a, e, i, o, u).
# Affichez le nombre total de voyelles trouvées.
# Demander à l'utilisateur d'entrer une phrase
phrase = input("Entrez une phrase : ")

# Initialiser un compteur de voyelles
nombre_de_voyelles = 0

# Définir les voyelles que nous cherchons (en minuscules et majuscules)
voyelles = "aeiouAEIOU"

# Parcourir chaque caractère de la phrase
for caractere in phrase:
    # Vérifier si le caractère est une voyelle
    if caractere in voyelles:
        # Incrémenter le compteur si c'est une voyelle
        nombre_de_voyelles += 1

# Afficher le nombre total de voyelles trouvées
print("Nombre total de voyelles :", nombre_de_voyelles)