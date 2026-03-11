
c = float(input())
d = float(input())
m = float(input())
j = float(input())

if((c>0) or (d>0) or (m>0) or (j>0)):
	
	cont = 0
	p = d
	
	while(p < c):
		p = p + m*(j)
		cont = cont + 1		
	print (cont/2)
else:
	print("Dados incorretos")
	