salario = float(input())

if (salario<1212):
	reajuste = (salario * 0.12)+salario
	print (round(reajuste, 2))
elif (salario>=1212 and salario<=5000):
	reajuste = (salario*0.08)+salario
	print(round(reajuste, 2))
elif (salario>=5000):
	reajuste = (salario*0.03)+salario
	print(round(reajuste, 2))