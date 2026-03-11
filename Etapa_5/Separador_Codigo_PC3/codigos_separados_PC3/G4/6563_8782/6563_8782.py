dias=float(input(""))
if dias<15:
	c=dias*175+20
	print("total=",round(c,2))
elif dias==15:
	c=dias*175+16
	print("total=",round(c,2))
else:
	c=dias*175+10
	print("total=",round(c,2))