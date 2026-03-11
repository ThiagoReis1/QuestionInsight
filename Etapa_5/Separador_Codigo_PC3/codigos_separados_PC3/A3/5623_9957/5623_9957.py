bous = input()
qtdbous = float(input())
qtdc = float(input())

salgado = 4.00
bolo = 5.00
capuccino = 7.50

if bous == "B":
	print(bolo * qtdbous + (qtdc * 7.50))
else:
	print(salgado * qtdbous + (qtdc * 7.50))