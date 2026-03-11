v=float(input("Valor de vendas: "))

if (v<=1000):
	p=v*0.05
	print(round(p,2))
else:
	p=(1000*0.05)+((v-1000)*0.1)
	print(round(p,2))