from numpy import*
n=array(eval(input("Insira os valores: ")))
ns=0
entrada=0
for i in range(0,size(n)):
	if n[i]<=50.0:
		ns=ns+1

r=zeros(ns,dtype=int)

for a in range (0,size(n)):
	if n[a]<=50.0:
		r[entrada]=a
		entrada=entrada+1
		
print(ns)
print(r)