from numpy import*
v = array(eval(input("Numeros Naturais: ")))
i = 0
while(i < size(v)):
	v[i] = v[i]**2
	i = i+1
med = (sum(v)/size(v))**(1/2)
print(round(med, 2))