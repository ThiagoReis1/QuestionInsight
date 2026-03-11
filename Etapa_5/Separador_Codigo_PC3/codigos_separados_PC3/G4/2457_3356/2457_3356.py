from math import*
q = float(input())
a = input()

if (a == "rede"):
	v = 500 * q
	print(round(v,2))
elif (a == "camarote"):
	v = 1200 * q
	print(round(v,2))
elif (a == "suite"):
	v = 1500 * q
	print(round(v,2))
else :
	print("acomodacao invalida")