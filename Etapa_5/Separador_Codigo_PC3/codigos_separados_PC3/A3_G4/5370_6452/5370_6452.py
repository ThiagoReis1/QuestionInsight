from numpy import*
v=array(eval(input('digite o vetor: ')))
i=0
m='True'
while i<size(v)-1:
	if v[i]>v[i+1]:
		m="False"
	i=i+1
print(m)
	