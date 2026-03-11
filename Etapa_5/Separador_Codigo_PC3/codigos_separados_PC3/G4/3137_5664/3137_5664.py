from numpy import*

v= array(eval(input('numeros: ')))
m=0
n=size(v)
for i in range(size(v)):
	m= m+(exp(v[i]))

k= log(m/exp(n))
print(round(k,2))
