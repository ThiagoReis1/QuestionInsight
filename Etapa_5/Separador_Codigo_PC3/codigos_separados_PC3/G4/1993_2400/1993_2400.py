O=15.9994
C=12.011
N= 14.0067
S= 32.066
H= 1.00794
J=input()
nome=J.lower()

if(nome=='cisteina'):
	A=C*3+H*7+N+O*2+S
	print(round(A,2))
elif(nome=='isoleucina'):
	A=C*6+H*13+N+O*2
	print(round(A,2))
elif(nome=='metionina'):
	A=C*5+H*11+N+O*2+S
	print(round(A,2))
else:
	print("Entrada:",nome)
	print("Dado Invalido")