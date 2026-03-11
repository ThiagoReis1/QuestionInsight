v= float(input(""))
m= float(input(""))
j= float(input(""))

j1=j/100
z=0
l=v+v*(20*100)
p1=v*j1

if(v>0 and m>0 and j>0):
	while(v<l):
		p1=v*j1
		p=p1+v
		p1=round(v,2)
		p=round(v,2)
		p1=p1-m
		v=round(v,2)
		z=z+1
	print(z)

else:
	print("Dados incorretos")