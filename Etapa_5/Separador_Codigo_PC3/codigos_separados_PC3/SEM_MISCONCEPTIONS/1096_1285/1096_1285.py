num = int(input("diite o numero: "))
prim1 = num//10000
resto1 = num%10000
prim2 = resto1//100
prim3 = resto1%100
propriedade = prim1**3 + prim2**3 + prim3 **3
if (propriedade == num):
	print (num, "atende a propriedade")
else:
	print (propriedade)

