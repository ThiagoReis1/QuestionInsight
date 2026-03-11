lan = int(input("lancamento:"))
cont = 0
cont5 = 0
while(-1<lan<=10):
	cont = cont + 1
	if(lan==5):
		cont5 = cont5 + 1
	lan = int(input("lancamento:"))
print(cont)
print(round((cont5/cont)*100,2))
	