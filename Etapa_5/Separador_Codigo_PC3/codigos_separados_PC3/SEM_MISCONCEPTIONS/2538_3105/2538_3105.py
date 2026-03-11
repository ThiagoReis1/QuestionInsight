valor=float(input())
depositadoini=float(input())
depositado=float(input())
juros=float(input())
por=juros/100
t=0

while (depositadoini<valor):
	
	saque=depositado*por			
	depositadoini=depositadoini+saque
	t=t+1
	if (valor<0 or depositadoini<0 or depositado<0 or juros<0):
		print("Dados incorretos")
print(t)
	
	
	
