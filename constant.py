# Chances de toucher l'adversaire (1=100%)
HIT_CHANCE = 0.9

# Déclaration des types

# Déclaration du nom du Type
TYPES_NAME_ARRAY = ["Eau", "Feu", "Plante", "Normal", "Foudre"]

# Déclaration des caractéristiques du type ([PV,Attaque,Defense])
TYPES_CARACTERISTICS_ARRAY = [[200, 40, 10], [200, 40, 10], [200, 40, 10], [200, 56, 0], [200, 40, 10]]

# Tableau d'affinité
AFFINITY_ARRAY = [
                  [1, 2, 0.5, 1, 0.5, 2, 1],          # 0=Eau
                  [0.5, 1, 2, 1, 1, 1],               # 1=Feu
                  [2, 0.5, 1, 1, 1, 2],               # 2=Plante
                  [0.75, 0.75, 0.75, 1, 0.75, 0.75],  # 3=Normal
                  [2, 1, 1, 1, 1, 0],                 # 4=Foudre
                  [1, 1, 0.5, 1, 2, 1]                # 5=Sol
                 ]
