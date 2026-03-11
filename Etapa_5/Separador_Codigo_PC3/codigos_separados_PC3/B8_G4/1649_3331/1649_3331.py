from numpy import*

cor= input("Digite: ").upper().split(',')
mat= zeros(5, dtype=int)

for i in range(size(cor)):
	if cor[i] == "P":
		mat[0]= mat[0] + 1
	elif cor[i] == "C":
		mat[1]= mat[1] + 1
	elif cor[i] == "M":
		mat[2]= mat[2] + 1
	elif cor[i] == "V":
		mat[3]= mat[3] + 1
	elif cor[i] == "A":
		mat[4]= mat[4] + 1
print(max(mat))
print(mat)