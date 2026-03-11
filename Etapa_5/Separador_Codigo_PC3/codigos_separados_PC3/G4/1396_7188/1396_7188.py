vc= float(input("valor consumido"))
if vc<= 300:
	a = vc +(vc * 0.1)
	print(round(a,2))
else:
	a = vc + (vc * 0.06)
	print(round(a,2))