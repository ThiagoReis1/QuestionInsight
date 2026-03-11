n = float(input("digite o valor do numero de mols: "))
V = float(input("digite o valor do volume: "))
T = float(input("digite o valor da temperatura: "))
T_F = float(T + 273.1)
R = 0.082057
p = float((n*R*T_F)/V)

print(p)


