x = int(input("quantidade de pecas de roupas:"))
if x<10:
	total = 30 + 3.25
elif x==10:
	total = 30 + 4.50
elif x>10:
	total = 30 + 6.00
print(round(total, 2))