bc = input("escolha (b) para bolo ou (c) para croissant: ").upper()
qtd = int(input("quantidade de fatias: "))
qtd_capp = int(input("quantidade de cappuccinos: "))

if bc == "B":
	vt = (qtd*3.00) + (qtd_capp*5.50)
	print(vt)
	
else:
	vt = (qtd*6.00) + (qtd_capp*5.50)
	print(vt)
	