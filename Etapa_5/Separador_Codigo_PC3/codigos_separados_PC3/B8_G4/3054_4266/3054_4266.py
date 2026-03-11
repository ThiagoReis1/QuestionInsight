ch = float(input("Digite a quantidade de horas trabalhada: "))

if (0<=ch<=10):
	valor= 50.00
	bon = 500.00
elif(10<ch<=20):
	valor = 60.00
	bon = 600.00
elif(20<ch<=30):
	valor = 70.00
	bon = 700.00
elif(ch>30):
	valor = 80.00
	bon = 800.00

pg = ch*valor+bon
print(round(pg,2))