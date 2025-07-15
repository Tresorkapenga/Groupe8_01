#Entréé utilisateur
heures = int(input("Nombre d'heures : "))
munites = int(input("Nombre de minutes : "))
secondes = int(input("Nombre de secondes : "))

#Conversion
total_secondes = heures * 3600 + munites * 60 + secondes
#résultat
print(f"Durée total : {total_secondes} secondes.")