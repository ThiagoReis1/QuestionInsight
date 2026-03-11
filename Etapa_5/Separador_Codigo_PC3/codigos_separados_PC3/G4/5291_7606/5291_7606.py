resp = input("qual a resposta").upper()
i = 0
a = 0
while resp!= "S":
	a = a + 1
	if resp == "SIM":
		i = i + 1
	resp = input("qual a resposta").upper()
	total = (i * 100) / a
print(a)
print(round(total,2))
	
	
