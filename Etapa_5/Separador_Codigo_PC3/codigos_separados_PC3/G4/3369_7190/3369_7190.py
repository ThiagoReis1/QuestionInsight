t = input("unidade de velocidade (M/K): ").upper()
v = float(input("velocidade: "))

if(t == "M"):
	print(round(v*3.6,2))
if(t == "K"):
	print(round(v/3.6,2))




