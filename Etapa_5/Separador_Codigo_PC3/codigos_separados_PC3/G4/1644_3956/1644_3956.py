import numpy as np
inp = eval(input())
cr = 0
ls = []
for i in range(len(inp)):
	if inp[i]<5:
		cr+=1
		ls.append(i)
		
print(cr)
print(np.array(ls))
		
