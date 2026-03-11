a=input("machado ou lanca (M/L)?")
b=int(input("fator de sucesso"))
if(a == "machado"):
	dano=30*b/10
	print(dano)
else:
	dano=5+(20*b)/10
	print(dano)