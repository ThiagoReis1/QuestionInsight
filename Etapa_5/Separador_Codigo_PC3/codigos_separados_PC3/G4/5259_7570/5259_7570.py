x = float(input("Valor da mensalidade: "))
y = float(input("Numero de criancas: "))
if(y == 1):
	m=x*0.10
	m1=x-m
	print(round(m1, 2))
elif(y==2):
	m = x * y
	m1=m*0.30
	m2=m-m1
	print(round(m2, 2))
else:
	m=x*y
	m1=m*0.40
	m3=m-m1
	print(round(m3, 2))