n = float(input("Número de Mols: "))
V = float(input("Volume de um gás: "))
T = float(input("Temperatura de um gás: "))

K = (T + 273.1)

R = 0.082057

P = (n*R*K) / V

print(P)