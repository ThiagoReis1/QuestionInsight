qi = int (input("quantidade de baloes: "))
c = int (input("novos baloes: "))
d = int (input("baloes destruidos: "))
semanas = 0
soma = qi
while (soma <= 200):
	soma = soma + c - d
	semanas = semanas + 1
print (semanas)
