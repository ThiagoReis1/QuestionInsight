d = float(input("valor do deposito: "))
tf = float(input("tarifa mensal: "))
j = float(input("juros: "))
a = d*1.15
t = 0
if((d<=0) or (tf<=0) or (j<=0)):
	print("Dados incorretos")
else:
	while(d <= a):
		t = t+1
		d = round(d * (1+(j/100)) -tf, 2)
	print(t)