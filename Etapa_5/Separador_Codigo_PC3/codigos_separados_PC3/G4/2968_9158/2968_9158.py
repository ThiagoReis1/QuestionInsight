X = input("L ou S: ").upper()
Y = int(input("Quant: "))
Z = int(input("Refri: "))

if X == "L":
	Total = Y * 5 +  Z * 4
	print(float(round(Total, 2)))
else:
	Total = Y * 3.50 + Z * 4
	print(float(round(Total, 2)))