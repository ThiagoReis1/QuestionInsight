from numpy import*
dado = array(eval(input("lamcamento do dado: ")))

i = 0
total = 0

while i < len(dado):
	if dado[i] == 1:
		total += 10
	elif dado[i] == 2:
		total += 5
	elif dado[i] == 3:
		total += 10
	elif dado[i] == 4:
		total += 5
	elif dado[i] == 5:
		total += 10
	elif dado[i] == 6:
		total += 5
	i += 1
print(total)