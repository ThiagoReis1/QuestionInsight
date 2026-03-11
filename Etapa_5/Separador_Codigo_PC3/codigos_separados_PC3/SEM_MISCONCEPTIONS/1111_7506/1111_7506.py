h_ext = float(input())
h_ntrab = float(input())

h = h_ext - (2/3)*h_ntrab

if h > 600.0:
	g = 300.00
else:
	g = 200.00
	
print(h_ext, 'extras e', h_ntrab, 'de falta ')
print('R$', g)
