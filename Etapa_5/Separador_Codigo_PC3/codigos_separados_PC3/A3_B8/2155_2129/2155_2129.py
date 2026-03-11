from numpy import *

peso= array (eval(input("Informe o peso:")))
altura= array (eval(input("Informe a altura:")))
d= array(zeros(3,dtype=float))

muitoabp = 0
abp = 0
pn = 0
acimap = 0
obes = 0
obess = 0
obesm = 0
imc = (peso/altura**2)

for i in range(size(imc)):
	if (imc[i] < 17):
		muitoabp = muitoabp +1
	elif (imc[i] >= 17 and imc[i] < 49):
		abp = abp +1
	elif (imc[i] >= 18.5 and imc[i] < 24.9):
		pn = pn +1
	elif (imc[i] >=  25 and imc[i] < 29.99):
		acimap = acimap +1
	elif (imc[i] >= 30 and imc[i] < 34.99):
		obes = obes +1
	elif (imc[i] >= 35 and imc [i] < 39.99):
		obess = obess +1
	elif (imc[i] > 40):
		obesm = obesm +1	
v= array ([muitoabp,abp,pn, acimap, obes, obess, obesm])

for i in range(size(d)):		
	d[i] = round(d[i]/size(imc))
x = max(v)
print (round(imc))