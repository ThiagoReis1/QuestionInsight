tp = (input("T se for fatia de torta ou P se for pastel: "))
quant_tp = float(input("A quantidade de fatias de torta ou pastel: "))
quantcapp = float(input("A quantidade de cappuccinos: "))

t = 6.00
p = 5.00
cappuccino = 4.50

a = (t * quant_tp) + (cappuccino * quantcapp)
b = (p * quant_tp) + (cappuccino * quantcapp)


if(tp == "t"):
	print(a)
	
else:
	print(b)
	
	