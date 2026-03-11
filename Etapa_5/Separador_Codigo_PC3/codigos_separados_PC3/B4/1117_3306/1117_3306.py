#leitura das entradas
preco= float(input("digite o preco:"))
dia= int(input("digite o dia da semana: "))
musica= input("digite se e dia de musica ao vivo: S OU N").upper()
print("Entradas: ", preco , "," , dia, "," , musica)
preco1= round(preco*(1-0.25), 2)
preco2= round(preco1+20.00, 2)
#todas as condicoes para n
if(preco>=0 and musica=="S"):
	print("Valor a pagar: R$", preco2)
elif(preco>=0 and dia==1 and musica=="N"):
	print("Valor a pagar:R$", preco)
elif(preco>=0 and dia==2 and musica=="N"):
	print("Valor a pagar:R$", preco1)
elif(preco>=0 and dia==3 and musica=="N"):
	print("Valor a pagar:R$", preco1)
elif(preco>=0 and dia==4 and musica=="N"):
	print("Valor a pagar:R$", preco)
elif(preco>=0 and dia==5 and musica=="N"):
	print("Valor a pagar:R$", preco1)
elif(preco>=0 and dia==6 and musica=="N"):
	print("Valor a pagar:R$", preco)
elif(preco>=0 and dia==7 and musica=="N"):
	print("Valor a pagar:R$", preco)
else:
	print("Dados invalidos")

