#Número de mols 
n = float(input("numero de mols: "))

#Volume de um gás
V = float(input("volume de um gas: "))

#Temperatura em Celsius
C = float(input("temperatura: "))

#Temperatura pra Kelvin
T = C + 273.1

#Constante Universal dos gases
R = 0.082057

#Equação de Clayperon
p = (n * R * T) / V
print(p)