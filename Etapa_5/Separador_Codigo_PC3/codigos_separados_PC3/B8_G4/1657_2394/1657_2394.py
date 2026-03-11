from numpy import*
s = input().split(',')
a = 0
c = 0
f = 0
p = 0
w = 0
z = zeros(5, int)
for x in range(size(s)):
	if(s[x] == "az".upper()):
		a = a + 1
	elif(s[x] == "ca".upper()):
		c = c + 1		
	elif(s[x] == "fl".upper()):
		f = f + 1		
	elif(s[x] == "pa".upper()):
		p = p + 1		
	elif(s[x] == "wi".upper()):
		w = w + 1
v = max(a,c,f,p,w) 
print(v)
z[0] = a
z[1] = c
z[2] = f
z[3] = p
z[4] = w
print(z)
