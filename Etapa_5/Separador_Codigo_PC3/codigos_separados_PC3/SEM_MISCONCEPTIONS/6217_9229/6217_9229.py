valorx = int(input(" "))
valory = int(input(" "))

acum = valorx

while acum <= valory:
	if acum % 7 == 0:
		print(acum)
	acum = acum + 1