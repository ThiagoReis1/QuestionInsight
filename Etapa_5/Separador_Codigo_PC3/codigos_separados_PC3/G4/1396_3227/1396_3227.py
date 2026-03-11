c = float(input("Digite o valor da conta: "))
cm = c*0.1 + c
mm = c*0.06 + c

if ( c<= 300):
	print(round(cm, 2))
else:
	print(round(mm, 2))

	