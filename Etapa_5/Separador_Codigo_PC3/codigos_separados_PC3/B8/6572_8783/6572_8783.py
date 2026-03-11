nump=int(input(""))
if nump<3:
	total=(nump*5)+3
	print("total=",round(total,2))
elif nump==3:
	total=(nump*5)+3.25
	print("total=",round(total,2))
elif nump>3:
	total=(nump*5)+4.50
	print("total=",round(total,2))