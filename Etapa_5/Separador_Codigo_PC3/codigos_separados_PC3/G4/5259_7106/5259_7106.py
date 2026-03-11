men = float(input("mensalidade:  "))
num = int(input("num de criancas:  "))

if num == 1:
	total = men-(men*0.10)
	print(round(total, 2))
	
elif num == 2:
	desc= men-(men*0.30)
	total = desc*num
	print(round(total, 2))

else:
	desc = men-(men*0.40)
	total = desc*num
	print(round(total, 2))
