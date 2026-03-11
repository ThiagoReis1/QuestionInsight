from numpy import*

n = array(eval(input('Vetores: ')))


m = 0
i = 0

while(i < size(n)):
	m = m + n[i]**2
	i = i + 1

j = (m/size(n))**(1/2)
print(round(j, 2))