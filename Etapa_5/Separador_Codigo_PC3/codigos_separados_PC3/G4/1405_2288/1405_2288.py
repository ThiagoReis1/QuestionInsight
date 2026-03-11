ataque = input("qual o nome do ataque? ")
d1 = int(input())
d2 = int(input())

if ( ataque == "grito"):
	pvp =  6 + d1 + d2
	print(pvp)
else:
	pvp = (d1+d2)**2
	print(pvp)
	