from numpy import*

a = input()
c = zeros(5, dtype = int)

for i in range(len(a)):
	if(a[i] == 'A' and a[i+1] == 'C' ):
		c[0] = c[0] + 1
	if(a[i] == 'A' and a[i+1] == 'M'):
		c[1] = c[1] + 1
	if(a[i] == 'P' and a[i+1] == 'A'):
		c[2] = c[2]+1
	if(a[i] == 'R' and a[i+1] == 'O'):
		c[3] = c[3] + 1
	if(a[i] == 'R' and a[i+1] == 'R'):
		c[4] = c[4] + 1
			 
print(max(c))
print(c)