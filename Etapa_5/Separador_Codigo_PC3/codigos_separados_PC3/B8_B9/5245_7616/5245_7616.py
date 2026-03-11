sal = float(input("Salario: "))
msg = "Novo salario: R$ "

if sal <= 0:
	print("Dado invalido")
elif sal > 0 and sal < 800:
	total = sal + (sal * 50/100)
	print(msg, round(total,2))
elif sal >= 800 and sal < 1000:
	total = sal + (sal * 40/100)
	print(msg, round(total,2))
elif sal >= 1000 and sal < 1200:
	total = sal + (sal * 30/100)
	print(msg, round(total,2))
elif sal >= 1200 and sal < 1400:
	total = sal + (sal * 20/100)
	print(msg, round(total,2))
elif sal >= 1400 and sal < 1600:
	total = sal + (sal * 10/100)
	print(msg, round(total,2))
elif sal >= 1600: 
	total = sal + (sal * 5/100)
	print(msg, round(total,2))
	