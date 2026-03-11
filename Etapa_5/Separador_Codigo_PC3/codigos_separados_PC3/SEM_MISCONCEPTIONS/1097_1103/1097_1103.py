numero=int(input())
formula=(numero//1000-numero%1000)**2
if(numero==formula):
	print(numero,"atende a propriedade")
else:
	print(formula)