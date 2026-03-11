x = input("palavra: ").upper()

o = 15.9994
c = 12.011
n = 14.00674
h = 1.00794

if(x == "ALANINA"):
	A = (c*3) + (h*7) + n + (o*2)
	print(round(A,2))
elif(x == "VALINA"):
	V = (c*5) + (h*11) + n + (o*2)
	print(round(V,2))
elif(x == "TIROSINA"):
	T = (c*9) + (h*11) + n + (o*3)
	print(round(T,2))
else:
	print("Entrada: ", x)
	print("Dado Invalido")
	