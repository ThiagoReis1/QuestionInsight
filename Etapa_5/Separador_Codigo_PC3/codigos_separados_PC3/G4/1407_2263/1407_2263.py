V=float(input("digite um valor para a vida inicial:"))
D1=int(input("digite um valor para o primeiro lancamento:"))
D2=int(input("digite um valor para o segundo lancamento:"))
D3=int(input("digite um valor para o terceiro lancamento:"))
N=D1+D2+D3
d=V-(10*N)
if(d>0):
	mensagem="VIVO"
else:	
	print(0)
	mensagem="MORTO"
print(mensagem)
					