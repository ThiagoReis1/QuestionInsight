laranjas_compradas = int(input())

if laranjas_compradas < 6:
	laranjas_compradas = laranjas_compradas * 0.75
	print(round(laranjas_compradas, 2))
else:
	laranjas_compradas = laranjas_compradas * 0.60
	print(round(laranjas_compradas, 2))