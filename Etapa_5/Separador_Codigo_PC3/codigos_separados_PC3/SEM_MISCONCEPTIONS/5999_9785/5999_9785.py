laranjas = int(input())

if laranjas < 6 :
	p_laranjas = 0.75 * laranjas
	print(round(p_laranjas,2))
else:
	p_laranjas = 0.60 * laranjas
	print(round(p_laranjas,2))