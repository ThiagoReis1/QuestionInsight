c = int(input("combustivel?: "))

if (( c > 0 ) and (c < 17.5)):
	conta = c + 0.8
	print(round(conta, 1))
elif (( c > 0) and (c >= 17.5) and (c <= 35.0)):
	conta = c + 1.3
	print(round(conta, 1))
elif (( c > 0) and (c >= 35.0) and (c <= 50.0)):
	conta = c + 2.1
	print(round(conta, 1))
elif ((c > 0) and (c > 50)):
	conta = c + 3.0
	print(round(conta, 1))
