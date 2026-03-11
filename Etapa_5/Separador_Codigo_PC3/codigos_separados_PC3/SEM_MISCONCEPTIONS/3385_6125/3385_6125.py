medida= input()
vm= float(input())
if medida == "H":
	tt= 2.47105 * vm
else:
	tt= vm / 2.47105
print(round(tt,2))	