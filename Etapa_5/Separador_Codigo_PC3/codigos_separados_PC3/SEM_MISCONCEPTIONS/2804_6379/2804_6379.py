dep = float(input())
meses = int(input())
cont = 0
while cont < meses:
	dep = dep + (dep * 0.01)
	cont = cont + 1
	print(round(dep,2))