from numpy import*
cor_olhos = (input("digite a cor dos olhos: ")).split(',')
cor = range(4,dtype=int)
for i in range(cor_olhos):
	if (cor_olhos == 'P'):
		cor[0] = cor[0] + 1
	elif(cor_olhos == 'C'):
		cor[1] = cor[1] + 1
	elif(cor_olhos == 'M'):
		cor[2] = cor[2] + 1
	elif(cor_olhos == 'V'):
		cor[3] = cor[3] + 1
	elif(cor_olhos == 'A'):
		cor[4] = cor[4] + 1 
print(size(cor_olhos))
print(cor)