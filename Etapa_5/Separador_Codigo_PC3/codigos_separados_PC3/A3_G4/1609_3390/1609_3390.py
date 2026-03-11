from numpy import*

dic= array(eval(input()))
n= len(dic)
palavra=  input()
i=0
j=0
palavra= palavra.replace("R","L")
while n>i:
	if dic[i]==palavra:
		print(i)
		j=1
	i=i+1
if j==0:
	print("NAO ENCONTRADA")
	
