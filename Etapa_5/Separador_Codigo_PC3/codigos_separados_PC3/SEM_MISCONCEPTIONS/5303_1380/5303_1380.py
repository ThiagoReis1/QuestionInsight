massa = int(input("Informe a massa inicial do material: "))
taxa = 10.0
massa_atual = massa
massa_meta = 0.5
cont = 0

while (massa_atual > massa_meta):
	massa_atual -= massa_atual * taxa / 100.0
	cont += 1

print(cont)