x= float(input())
k=int(input())
cont=2
d=1
j=1
while(cont<k+1):
	d=d-((x**cont)/cont)*(j)
	j=j*(-1)
	cont=cont+1
print(round(d,10))