lanche = input()
qLanche = int(input())
qCap = int(input())

if lanche.upper() == "T":
	print(round((qLanche*6)+(qCap*4.5), 2))
if lanche.upper() == "P":
	print(round((qLanche*5) + (qCap*4.5), 2))

