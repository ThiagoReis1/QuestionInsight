sal = float(input("qual o salario meu nobre: "))

if sal <= 800:
	sf = sal + (sal*0.50)
	print("Entrada: R$ ",round(sal,2))
	print("Novo salario: R$ ",round(sf,2))
elif sal <= 1000:
	sf = sal + (sal*0.40)
	print("Entrada: R$ ",round(sal,2))
	print("Novo salario: R$ ",round(sf,2))
elif sal <= 1200:
	sf = sal + (sal*0.30)
	print("Entrada")