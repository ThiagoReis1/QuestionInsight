q = 5
n = 0
for i in range(q):
	x = float(input("> "))
	n = n+x

med = round(n/5,2)
print(med)
if med < 7:
	print("Reprovado por nota")
else:
	print("Aprovado")