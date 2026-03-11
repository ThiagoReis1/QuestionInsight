item= input()
qnt_cs= int(input())
qnt_s= int(input())


if item.upper()== "C":
	subtotal= qnt_cs*2 + qnt_s*6
	print(round(subtotal,2))
else:
	subtotal= qnt_cs*4.5+ qnt_s*6
	print(round(subtotal,2))
	