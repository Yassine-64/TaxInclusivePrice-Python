
prix_HT = float(input("Veuillez entrer le prix hors taxe du produit : "))
categorie = input("Veuillez entrer la catégorie du produit (A, B, C) : ")


if categorie == 'A':
    prix_TTC = prix_HT * (1 + 7 / 100)
elif categorie == 'B':
    prix_TTC = prix_HT * (1 + 20 / 100)
elif categorie == 'C':
    prix_TTC = prix_HT * (1 + 25 / 100)

print("Le prix TTC est", prix_TTC)
