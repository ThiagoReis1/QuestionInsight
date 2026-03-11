csm = int(input("Insira o consumo mensal em kWh: ")) #variável de consumo
vf1 = 5 #valor fixo da primera situação
vf2 = 16 #valor fixo da segunda situação
lim = 150 #limite mensal de 150 kWh

if( csm <= lim):
	vC = 0.60*csm + vf1
else:
	vC = 0.75*csm + vf2
print(round(vC,2))
