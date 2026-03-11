from numpy import*
v=array(eval(input("digite v: ")))
n=0
cont=0
record= 307 
while(n < size(v)):
	if(v[n]<record):
		cont=cont+1
	n=n+1
print(record)
print(cont)