nome = input("Qual o aminoacido? ").lower()
if (nome == "isoleucina"):
	x = 6*12.011 + 13*1.00794 + 14.0067 + 2*15.9994
	print(round(x,2))
else:
	y = 5*12.011 + 11*1.00794 + 14.0067 + 2*15.9994 + 32.066
	print(round(y,2))