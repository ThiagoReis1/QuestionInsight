q= float(input("quantidade de combustivel: "))

if q>0:
	if q<17.5:
		v=q+1.5
		print(round(v,1))
	elif 17.5<= q <= 35:
		v=q+2.3
		print(round(v,1))
	elif 35<= q <= 50:
		v=q+3.3
		print(round(v,1))
	elif q>=50:
		v=q+4.7
		print(round(v,1))
else:
	print("dados invalidos")