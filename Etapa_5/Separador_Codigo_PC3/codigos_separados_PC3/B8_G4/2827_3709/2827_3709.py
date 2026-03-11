from numpy import*
vn = array(eval(input("notas: "))) #se for entre 4 e 5, arredonda para 4. Se for entre 9 e 10 arrednda para 10
i = 0
while (i < size(vn)):
	if (vn[i] > 4) and (vn[i] < 5):
		vn[i] = 4
	elif (vn[i] > 9) and (vn[i] < 10):
		vn[i] = 10
	i += 1
print(vn)