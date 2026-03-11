from math import *

nu = int(input("numero fornecido pelo usuario: "))
n1 = nu // 100
n2 = nu % 100


if(nu == ((n1 + n2)**2)):
	print(nu)
	print("atende")
else:
	print(nu)
	print("nao atende")