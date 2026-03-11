a= float(input("digite a nota da prova: 1"))
b= float(input("digite a nota da prova: 2"))
c= float(input("digite a nota da prova: 3"))

media= (a + b +c)/3
if(round(media,1)>= 7.0):
	print(round(media,1))
	print("Aprovado")
else: 
	print(round(media,1))
	print("Reprovado")

	