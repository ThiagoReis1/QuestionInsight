from numpy import*

p= array(eval(input("coepigabau:")))
q= array(eval(input("quequehavelinho:")))
x=0
a= p

for i in range(size(a)):
	x= x+(p[i]+q[i])**2
	sim= (1 /1+x)

print(round(x ,4))
