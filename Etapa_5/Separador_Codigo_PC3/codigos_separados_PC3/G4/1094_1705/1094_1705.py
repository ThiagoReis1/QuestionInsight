#Luiz Inácio
#Av 02 Ex.02

x=int(input("Insira um número com X com 06 digitos:"))

b=x%1000
c=x//1000

d=((b+c)**2)

if d==x:
	print(x,"X atende a propriedade")
else:
	print(d)
	