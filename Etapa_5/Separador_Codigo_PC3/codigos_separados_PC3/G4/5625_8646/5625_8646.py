a = (input("Tap ou sal: "))
q_1 = int(input("Quantidade: "))
q_2 = int(input("Quantidade de acai: "))

if a == "T":
	op = q_1*5.5 + q_2*10
	print(op)

else:
	op = q_1*4 + q_2*10
	print(op)