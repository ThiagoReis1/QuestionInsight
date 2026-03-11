a = float(input("insira a altura: "))
t = float(input("insira o valor da taxa:"))
altura_chico = 1.5
taxa_chico = 0.02
y = 0
while (a<altura_chico):
	y += 1
	a += t
	altura_chico += taxa_chico
print(y)
