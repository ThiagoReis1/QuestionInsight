compra = float(input("Digite:"))
form = input("Digite:")

if (form.upper()) == 'C 1':
	print(round(compra,2))
	
elif (form.upper()) == 'C 2':
	print(round(compra+compra*(7/100),2))
	
elif (form.upper()) == 'D':
	print(round(compra-compra*(18/100),2))
	
else:
	print(round(compra-compra*(18/100),2))

