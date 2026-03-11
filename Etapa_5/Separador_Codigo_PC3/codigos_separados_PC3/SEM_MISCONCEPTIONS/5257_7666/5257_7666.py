valor = float(input())

if(valor <= 50):
	valor = valor*2
elif(valor <= 100):
	valor = valor*1.5
elif(valor <= 500):
	valor = valor*1.4
else:
	valor = valor*1.3
	
print(round(valor,2))