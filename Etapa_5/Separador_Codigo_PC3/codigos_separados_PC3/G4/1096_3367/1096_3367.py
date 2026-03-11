N=int(input("digete o numero fornecido"))
A=N//10000
RA=N%10000
B=RA//100
RB=RA%100
calculo=(A**3)+(B**3)+(RB**3)

if (N==calculo):
	mensagem="atende"
else:
	mensagem="nao atende"
	
print(mensagem, N)	
