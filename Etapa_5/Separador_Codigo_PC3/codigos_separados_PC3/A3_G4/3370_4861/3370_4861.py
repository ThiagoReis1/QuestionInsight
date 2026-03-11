P = 1 
C = 2 
uni = input("unidade de medida: ")
b = float(input("digite o valor da medida: "))
m = float(0.393701*b)
d = float(b*0.393701)

if(uni != 1):
	print(round(m, 2))
	
else:
	print(round(d, 2))
	