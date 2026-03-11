v = float(input("Venda por funcionario: "))

if(v <= 1000):
	a= v*0.05
else:
	a = (1000*0.05)+((v-1000)*0.1)
	
print(round(a,2))