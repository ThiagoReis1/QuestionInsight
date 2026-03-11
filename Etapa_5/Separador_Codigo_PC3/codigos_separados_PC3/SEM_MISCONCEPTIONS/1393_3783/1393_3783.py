peso_comida= input()
peso_1= (peso_comida-4999.9)
frete_1=(peso_1*0.05)
peso_2=(peso_comida-5000)
frete_2= ((peso_2*0.04)+60)
if  (peso_comida>5000):
	 print(round(frete_2,2))
else:
	 print(round(frete_1,2))

