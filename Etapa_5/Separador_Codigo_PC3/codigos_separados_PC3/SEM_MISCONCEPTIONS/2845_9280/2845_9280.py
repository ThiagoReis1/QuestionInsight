numeros = eval(input("num: "))
numeros_sub = []
for num in numeros:
	if num == 7:
		numeros_sub.append(8)
	elif num == 9:
		numeros_sub.append(0)
	else:
		numeros_sub.append(num + 1)
print("[" + " ".join(map(str, numeros_sub)) + "]")