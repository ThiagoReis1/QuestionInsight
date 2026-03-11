item = input()
quant = int(input())
acai = int(input())

if item == "T":
	total = 4.50 * quant + (acai * 12)
else:
	total = 5 * quant + (acai *12)
	
print(round(total, 1))