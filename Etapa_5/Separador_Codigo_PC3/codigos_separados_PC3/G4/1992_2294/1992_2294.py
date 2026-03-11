a = input("").lower()
c = 12.011
o = 15.999
n = 14.00674
h = 1.00794
if (a == "glutamina"):
	f = (c*5)+(h*8)+(n*1)+(o*4)
	print(round(f, 2))
elif (a == "histidina"):
	f = (c*6)+(h*10)+(n*3)+(o*2)
	print(round(f, 2))
elif (a == "prolina"):
	f = (c*5)+(h*10)+(n*1)+(o*2)
	print(round(f, 2))
else:
	print("Entrada: ", a)
	print("Dado Invalido")