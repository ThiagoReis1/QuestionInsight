area = float(input())

if(area<=10000):
	custo= area*5
	print (round(custo,2))
else:
	excedente = area-10000
	custo = (excedente*4) + 50000
	print (round(custo,2))