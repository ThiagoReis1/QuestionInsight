from numpy import*
v = (input("Digite uma palavra: ")).upper()
x = 0
for i in range(len(v)):
	if v[i] == "M":
		print(i)
		x = x +1
if x == 0:
	print("nao achei")


