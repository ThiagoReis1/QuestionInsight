DA = float(input("Valor A: "))
DB = float(input("Valor B: "))
jA = float(input("taxa A: "))
jB = float(input("taxa B: "))

ja = jA / 100
jb = jB / 100

sa = DA
sb = DB 
t = 0

if (DA > 0 and DB > 0 and ja > 0 and jb > 0 and DA > DB and ja < jb):
	while (sa>=sb):
		sa = sa + (sa*ja)
		sa = round(sa , 2)
		sb = sb + (sb*jb)
		sb = round(sb , 2)
		t = t + 1
	print(t)
else:
	print("Dados incorretos")