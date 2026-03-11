l = input("bote 'L' ou 'S':")
ql= int(input("q. de lanches ou salgados:"))
qr = int(input("q. de refris:"))
if l.upper()=='S':
	t = (ql*3.50)+(qr*4.00)
	print(round(t,2))
else:
	s= (ql*5.00)+(qr*4.00)
	print(round(s,2))