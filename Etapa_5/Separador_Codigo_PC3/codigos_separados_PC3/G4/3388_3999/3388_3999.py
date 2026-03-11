u=input("unidade: ")
v=float(input("valor da medida: "))
if(u=="B"):
	print(round(v/3.41214,2))
if(u=="W"):
	print(round(3.41214*v,2))