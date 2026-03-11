face=int(input("Isira a face do dado sorteada: "))
num=0
while (face!=-1):
	if face==6:
		num=num+1
	else:
		num=num+0
	face=int(input("Insira a face do dado sorteada: "))
print(num)