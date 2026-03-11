cenoura = int(input())
if cenoura >= 5:
	desconto = cenoura * 0.90
	print(round(desconto,2))
else:
	comum = cenoura * 1.20
	print(round(comum,2))