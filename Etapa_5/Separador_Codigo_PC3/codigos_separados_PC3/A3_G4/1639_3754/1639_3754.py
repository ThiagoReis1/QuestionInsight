from numpy import*

par = array(eval(input("Digite: ")))

r = zeros(3, dtype=int)
cont =0 
for x in par:
	npar = 0
	
	if(npar % 2 == 0):
		npar += 1
	cont += 1	
print(npar)	
	