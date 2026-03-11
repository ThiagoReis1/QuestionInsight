c = float(input("conbustivel: "))

if c < 17.5:	
	f = c + 0.8
	print(round(f, 4))
elif c == 17.5 or c <= 35:
		f = c + 1.3
		print(round(f, 4))
elif c == 35.0 or c <= 50.0:
		f = c + 2.1
		print(round(f, 4))
else:
	c > 50.0
	f = c + 3.0
	print(round(f, 4))
