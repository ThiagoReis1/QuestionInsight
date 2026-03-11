N=int(input("digite num: "))
acum = 1
cont= 0
inv=-1
div=1
sf=0
while(cont != N):
	inv= inv*(-1)
	acum=acum+1
	div=div+ 2
	cont = cont +1
	Sf =inv*(acum**2)/(7+div)
print(round(sf,11))