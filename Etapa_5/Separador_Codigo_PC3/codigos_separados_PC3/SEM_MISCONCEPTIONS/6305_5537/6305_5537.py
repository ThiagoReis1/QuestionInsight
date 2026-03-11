from numpy import*
vet = input("Digite: ").upper()
i = 0
h = 0
sum_h = 0
l = 0
sum_l = 0
e = 0
sum_e = 0
while(i < len(vet)):
	if(vet[i] == "H"):
		h = h + 1
		sum_h = sum_h + 3.85
	elif(vet[i] == "L"):
		l = l + 1
		sum_l = sum_l + 2.95
	else:
		e = e + 1
		sum_e = sum_e + 7.9
	i = i + 1
sum_total = sum_h + sum_l + sum_e
print(round(sum_total,2),h,l,e)
	