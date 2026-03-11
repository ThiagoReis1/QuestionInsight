tempo = int(input("tempo de voo: "))

if tempo > 0 and tempo <= 100:
	total = tempo * 80.00 + 3000.00
elif tempo > 100 and tempo <= 200:
	total = tempo * 90.00 + 4000.00
elif tempo > 200 and tempo <= 300:
	total = tempo * 100.00 + 5000.00
elif	tempo > 300:
	total = tempo * 110.00 + 6000.00
print(round(total, 2))