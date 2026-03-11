tomates =  int(input(" "))

if(tomates >= 4):
	conta = tomates * 0.55
	print(round(conta, 2))
else:
	conta = tomates * 0.75
	print(round(conta, 2))