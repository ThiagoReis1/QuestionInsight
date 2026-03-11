x = float(input("Informe o valor de x:\n"))

if(x<=-1) or (x>=1):
	print(round(x,2))
elif ((x>-1) and (x<0)) or ((x>0) and (x<1)):
	print("1")
else:
	print("2")