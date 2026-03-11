op=input("T para tapioca S para salgado ")
if op=="T":
	qt=int(input("quantas tapiocas "))*3.5
	qa=int(input("quantos acais "))*13
	to=qt+qa
	print(round(to, 1))
else:
	qs=int(input("quantos salgados "))*5
	qa1=int(input("quantos salgados "))*13
	t1=qs+qa1
	print(round(t1, 1))
	