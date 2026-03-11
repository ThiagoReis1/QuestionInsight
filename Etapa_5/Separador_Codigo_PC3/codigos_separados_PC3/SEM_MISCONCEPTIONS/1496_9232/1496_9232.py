tempo = int(input("quanto tempo? "))

if 0 < tempo < 100:
	total = tempo * 80 + 3000
	print(round((total), 2))
	
if 100 < tempo < 200:
	total1 = tempo * 90 + 4000
	print(round((total1), 2))
	
if 200 < tempo < 300:
	total2 = tempo * 100 + 5000
	print(round((total2), 2))
	
if 300 < tempo:
	total3 = tempo * 110 + 6000
	print(round((total3), 2))