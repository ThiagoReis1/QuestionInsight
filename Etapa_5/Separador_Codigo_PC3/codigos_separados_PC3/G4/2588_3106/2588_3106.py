from numpy import*
lim = array(eval(input("Limit/Velocidade: ")))

a = 0 
cont = 0

for i in lim:
	if(i > 1.2*lim[0]) and (i < 1.5*lim[0]) :
		print(a)
		cont = cont + 1
	a = a +1
	
print(cont)