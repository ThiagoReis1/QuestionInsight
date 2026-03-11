x = input("Digite a palavra: ").upper()
v = 0
for i in range(0,len(x)):
	if x[i]=="A" or x[i]=="E" or x[i]=="I" or x[i]=="O" or x[i]=="U":
		v = v + 45.12
	else:
		v = v + 50.18
print(round(v,2))