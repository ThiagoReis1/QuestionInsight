v1 = float(input("informe o valor1: "))
v2 = float(input("informe o valor2: "))
v3 =float(input("informe o valor3: "))
limite = float(input("informe o limite: "))

total = v1 + v2 + v3

if (total <= limite):
	msg= "Nao ultrapassou"
else:
	msg="Ultrapassou"
	
print(round(total, 2))
print(msg)