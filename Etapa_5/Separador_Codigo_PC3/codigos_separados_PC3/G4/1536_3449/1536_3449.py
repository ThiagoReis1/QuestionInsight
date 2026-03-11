x= float(input("numero real: "))
k=int(input("quantidade de termos: "))

termo=x
cont=1
e= k
t=1

while	(e > cont):
	termo= termo + ((-1)*(-1)**(cont+1)) *((x**(t+1))/(t+1))
	cont=cont+1
	t= t+1
	
print(round(termo,10))
	