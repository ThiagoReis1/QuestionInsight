p = input("")
qp = int(input("quantida de pizza ou lanche:"))
qr = int(input("quantidade de refrigerante:"))
total = qp*4.50 + qr* 3.00
	
if p == 'P':
	print(round(qp*4.50 + qr*3.00,2))
	
else: 
	total = qp*6.00 + qr* 3.00
	print(round(total,2))

