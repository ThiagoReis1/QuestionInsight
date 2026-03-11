#Entradas:
qi = int(input("Número de balões: "))
qc = int(input("Número de balões: "))
qd = int(input("Número de balões: "))

#Contadores:
i = 0
soma = 0

#Laço:
while(qi < 200):
	qi = qi + qc - qd
	soma = soma + qi
	i = i + 1
	
print(i)
	
	