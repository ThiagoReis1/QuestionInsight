# Monalisa Pereira 21600560
# 280716
# Av 04 - Ex 01

Z = int(input("Insira o número inicial de zumbis: "))
H = int(input("Insira o número de habitantes da vila: "))
X = int(input("Insira o número de zumbis que podem ser transformados por dia: "))
Y = int(input("Insira o número de zumbis que podem ser exterminados por dia: "))

d = 1

while (Z<H):
	Z = Z*X-Y
	d = d+1

print(d)