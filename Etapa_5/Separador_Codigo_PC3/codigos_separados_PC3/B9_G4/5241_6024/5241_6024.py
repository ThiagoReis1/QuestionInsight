x = int(input("Insira um valor:"))
if x<10:
	resp  = (2 * x) + 20
	print(round(resp,2))
elif x>=10 and x<20:
	resp = (2.5*x)+20
	print(round(resp,2))
elif x>=20 and x<40:
	resp = (2.75*x)+20
	print(round(resp,2))
else:
	resp = (3*x)+20
	print(round(resp,2))