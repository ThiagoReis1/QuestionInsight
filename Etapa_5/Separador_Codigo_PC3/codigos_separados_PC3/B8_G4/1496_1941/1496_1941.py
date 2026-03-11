#o custo do servico depende do tempo de voo
t = int(input("tempo de voo: "))


if((t>=0)and(t<=100)):
	c1 = 80
	c2 = 3000
	vt= t * c1 + c2
elif((t>100)and(t<=200)):
	c1 = 90
	c2 = 4000
	vt= t * c1 + c2
elif((t>200)and(t<=300)):
	c1 = 100
	c2 = 5000
	vt= t * c1 + c2
elif(t>300):
	c1 = 110
	c2 = 6000
	vt= t * c1 + c2
	
print(float(round(vt, 2)))