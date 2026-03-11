from numpy import*

n=array(eval(input("Vetor de numeros: ")))
i=0
p=200

while i<size(n):
	if n[i]==2 or n[i]==4 or n[i]==6 :
		p=p*3
	else:
		p=p/2
	i=i+1
print(round(p,2))