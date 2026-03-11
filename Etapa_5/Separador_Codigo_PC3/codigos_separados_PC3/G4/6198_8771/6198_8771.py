hl = 1.65
tl = 0.02
hp= float(input())
tp= float(input())

cont=0
while hl>hp:
	hl=hl+tl
	hp=hp+tp
	cont=cont+1
print(cont)