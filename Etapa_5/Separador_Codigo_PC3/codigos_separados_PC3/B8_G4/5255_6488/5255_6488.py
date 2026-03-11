p = float(input("Digite o peso do produto (kg): "))
d = float(input("Digite a distancia entre o ponto de origem e o destino (km): "))
c = int(input("Codigo do estado de destino: "))

# p = peso
# d = distancia
# c = CEP

if (c == 1):
	icms = 17
elif (c == 2):
	icms = 17.5
elif (c == 3):
	icms = 18
elif (c == 4):
	icms = 20
	
s = (p * 25 + d * 0.10) * (1 + (icms / 100))

print(round(s, 2))