nome = input().lower()

C = 12.011
H = 1.0079
N = 14.00674
O = 15.9994



if(nome == "histidina"):
	p = C*6 + H*10 + N*3 + O*2 
	print(round(p,2))
elif(nome == "leucina"):
	p = C*6 + H*13 + N + O*2
	print(round(p,2))
elif(nome == "lisina"):
	p = C*6 + H*15 +	N*2 + O*2
	print(round(p,2))
else:
	print("Entrada:",nome)
	print("Dado Invalido")
	