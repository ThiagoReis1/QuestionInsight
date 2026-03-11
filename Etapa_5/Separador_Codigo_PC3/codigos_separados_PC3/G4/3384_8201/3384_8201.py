op=input("O para oncas K para quilos ")
if op=="K":
	q=float(input("quanto "))
	oz=35.274*q
	print(round(oz, 2))
else:
	q=float(input("quanto "))
	k=q/35.274
	print(round(k, 2))