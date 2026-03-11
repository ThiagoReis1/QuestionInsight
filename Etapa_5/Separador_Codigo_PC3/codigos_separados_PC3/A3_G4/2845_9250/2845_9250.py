from numpy import * 

n = array(eval(input("")))
npx = zeros(size(n), dtype=int)

for i in range (len(n)): 
	if n[i] == 0:
		npx = n+1
		if n[i] == 9:
			npx = 0
		
			
		
print(npx)