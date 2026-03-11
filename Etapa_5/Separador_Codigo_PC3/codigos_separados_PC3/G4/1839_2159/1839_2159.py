# Grandezas
p = float(input("Digite a pressão (em atm): "))
n = int(input("Digite o número de mols: "))
C = float(input("Digite a temperatura (em C): "))

# Dados
R = 0.082
T = C + 273.15

# Equação para volume
V = (n*R*T)/p

print(V)