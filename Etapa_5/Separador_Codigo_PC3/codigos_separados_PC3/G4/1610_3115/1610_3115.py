from numpy import*
n = input("")
s = n.split(',')
#print(s)
x = zeros(size(s),dtype=int)
c = 0
while(c<size(s)):
	
	x[c] = s[c] 
	c = c + 1	

print(sum(x))
