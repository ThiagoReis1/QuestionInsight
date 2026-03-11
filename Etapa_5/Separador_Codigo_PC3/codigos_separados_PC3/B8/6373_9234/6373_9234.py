from numpy import*
livro = input("digite a letra: ").upper()
cont = zeros(4,dtype = int)

for i in range (len(livro)):
	if(livro[i]=="A"):
		cont[0] += 1
	elif(livro[i]=="P"):
		cont[1] += 1
	elif(livro[i]=="D"):
		cont[2] += 1
	elif (livro[i]=="M"):
		cont[3] += 1
print(cont)