from numpy import *
mat = array(eval(input("Informe o preco dos materiais: ")))
mf = zeros(size(mat), dtype=float)
c = 0

for i in range(size(mat)):
	if mat[i] > 170:
		mf[i] = mat[i]
		c += 1
	else: 
		mf[i] = 0.0

if sum(mf) == 0:
	print("0.0")
else:	
	media = sum(mf)/c
	print(round(media,2))
