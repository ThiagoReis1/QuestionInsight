altura_macaco = 1.86
taxa_macaco = 0.01

ac = float(input())
tc=float(input())
anos = 0
while (ac<altura_macaco):
	ac+=tc
	altura_macaco+=taxa_macaco
	anos+=1
print(anos)