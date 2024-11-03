# Exercice 5 : Mot de Passe Correct


#  Créez une variable mot_de_passe et attribuez-lui une valeur, par exemple "python123".
#  Demandez à l'utilisateur d'entrer le mot de passe.
#  Tant que le mot de passe n'est pas correct, redemandez-le (à l'aide d'une boucle while).
#  Quand le mot de passe est correct, affichez "Accès autorisé".
# Créer une variable mot_de_passe avec une valeur
mot_de_passe = "python123"

# Demander à l'utilisateur d'entrer le mot de passe pour la première fois
saisie_utilisateur = input("Entrez le mot de passe : ")

# Utiliser une boucle while pour continuer à demander le mot de passe jusqu'à ce qu'il soit correct
while saisie_utilisateur != mot_de_passe:
    print("Mot de passe incorrect. Veuillez réessayer.")
    saisie_utilisateur = input("Entrez le mot de passe : ")

# Une fois que le mot de passe est correct
print("Accès autorisé")
