inicial = int(input("Quantidade inicial: "))
c = int(input("Balões Construidos:"))
D = int(input("Balões destruidos: "))
frota = inicial
semana = 0

while (frota < 200):
	semana = semana + 1
	frota = frota - D + c

print(semana)
	

