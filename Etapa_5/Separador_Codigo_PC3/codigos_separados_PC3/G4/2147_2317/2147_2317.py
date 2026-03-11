v = input("")
t = ""

if len(v) == 11:
	for i in range(len(v)):
		if i % 2 != 0:
			t += v[i]
		
	print(t)
else:
	print("INVALIDO")