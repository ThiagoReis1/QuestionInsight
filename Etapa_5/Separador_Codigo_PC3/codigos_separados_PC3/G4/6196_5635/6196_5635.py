af = float(input())
tc = float(input())
c = 0 

am = 1.5
tcm = 0.02

while (af < am):
	
	af += tc
	am += tcm
	
	c += 1
print(c)