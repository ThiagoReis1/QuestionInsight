c = float(input("Valor Inicial: "))
d = float(input("Valor Depositado: "))
m = float(input("Valor mensal fixo:"))
tx = float(input("juros: "))
mes = 0
cont = 0
if(c > 0 and d > 0 and m > 0 and tx > 0):
	while(d < c):
		d = d + (d* (tx / 100)) + m
		d = round(d,2) 
		mes += 1
	print(mes)	
else:
	print("Dados incorretos")
	