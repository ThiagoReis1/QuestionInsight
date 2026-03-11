qi = int(input("Digite a quantidade inicial de baloes: "))
qc = int(input("Digite a quantidade de baloes construidos: "))
qd = int(input("Digite a quantidade de baloes destruidos: "))

semanas = 0
b = qi

while(b < 200):
	b = b-qd+qc
	semanas = semanas + 1
print(semanas)
