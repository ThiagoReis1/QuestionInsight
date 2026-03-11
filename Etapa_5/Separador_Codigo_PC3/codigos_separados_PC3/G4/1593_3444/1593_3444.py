from numpy import*
vn = array(eval(input("digite as notas: ")))
i = 0
cont = 0

for i in vn:
	if(i == 0):
		cont = cont[0] + 1
	if(i == 5):
		cont = cont + 1
med = ((vn[0]*1)+(vn[1]*2)+(vn[2]*3)/size(vn))

print(round(med,2))