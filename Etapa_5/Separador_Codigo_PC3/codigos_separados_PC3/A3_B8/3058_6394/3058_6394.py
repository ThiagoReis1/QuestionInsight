area = float(input("Digite o valor da area: "))
valor = 0

if(area>=0 and area<=100):
	custo = 2
	adubo = 100
	valor = (area*custo) + adubo
	print(round(valor, 2))
elif(area>100 and area<=2500):
	custo = 1.8
	adubo = 150
	valor = (area*custo) + adubo
	print(round(valor, 2))
elif(area>2500 and area<=10000):
	custo = 1.5
	adubo = 200
	valor = (area*custo) + adubo
	print(round(valor, 2))
elif(area>10000):
	custo = 1.2
	adubo = 250
	valor = (area*custo) + adubo
	print(round(valor, 2))