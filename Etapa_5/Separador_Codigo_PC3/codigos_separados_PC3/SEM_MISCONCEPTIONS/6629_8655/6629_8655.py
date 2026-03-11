string = input("").upper()
i = 0
contador = 0
while i < len(string):
	if string[i] == "P":
		print(i)
		contador = contador + 1
	i +=1
if contador == 0:
	print("nao achei")
	