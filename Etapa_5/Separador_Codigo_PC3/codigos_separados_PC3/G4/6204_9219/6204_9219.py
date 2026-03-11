am = 1.86
tm = 0.01

ac = float(input())
tc = float(input())

anos = 0

while am>=ac:
	ac = ac + tc
	am = am + tm
	anos += 1
print(anos)