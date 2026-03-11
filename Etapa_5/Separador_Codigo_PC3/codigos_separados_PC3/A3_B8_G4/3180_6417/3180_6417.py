from numpy import *

vet = array(eval(input("Sorotipos dos pacientes: ")))
m = size(vet)

vetf = zeros(4, dtype=int)
soum = 0
sdois = 0
stres = 0
squa = 0

for i in vet:
	if i == 1:
		soum = soum + 1
		vetf[0] = soum
	elif i == 2:
		sdois = sdois + 1
		vetf[1] = sdois
	elif i == 3:
		stres = stres + 1
		vetf[2] = stres
	elif i == 4:
		squa = squa + 1
		vetf[3] = squa
		
print(vetf)
	