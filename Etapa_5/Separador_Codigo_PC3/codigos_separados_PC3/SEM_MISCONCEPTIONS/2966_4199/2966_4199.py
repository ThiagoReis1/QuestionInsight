genero=input("mulher ?: (S//N)")
v=float(input("valor ingresso"))
qt=int(input("quantidade de ingressos"))
if(genero=="S"):
	preco= (v-v*0.2)*qt
	print(round(preco,2))
else:
	preco=v*qt
	print(round(preco,2))