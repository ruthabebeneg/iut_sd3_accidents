import pandas as pd

# Lire les fichiers CSV
csv1 = pd.read_csv('data/carac.csv', sep=';', decimal='.')
csv2 = pd.read_csv('data/lieux.csv', sep=';', decimal='.')
csv3 = pd.read_csv('data/veh.csv', sep=';', decimal='.')
csv4 = pd.read_csv('data/vict.csv', sep=';', decimal='.')

# Liste des DataFrames
dfs = [csv1, csv2, csv3, csv4]

# Fusionner tous les DataFrames sur la colonne 'Num_Acc'
resultat = dfs[0]  # Initialiser avec le premier DataFrame
for df in dfs[1:]:
    resultat = pd.merge(resultat, df, on='Num_Acc', how='inner')  # Fusion progressive

# Sauvegarder le DataFrame fusionné dans un fichier CSV
resultat.to_csv('fichiers_fusionnees.csv', index=False)
