altura_cicero = 1.8
taxa_cicero = 0.01

altura_fulano = float(input("Qual a sua altura? "))
taxa_fulano = float(input("E a sua taxa de crescimento por ano? "))

cont = 1

while (altura_cicero > altura_fulano):
	altura_cicero = altura_cicero + taxa_cicero
	altura_fulano = altura_fulano + taxa_fulano
	if (altura_cicero > altura_fulano):
		cont = cont + 1
print(cont)
		