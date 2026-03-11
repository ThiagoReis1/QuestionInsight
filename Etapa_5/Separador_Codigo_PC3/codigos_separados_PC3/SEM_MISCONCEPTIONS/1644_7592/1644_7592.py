from numpy import*

nf = array(eval(input()))

acum = 0

for i in range(size(nf)):
	if (nf[i] < 5):
		acum+=1
		
cont1 = 0
cont2 = zeros(acum, dtype = int)

for i in range(size(nf)):
	if (nf[i] < 5 ):
		cont2[cont1] = i
		cont1+=1
print(acum)
print(cont2)

