from numpy import*
v = array(eval(input("Aneis acertados:")))
t = size(v)
a1 = 80
a2 = 40
a3 = 20
a4 = 10
p = 0
i = 0
while( i < t):
	if(v[i] == 1):
		p = p + a1
	if(v[i] == 2):
		p = p + a2
	if(v[i] == 3):
		p = p + a3
	if(v[i] == 4):
		p = p + a4
	i = i + 1
print(p)	
		