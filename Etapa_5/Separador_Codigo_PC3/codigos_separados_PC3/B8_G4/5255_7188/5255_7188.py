pp=int(input("peso"))
d=int(input("distancia"))
c=int(input("codigo"))
if c== 1:
	pt=((pp*25)+(d*0.10)) * ((1.0 + 17/100))
	print(round(pt,2))
elif c== 2:
	pt=((pp*25)+(d*0.10)) * ((1.0 + 17.5/100))
	print(round(pt,2))
elif c== 3:
	pt=((pp*25)+(d*0.10)) * ((1.0 + 18/100))
	print(round(pt,2))
elif c== 4:
	pt= ((pp*25)+(d*0.10)) * ((1.0 + 20/100))
	print(round(pt,2))