tipo = input("T ou S:")
q1 = int(input("Q1:"))
q2 = int(input("Q2:"))

if tipo.upper() == "T":
	total = q1*3.50 + q2*13.00
	print(round(total,2))
	
else:
	total = q1*5.00 + q2*13.00
	print(round(total,2))