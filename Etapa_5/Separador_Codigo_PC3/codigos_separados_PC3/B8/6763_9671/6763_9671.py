tempo = float(input("qual foi o tempo de permanencia? "))

if tempo < 2:
	taxa = 1.25
elif tempo == 2:
	taxa = 2.25
elif tempo > 2:
	taxa = 3.25

total = 5 + taxa
print(round(total, 2))