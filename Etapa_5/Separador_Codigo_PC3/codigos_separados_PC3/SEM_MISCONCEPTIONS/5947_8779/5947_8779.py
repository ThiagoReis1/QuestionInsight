item = input()
qtde_c = int(input("quantidade de coxinhas ou esfirras: "))
qtde_e = int(input("quantidade de sucos: "))

if item == 'C':
	total = qtde_c*2 + qtde_e*6
	print(round(total, 2))
else:
	total= qtde_c*4.5 + qtde_e*6
	print(round(total,2))