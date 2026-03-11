from numpy import*
x=array(eval(input("alvo: ")))
p=0
i=0
while i<size(x):
	if x[i]==1:
		p=p+100
	if x[i]==2:
		p=p+60
	if x[1]==3:
		p=p+20
	i= i+1
print(p)
	
