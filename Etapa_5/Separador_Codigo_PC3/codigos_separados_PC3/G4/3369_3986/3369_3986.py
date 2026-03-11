u=input("unidade da velocidade M/K: ")
v=float(input("valor da velocidade: ")) 
m=3.6*v
k=v/3.6 
if (u.upper() == "M"):
	print(round(m,2))
else:
	print(round(k,2))