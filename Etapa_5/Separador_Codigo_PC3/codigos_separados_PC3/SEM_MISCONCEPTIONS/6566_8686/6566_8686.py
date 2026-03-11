qnt = int(input("roupas: "))

if (qnt == 10):
	total = 30 + 4.50
elif (qnt > 10):
	total = 30 + 6.00
else: 
	total = 30 + 3.25
total = round(total, 2)
print("total= " + str(total))