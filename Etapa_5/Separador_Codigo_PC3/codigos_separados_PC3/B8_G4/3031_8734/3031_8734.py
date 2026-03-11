val = float(input('valor:'))

if val <= 1:
	print('1')
elif 1 < val <= 2:
	print('2')
elif 2 < val <= 3:
	b = val * val
	print(round(b,2))
elif val > 3 :
	c = val * val * val
	print(round(c,2))