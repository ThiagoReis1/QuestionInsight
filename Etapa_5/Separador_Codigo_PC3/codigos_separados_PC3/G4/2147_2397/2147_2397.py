from numpy import*
n=input()
if(len(n)!=11):
	print("INVALIDO")
else:
	i=0
	p=""
	while(i<len(n)):
		if((i%2)!=0):
			p=p+n[i]
		i=i+1
	print(p)