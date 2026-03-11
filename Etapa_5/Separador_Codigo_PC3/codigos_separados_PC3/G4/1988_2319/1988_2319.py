k = input().upper()
c = 12.011
h = 1.00794
n = 14.00674
o = 15.9994
if k == "ARGININA":
	p = c*6 + h*15 + n*4 +o*2
	print(round(p,2))
elif k == "TIROSINA":
	p = c*9 + h*11 + n + o*3
	print(round(p,2))
elif k == "TRIPTOFANO": 
	p = c*11 + h*11 + n*2 + o*2
	print(round(p,2))
else:
	print("Entrada:",k)
	print("Dado Invalido")
	