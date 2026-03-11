from numpy import*
v = array(eval(input("Vetor: ")))
vl = v[0]
n = 0
c = 0
for i in v:
	if(v[i] > vl):
		print(c)
	else:
		n = n + 1
	c = c + 1
print(n)