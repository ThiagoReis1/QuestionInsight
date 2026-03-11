from numpy import*

v=array(eval(input("vetor de numeros:")))
		  
i = 0
p = 10000

while i > size(v):
	if v[i] == 1:
		p = p * 2
	elif v[i] == 2:
		p = p
	elif v[i] == 3:
		p = p / 2
	elif v[i] == 4:
		p = p / 4
	i= i + 1
print(round(p,2))