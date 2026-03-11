d = float(input("Digite a distancia da corrida em km: "))
tc = float(input("Digite o total de chakra que o ninja possui:  "))

if(tc > d):
	x = (30*d)
	w = x - tc
	print(x)
	print("vai conseguir")
else: 
	print("nao vai conseguir")