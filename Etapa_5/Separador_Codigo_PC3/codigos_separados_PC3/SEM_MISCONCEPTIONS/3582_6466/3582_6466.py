from numpy import*

c= array(eval((input('Vetor de custo dos intens: ')))

v = 0
d = 0
i = 0
while(i < size(c)):
	if(c[i] > 160):
		d = c[i] - 25
		v = d + v
	else:
		v = c[i] + v
	i = i + 1
print(round(v, 2))			

		
