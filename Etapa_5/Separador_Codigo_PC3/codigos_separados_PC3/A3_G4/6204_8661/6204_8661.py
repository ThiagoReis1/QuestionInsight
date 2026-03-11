altura_macaco = 1.86
taxa_macaco = 0.01
af = float(input())
tc = float(input())
c = 0

am = 1.86
tcm = 0.01

while (af < am):
	af += tc
	am += tcm
	
	c += 1
print(c)