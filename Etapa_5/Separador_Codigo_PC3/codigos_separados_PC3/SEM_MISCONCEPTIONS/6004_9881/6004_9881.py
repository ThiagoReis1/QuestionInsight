tomate = int(input("quant de tomates: "))

if tomate >= 4:
	total = tomate * 0.55
	
else:
	total = tomate * 0.75
print(round(total, 2))