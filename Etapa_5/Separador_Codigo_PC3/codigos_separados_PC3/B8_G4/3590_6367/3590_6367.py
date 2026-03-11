from numpy import*
a=array(eval(input("Insira o vetor de fases: ")))
i=0
p=0
while i<size(a):
	if a[i]==1 or a[i]==6:
		p=p+10
	elif a[i]==2 or a[i]==4:
		p=p+5
	elif a[i]==3:
		p=p+0
	elif a[i]==5:
		p=p+20
	i=i+1
print(p)