ta= input("ataques(contrucao/polen):")
n = int(input("digite o numero de rodadas:"))
d1= int(input("digite um valor:"))
d2= int(input("digite um valor:"))
n1= n*(d1+d2+1)
n2= d1*d2
if(ta=="constricao"):
	print(n1)
if(ta=="polen"):
	print(n2)

	