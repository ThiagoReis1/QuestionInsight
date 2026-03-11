from math import*
num=float(input())
#6 CASAS DECIMAIS
k=int(input())
p=3
i=0
flag=1
s=num
x=1
multi=1

#if(=2):
	
while(i<k-1):
	if(flag%2==1):
		while(x<=p):
			multi=s*multi
			x=x+1
		#print(multi/p)
		#print(multi)
		num=num-(multi)/p
		
		#print(num)
		multi=1
		x=1
	if(flag%2==0):
		while(x<=p):
			multi=s*multi
			x=x+1
		#print(multi/p)
		#print(multi)
		num=num+(multi)/p
		#print(num)
		multi=1
		x=1
	flag=flag+1
	p=p+2
	i=i+1
	
print(round(num,6))
	