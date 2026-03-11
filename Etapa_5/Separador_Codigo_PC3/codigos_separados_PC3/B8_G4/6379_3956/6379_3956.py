import numpy as np
inp = input()
inp = inp.replace(",", "")

ca, cb, cc, cd, ce = 0, 0, 0, 0, 0

for i in range(len(inp)):
	if inp[i]=='A':
		ca += 1
	elif inp[i]=='B':
		cb += 1
	elif inp[i]=='C':
		cc += 1
	elif inp[i]=='D':
		cd += 1
	elif inp[i]=='E':
		ce += 1
		
out = np.array([ca, cb, cc, cd, ce])
print(out)