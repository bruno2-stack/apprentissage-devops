print("=== MA PREMIÈRE CALCULATRICE ===")

a = float(input("Entrez le premier nombre : "))
b = float(input("Entrez le deuxième nombre : "))

somme = a + b
difference = a - b
produit = a * b

print("Somme :", somme)
print("Différence :", difference)
print("Produit :", produit)

if b != 0:
    print("Quotient :", a / b)
else:
    print("Division impossible : le deuxième nombre est nul.")