from numpy import *

vn= array(eval(input("nome do alimento:")))
vc= array(eval(input("quantidade:")))
i=0
a=0
while (i< size(vn)):
	if (vn[i] == "BANANA"):
		a= vc[i]*0.97
	if (vn[i] == "BIFE"):
		a=vc[i] * 2.95
	if (vn[i] == "FEIJOADA"):
		a=vc[i] * 1.97
	if (vn[i] == "OMELETE"):
		a=vc[i] * 1.04
	if (vn[i] == "TOMATE"):
		a=vc[i]* 0.2
	i=i+1

print(round(a,2))
