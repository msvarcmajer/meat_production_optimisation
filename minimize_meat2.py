from pulp import *

# Stvaranje problem objekta
problem = LpProblem("Minimiziranje ostatka mesa", LpMinimize)

# Varijable
g = LpVariable("govedina", lowBound=0)
s = LpVariable("svinjetina", lowBound=0)
x = LpVariable("kvalitetna_salamica", lowBound=0)
y = LpVariable("normalna_salamica", lowBound=0)
G = 100
S = 200

# Funkcija cilja
problem += (G-g) + (S-s), "Minimizirani ostatak mesa"

# Ograničenja
problem += 0.1*g + 0.4*s == y, "Kolicina_normalne_salamice"
problem += 0.8*g + 0.2*s == x, "Kolicina_kvalitetne_salamice"

problem += g <= G, "Dostupna_kolicina_govedine"
problem += s <= G, "Dostupna_kolicina_svinjetine"
problem += x>=0
problem += y>=0
problem += g>=0
problem += s>=0

# Rješavanje problema
problem.solve()

# Ispis rezultata
print("Status:", LpStatus[problem.status])
print("Minimizirani ostatak mesa:", value(problem.objective))
print("Količina kvalitetne salame:", value(x))
print("Količina normalne salame:", value(y))
print("---------------")
print("Količina govedine:", value(g))
print("Količina svinjetine:", value(s))
print("Ostatak govedine", G-value(g) )
print("Ostatak svinjetine", S-value(s))