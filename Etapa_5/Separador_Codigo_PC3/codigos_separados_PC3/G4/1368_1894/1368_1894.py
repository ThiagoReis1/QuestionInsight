colmeia = float(input("quantidade de casca de colmeia: "))
alho = float(input("quantidade de alho: "))
oleo = float(input("quantidade de oleo: "))

qtdc = colmeia / 0.2
qtda = alho / 0.32
qtdo = oleo / 1.29

min1 = min(qtdc,qtda,qtdo)

print(int(min1))