dias = int(input("digite:"))

r = 175
c = r*dias

if dias < 15:
	t = 20
elif dias == 15:
	t = 16
elif dias > 15:
	t = 10
print(round(c+t,2))