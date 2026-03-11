na=input("Nome do aminoacido: ")
O= 15.9994
C=12.011
N= 14.0067
S= 32.066
H= 1.00794
i= na.lower()

if i == "cisteina" :
	a= C*3 + H*7 + N + O*2 + S
	print(round(a,2))
elif i == "isoleucina" :
	b= C*6 + H*13 + N + O*2
	print(round(b,2))
elif i == "metionina" :
	j= C*5+H*11+N+O*2+S
	print(round(j,2))
else:
	print("Entrada:", i)
	print("Dado Invalido")
