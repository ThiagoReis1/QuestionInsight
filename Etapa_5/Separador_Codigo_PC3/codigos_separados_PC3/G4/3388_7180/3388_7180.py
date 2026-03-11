u = str(input("Qual unidade esta: "))
v = float(input("Qual o valor: "))

B = v*3.41214
W = v/3.41214

if(u==B):
	print(round(W,2))
else:
	print(round(B,2))

if(u==W):
	print(round(B,2))
else:
	print(round(W,2))
	