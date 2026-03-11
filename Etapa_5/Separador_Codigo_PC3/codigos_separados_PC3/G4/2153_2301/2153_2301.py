from numpy import*
v1= array(eval(input()))
v2= array(eval(input()))
soma = 0 
for i in range(size(v1)):
	soma = soma + ((v1[i] - v2[i])**2)
dist = soma**(1/2)
print(round(dist,4))