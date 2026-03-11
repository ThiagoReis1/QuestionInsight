a = input("Digite o resultado: ")
b = input("Digite quantas vezes: ")

c = "06-vezes"
d = "03-vezes"
e = "01-vez"

if(a=="campeao" and b==c):
	print("CORINTHIANS")
elif(a=="campeao"and b==d):
	print("SANTOS")
elif(a=="vice-campeao" and b==e):
	print("FLAMENGO")
elif(a=="vice-campeao" and b==c):
	print("INTERNACIONAL")
else:
	print("TIME DE FUTEBOL NAO IDENTIFICADO")