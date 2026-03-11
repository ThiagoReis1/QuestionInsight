espigas = int(input("unidades de espigas de milho: "))

if espigas <= 6 :
	total = espigas * 1.85
else:
	total = espigas * 1.50

print(round(total,2))