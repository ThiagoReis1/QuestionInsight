numero=int(input())
a=numero//1000
ra=numero%1000
b=a//1000
rb=a%1000

calculo=(rb-ra)**2
if(numero==calculo):
	mensagem="atende"
	print(mensagem)
else:
	mensagem="nao atende"
	print(mensagem)
print(int(numero))