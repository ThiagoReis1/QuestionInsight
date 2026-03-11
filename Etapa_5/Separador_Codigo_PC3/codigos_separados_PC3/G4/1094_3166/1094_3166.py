from math import*
numcp= float(input("ditige o numero"))
n1 = numcp //1
n2 = n1%10
n3 = numcp //10
n4 = n3%10
n5 = numcp //100
n6 = n5%10
n7 = numcp //1000
n8 = n7%10
n9 = numcp //10000
n10 = n9%10
n11 = numcp //100000
n12 = n11%10
numcp = n2,n4,n6,n8,n10,n12
X = (494+209)**2 
if (numcp == X):
	print("atende")
	print(X)
else:
	print("nao atende")
	print(X)
	
