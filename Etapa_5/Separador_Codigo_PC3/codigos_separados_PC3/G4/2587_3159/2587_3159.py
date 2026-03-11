from numpy import*

vl = array(eval(input("velocidade limite :")))

cont = 0

for i in range(size(vl)):
	if vl[i] > vl[0]:
		cont = cont +1
		print(i)

print(cont)