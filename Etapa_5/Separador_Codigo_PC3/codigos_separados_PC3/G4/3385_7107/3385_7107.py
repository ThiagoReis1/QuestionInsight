u = input().upper()
vm = float(input())

if(u == 'A'):
	
	H = (vm / 2.47105)
	r = H
	
else:
	
	A = (2.47105 * vm)
	r = A
	
print(round(r, 2))