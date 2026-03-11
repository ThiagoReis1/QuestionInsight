from numpy import*
s = input("informe a string: ").split(',')
p = 0
c = 0
m = 0
v = 0
a = 0
if(s.upper()=='P'):
	p = p + 1
elif(s.upper=='C'):
	c = c + 1
elif(s.upper=='M'):
	m = m + 1
elif(s.upper()=='V'):
	v = v + 1
elif(s.upper=='A'):
	a = a + 1
w = zeros(s,dtype)
for i in range(len(s)):
	