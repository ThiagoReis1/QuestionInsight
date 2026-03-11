from numpy import*
v = array(eval(input("Qual o vetor das velocidades?: ")))
vl = v[0]
inf = 0
c = 0
while(size(v) > c):
	if(v[c] > 1.5 * vl):
		print(c)
		inf = inf + 1
	c = c + 1
print(inf)		
		