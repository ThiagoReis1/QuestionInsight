programa = input("programa em que: ").upper()

ambas = 0

while (programa != "X"):
	if programa == "A":
		ambas = ambas + 1
		programa = input("programa em que: ").upper()
	else:
		ambas = ambas
		programa = input("programa em que: ").upper()
		
print(ambas)