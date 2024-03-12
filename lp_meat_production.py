from pulp import *

# Definiranje problema
prob = LpProblem("Maksimizacija_Profita_Mesara", LpMaximize)

# Definiranje varijabli

x = LpVariable("Premium_Salama", lowBound=0)
y = LpVariable("Normalna_Salama", lowBound=0)
z = LpVariable("Jeftina_Salama", lowBound=0)


S = 600  # Dostupna količina svinjetine u kilogramima
G = 100  # Dostupna količina govedine u kilogramima
U = 0.2  # Minimalni udio premium salame (raspon 0-1)

Cijena_govedine = 5
Cijena_svinjetine = 3
Marza = 1 #Raspon marze je 0-1

Prodajna_cijena_premium_salame = (0.8*Cijena_govedine + 0.2*Cijena_svinjetine)+(0.8*Cijena_govedine + 0.2*Cijena_svinjetine)*Marza
Prodajna_cijena_normalne_salame = (0.4*Cijena_govedine + 0.6*Cijena_svinjetine)+(0.4*Cijena_govedine + 0.6*Cijena_svinjetine)*Marza
Prodajna_cijena_jeftine_salame = (0.1*Cijena_govedine + 0.9*Cijena_svinjetine)+(0.1*Cijena_govedine + 0.9*Cijena_svinjetine)*Marza
Profit= (Prodajna_cijena_premium_salame * x + Prodajna_cijena_normalne_salame * y + Prodajna_cijena_jeftine_salame * z) - (S*Cijena_svinjetine + G*Cijena_govedine)

x = LpVariable("Premium_Salama", lowBound=0)
y = LpVariable("Normalna_Salama", lowBound=0)
z = LpVariable("Jeftina_Salama", lowBound=0)

# Definiranje ciljne funkcije
prob += Profit , "Profit"

# Definiranje ograničenja
prob += 0.8 * x + 0.4 * y + 0.1 * z <= G, "Potrosena govedina"
prob += 0.2 * x + 0.6 * y + 0.9 * z <= S, "Potrosena svinjetina"
prob += x >= 0, "Nenegativna količina premium salame"
prob += y >= 0, "Nenegativna količina normalne salame"
prob += z >= 0, "Nenegativna količina jeftine salame"
prob += x >= U * (x + y + z), "Uvjetovani_Udio_Premium_Salame"

# Rješavanje problema
prob.solve()

# Ispis rezultata
print("Status:", prob.status)

if prob.status == LpStatusOptimal:
    print("Količina premium salame:", x.value())
    print("Količina normalne salame:", y.value())
    print("Količina jeftine salame:", z.value())
    print("Profit:", Profit.value())

else:
    print("Ne postoji optimalno rješenje.")