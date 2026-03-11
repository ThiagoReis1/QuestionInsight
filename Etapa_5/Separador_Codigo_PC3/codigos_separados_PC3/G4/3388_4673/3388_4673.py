m=input("B ou W:")
vm=float(input("valor da medida:"))
if(m=="B"):
	B=(vm / 3.41214)
else:
	B= (3.41214 * vm)
print(round(B,2))

	