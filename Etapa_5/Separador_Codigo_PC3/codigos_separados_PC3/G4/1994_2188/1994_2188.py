ami = input()

o = 15.9994
c = 12.011
n = 14.00674
h = 1.0079

if (ami.lower() == "histidina"):
	hi = (c*6)+(h*10)+(n*3)+(o*2)
	print(round(hi, 2))
elif (ami.lower() == "leucina"):
	le = (c*6)+(h*13)+(n*1)+(o*2)
	print(round(le, 2))
elif (ami.lower() == "lisina"):
	li = (c*6)+(h*15)+(n*2)+(o*2)
	print(round(li, 2))
else:
	print("Entrada:",ami)
	print("Dado Invalido")