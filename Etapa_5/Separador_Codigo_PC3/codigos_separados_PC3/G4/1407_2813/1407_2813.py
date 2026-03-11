Q = int(input(""))
D1 = int(input(""))
D2 = int(input(""))
D3 = int(input(""))

N = D1+ D2 + D3
R = Q - (10*N)

if(R > 0):
	mensagem = "vivo"

else:
	R = Q - (10*N) - Q + (10*N)
	mensagem = "morto"
	
print(R)
print(mensagem.upper())