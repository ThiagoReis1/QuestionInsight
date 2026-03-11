ce = float(input(":"))

x = (ce * 0.60) + 5
y = (ce * 0.75) + 16

if(ce <= 150):
	print(round(x,2))
else:
	print(round(y,2))