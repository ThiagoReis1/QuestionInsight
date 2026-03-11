# faça seu código aqui!
ddl = 32.90
qddl = int(input("quantas ddl vc deseja?"))
total = qddl*ddl


if qddl > 3:
	print(round(total-total*0.2, 2))
else:
	print(round(total ,2))
	