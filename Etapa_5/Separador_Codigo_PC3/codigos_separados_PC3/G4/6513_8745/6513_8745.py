# faça seu código aqui!
man = (int(input("quantidade de combos manha energetica: ")))
if (man<=3):
	v = (man*20)
	vt = v
	print(round(v,2))
else:
	v = (man*20)
	vp = v*(15/100)
	vt = v-vp
	print(round(vt,2))