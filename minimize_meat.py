from pulp import *

# Definiranje problema
prob = LpProblem("Minimalizacija_Ostataka_Mesa", LpMaximize)

# Definiranje varijabli
V = LpVariable("Kvalitetna_Salami", lowBound=0)  # Količina kvalitetne salame
N = LpVariable("Normalna_Salami", lowBound=0)  # Količina normalne salame

S = 200  # Sljunak
C = 100 # Cement
profit = 1.2 * V + N
# Definiranje ciljne funkcije (max zarada)
prob += profit, "Maximalizacija zarade"

# Definiranje ograničenja

prob+= 10*V+12*N<=S





# Rješavanje problema
prob.solve()

# Ispis rješenja
print("Status:", prob.status)

if prob.status == LpStatusOptimal:
    print("Količina kvalitetne salame (x):", 1,2*V.value() + N.value())


else:
    print("Ne postoji optimalno rješenje.")
