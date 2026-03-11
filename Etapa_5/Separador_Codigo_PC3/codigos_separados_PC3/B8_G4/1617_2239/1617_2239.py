from numpy import *
tesp = array(eval(input()))
niv = array(eval(input()))
i=0
soma=0

while(i<size(tesp)):
	if(tesp[i]=="CENOURA"):
		soma += (2*(niv[i]))
	elif(tesp[i]=="FERRO"):
		soma += (4*(niv[i]))
	elif(tesp[i]=="DWARVEN"):
		soma += (8*(niv[i]))
	elif(tesp[i]=="ELVEN"):
		soma += (11*(niv[i]))
	elif(tesp[i]=="DAEDRIC"):
		soma += (14*(niv[i]))
	i += 1
print(soma)
