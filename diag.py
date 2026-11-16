#pb de séparateur donc je teste si je peux changer tout ça et remettre les bons séparateurs
#à uncomment si pb de séparateur

"""with open("data/11201.csv", encoding="utf-8", errors="replace") as f:
    lignes = f.readlines()  # liste de toutes les lignes du fichier

# 1. Nombre total de lignes du fichier
print("Nombre total de lignes :", len(lignes))

# 2. Les 5 premières lignes, telles quelles (repr montre les caractères cachés comme \t ou \n)
print("\n--- En-tête et premières lignes ---")
for ligne in lignes[:5]:
    print(repr(ligne))

# 3. Compter les ";" et les "," dans l'en-tête : cela révèle le vrai séparateur
print("\nEn-tête : nb de ';' =", lignes[0].count(";"), "| nb de ',' =", lignes[0].count(","))

# 4. Les lignes autour de la ligne 1749.
#    Attention : Python compte à partir de 0, donc la ligne 1749 correspond à l'index 1748.
print("\n--- Lignes 1745 à 1752 ---")
for i in range(1744, min(1752, len(lignes))):  # on évite de dépasser la fin du fichier
    ligne = lignes[i]
    # On affiche le numéro réel (i + 1), le contenu, et le nombre de séparateurs
    print(f"Ligne {i + 1} | ';' = {ligne.count(';')} | ',' = {ligne.count(',')} | {ligne.strip()}")

# 5. Les dernières lignes : vérifier s'il y a une note de bas de fichier
print("\n--- 3 dernières lignes ---")
for ligne in lignes[-3:]:
    print(repr(ligne))"""""