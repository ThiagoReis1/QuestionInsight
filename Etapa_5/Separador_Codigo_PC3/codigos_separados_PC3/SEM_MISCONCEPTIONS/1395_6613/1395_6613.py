a = float(input("valor de vendas: "))

if (a<=1000):
	comisao = a*0.05

else:
	comisao = 1000*0.05 + (a-1000)*0.1
	
print(round(comisao,2))
	