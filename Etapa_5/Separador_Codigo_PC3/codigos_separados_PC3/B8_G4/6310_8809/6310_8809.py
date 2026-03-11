from numpy import*
preco=input("ponha aqui os locais de compra (M,P,R): ")
m=0
p=0
r=0
q=len(preco)
i=0
while i < q:
	d=preco[i]
	if d.upper() == "M":
		m=m+1
	elif d.upper() == "P":
		p=p+1
	elif d.upper() == "R":
		r=r+1
	i=i+1
t=(m*7.25)+(p*4.75)+(r*3.50)
print(round(t,2),m,p,r)