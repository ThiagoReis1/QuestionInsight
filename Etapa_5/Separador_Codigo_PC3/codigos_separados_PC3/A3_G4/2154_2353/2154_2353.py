from numpy import*

p=array(eval(input("digite p: ")))
q=array(eval(input("digite q: ")))

vet=zeros

soma=0

for i in range(size(q)) :
	soma=soma+((p[i]-q[i])**2)
	d=sqrt(soma)
	
print(round(d,4))
print(round(1/(1+d),2))
	