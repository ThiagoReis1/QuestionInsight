qi = int(input("Quantidade inicial de baloes na frota:  "))
qc = int(input(" Quantidade de baloes construidos por semana:  "))
qd = int(input("Quantidade de baloes destruidos por semana:  "))

qb = qi
semanas = 0
while (qb < 200):
	qb = qb + (qc - qd)
	semanas = semanas + 1
	
print(semanas)