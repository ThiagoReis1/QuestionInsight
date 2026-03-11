# faça seu código aqui!
q = int(input("quantidade de pratos consumidos: "))
sob = input("sobremesa s ou n ")

if (sob=="s"):
	vt= 40.00*q-0.05*40*q
else:
	vt= 40.00*q
   
print(round(vt,2))