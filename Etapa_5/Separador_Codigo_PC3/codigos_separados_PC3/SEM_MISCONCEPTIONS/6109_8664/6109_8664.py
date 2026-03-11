comb_comum = int(input("Combustivel comum: "))

if comb_comum < 17.5:
	Coaxium = 1.5
	total = comb_comum + Coaxium
	print(round(total, 2))
elif 17.5 <= comb_comum < 35:
	Coaxium = 2.3
	total = comb_comum + Coaxium
	print(round(total, 2))
elif 35.0 <= comb_comum < 50:
	Coaxium = 3.3
	total = comb_comum + Coaxium
	print(round(total, 2))
else:
	Coaxium = 4.7
	total = comb_comum + Coaxium
	print(round(total, 2))