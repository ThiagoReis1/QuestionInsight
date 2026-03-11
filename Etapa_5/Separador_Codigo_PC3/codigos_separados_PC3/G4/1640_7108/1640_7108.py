from numpy import*
v= array(eval(input()))
p=0
im=0

for i in range(size(v)):
	if v[i]%2==0:
		p= p+1
		
	else: 
		n= p+im
		cont= zeros(n,dtype=int)
		im= im+1
		cont = cont + 1
print(im)
print(cont)






		
