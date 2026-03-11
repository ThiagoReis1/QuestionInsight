from numpy import*
produto= input('').upper().split(',')
cat= zeros (4, dtype=int)

for v in produto: 
		if v == 'E':
			 cat[0] += 1
		elif v == 'V':
			 cat[1] += 1
		elif v == 'A' :
			 cat[2] += 1
		elif v == 'D':
			 cat[3] += 1
print(cat)