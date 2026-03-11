# faça seu código aqui!
num = float(input())
d = 10
if num <5:
	tax=3.75+d
	print(round(tax,2))
elif num == 5:
	tax=4.75+d
	print(round(tax,2))
elif num >5:
	tax=5.75+d
	print(round(tax,2))