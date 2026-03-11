x=float(input("Populacao inicial de tambaquis no tanque. "))
y=float(input("Taxa anual de crescimento (em %) do numeros de peixes. "))
z=float(input("Numero de tambaquis retirados anualmente. "))
while(z<=12000):
	s=s+1
	x=x-x*z
	if(s==0.08):
	   x=x-x*y+z
if(z>=2000):
		print(s)
	