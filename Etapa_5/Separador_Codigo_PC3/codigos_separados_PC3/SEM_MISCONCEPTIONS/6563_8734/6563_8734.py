dias = float(input('dias'))

d = 175 

if dias < 15:
	total = (dias * d) + 20
	print('total=',total)
elif dias == 15:
	total = (dias * d) + 16
	print('total=',total)
	
else:
	total = (dias * d) + 10
	print('total=',total)