satisfacao = input().upper()

cont = 0
sim = 0

while satisfacao != "X":
	cont += 1
	if satisfacao == "S":
		sim += 1
	satisfacao = input().upper()
print(sim)