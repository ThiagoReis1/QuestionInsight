v = float(input("valor de vendas?"))

if(v<=1000):
	valor = (v*0.05)
else:
	valor = (1000*0.05)+((v-1000)*0.1)
print(round(valor, 2))