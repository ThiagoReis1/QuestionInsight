limite=float(input())
valorcompra1=float(input())
valorcompra2=float(input())
valorcompra3=float(input())
valorcompra4=float(input())
valortotal=valorcompra1+valorcompra2+valorcompra3+valorcompra4
	
if (valortotal<=limite):
	print(round(valortotal,2))
	print("Dentro do limite")
		
	
else:
	print(round(valortotal,2))
	print("Estourou o limite")