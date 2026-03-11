cachos_b = int(input("digite quantos cachos: "))

if cachos_b < 3:
	v_compra1 = cachos_b * 5
	print(round(v_compra1,2))
	
if cachos_b >= 3:
	v_compra2 = cachos_b * 4.25
	print(round(v_compra2,2))