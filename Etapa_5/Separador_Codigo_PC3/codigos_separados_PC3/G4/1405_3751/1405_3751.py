ataque = input().lower()
d1 = int(input())
d2 = int(input())

if ataque == "grito":
	pvp = 6 + d1 + d2
else:
	pvp = pow(d1 + d2, 2)

print(pvp)