bolo = 3.00
cro = 6.00
cap = 5.50
bc = input("B ou C")
qtd = int(input("qtd bc"))
cap1= int(input("qtd cap"))
if bc == "B":
	res = qtd * bolo + cap1 * cap 
else:
	res = qtd * cro + cap1 * cap 
print(round(res, 2))