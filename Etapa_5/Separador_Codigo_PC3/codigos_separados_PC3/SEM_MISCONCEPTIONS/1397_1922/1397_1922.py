area = float(input())
if(area<=10000):
	custo = area*5
	print(round(custo,2))
else:
	custo = (area - 10000)*4+(10000*5)
	print(round(custo,2))
	
	