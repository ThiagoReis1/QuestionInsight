p = float(input("valor da pressao: "))
n = float(input("valor do numero de mols: "))
T = float(input("valor da temperatura: "))
V = float(input("valor do volume: "))
R = float(input(0.082))

V = (n * R * (T + 273,15))/p
print(V)