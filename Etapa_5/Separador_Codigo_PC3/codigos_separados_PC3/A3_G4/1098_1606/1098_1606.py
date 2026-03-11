x = int(input("digite um numero:"))
v1 = int(x//100000.0)
v2 = int(v1%100000.0//10000.0)
v3 = int(v2%10000.0//1000.0)
v4 = int(v3%1000.0//100.0)
v5 = int(v4%100.0//10.0)
v6 = int(v4%10.0)
if (x==v6**4):
	print("x atende a propriedade")
else:
	print("")