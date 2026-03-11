abc = input("A, B ou C: ")
qnt = int(input("quantidade: "))

total = qnt * 30
if (abc.upper() == "C"):
	desc = total * 0.15
	total = total - desc
	print(round(total, 2))
else:
	print(round(total, 2))	