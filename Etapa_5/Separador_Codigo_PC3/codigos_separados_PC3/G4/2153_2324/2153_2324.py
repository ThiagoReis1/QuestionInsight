from numpy import*
v=array(eval(input()))
q=array(eval(input()))
j=0
for i in range(size(v)):
	j=(v[i]-q[i])**2+j
print(round((j)**(1/2), 4))