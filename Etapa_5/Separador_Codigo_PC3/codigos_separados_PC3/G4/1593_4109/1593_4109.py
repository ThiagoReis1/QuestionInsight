from numpy import*

x = array(eval(input("Notas: ")))
i = 0
s = 0
p = 1

while(size(x)>i):
	s += (x[i]*p)
	p += 1 
	i += 1

print(round(s/(i), 2))
