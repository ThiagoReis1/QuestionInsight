na = input("histidina / leucina e lisina: ").lower()
o=15.9994
c=12.011
n=14.00674
h=1.00794
if(na=='histidina'):
	mensagem =((6*c)+(h*10)+(n*3)+(o*2))
	print(round(mensagem,2))
elif(na == 'leucina'):
	mensagem = ((6*c)+(h*13)+n+(o*2))
	print(round(mensagem,2))
elif(na=='lisina'):
	mensagem = ((c*6)+(h*15)+(n*2)+(o*2))
	print(round(mensagem,2))
else:
	print("Entrada: ",na)
	print("Dado Invalido")