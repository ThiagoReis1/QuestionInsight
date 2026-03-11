nome = input("nome do peso molecular: ").lower()
o = 15.999
c= 12.011
n= 14.00674
h= 1.00794
if(nome == 'glutamina'):
	x=((c*5)+(h*8)+(n*1)+(o*4))
	print(round(x,2))
elif(nome =='histidina'):
	x=((c*6)+(h*10)+(n*3)+(o*2))
	print(round(x,2))
elif(nome == 'prolina'):
	x=((c*5)+(h*10)+n+(o*2))
	print(round(x,2))
else:
	print("Entrada: ",nome)
	print("Dado Invalido")