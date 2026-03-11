from numpy import*
dic=array(eval(input()))
pal=input()
n=len(dic)
i=0
j=0
while n>i:
	pal=pal.replace("R","L")
	if dic[i]==pal:
		print(i)
		j=1
	i=i+1
if j==0:
	print("NAO ENCONTRADA")