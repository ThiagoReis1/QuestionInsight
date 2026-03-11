from numpy import * 

Qsq = array(eval(input("digite a quantidade de saque: ")))
y = 0
Qmax = 0

for x in range(size(Qsq)):
	if Qsq[x] >= 2000:
		Qmax = Qmax + 1
	
print(Qmax)

cont = zeros(Qmax,dtype=int)

for x in range(size(Qsq)): 
	if Qsq[x] >= 2000:
		cont[y] = x
		y = y + 1
	
print(cont)