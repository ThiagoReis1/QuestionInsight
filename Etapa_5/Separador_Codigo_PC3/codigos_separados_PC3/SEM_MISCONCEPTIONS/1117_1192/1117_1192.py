preco=float(input())
dia=int(input())
diam=input()

print("Entradas:",preco,dia,diam)
if (preco>=0 or (dia>=0 and dia<=0) or (musica=="S" or musica=="N")):
  if (dia==1 and diam=="N"):
    print("valor a pagar: R$",preco)
  elif (dia==1 and diam=="S"):
    total=preco+20.00
    print("valor a pagar: R$",total)
  elif (dia==2 and diam=="N"):
    total1=preco*0.25
    total=preco-total1
    print("valor a pagar: R$",total)
  elif (dia==1 and diam=="S"):
  	total=preco+20.00
	print("valor a pagar: R$",total)
  elif (dia==3 and diam=="N"):
    total1=preco*0.25
    total=preco-total1
    print("valor a pagar: R",total):
  elif (dia==3 and diam=="S")
  	total=(preco+20.00)
    print("valor a pagar: R$",total)
  elif (dia==4 and diam=="N"):
    total=preco
    print("valor a pagar: R$",preco)
  elif (dia==4 and diam=="S"):
  	total=(preco+20.00)
    print("valor a pagar: R$",total)
  elif (dia==5 and diam=="N"):
    total1=preco*0.25
    total=preco-total1
    print("valor a pagar: R$",total)
  elif (dia==5 and diam=="S"):
  	total=(preco+20.00)
    print("valor a pagar: R$",total)
  elif (dia==6 and diam=="S"):
  	total=(preco+20.00)
    print("valor a pagar: R$",total)
  elif (dia==6 and diam=="S"):
  	total=(preco+20.00)
    print("valor a pagar: R$",total)
  elif (dia==7 and diam=="S"):
  	total=(preco+20.00)
    print("valor a pagar: R$",total)
  elif (dia==7 and diam=="S"):
  	total=(preco+20.00)
    print("valor a pagar: R$",total)
else:
  print()