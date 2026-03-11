vm = float(input("valor da mensalidade:"))
nc = int(input("numero de criancas:"))
total = (vm / nc) + desconto
print(total)

if (nc==1) and (vm == 10/100) :
	r = (vm == total)
	print(round(r,2)
elif (nc==2) and (vm == 30/100) :
	r = (vm == total)
	print(round(r,2))
elif (nc>=3 and vm<=40) :
	r = (vm == total)
	print(round(r,2))
print(round(r,2))