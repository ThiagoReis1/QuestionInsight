x=float(input("preco normal:"))
y=int(input("dia:(1,2,3,4,5,6,7)"))
z=input("dia de musica ao vivo?")
print("Entradas:",x,",",y,",",z)


if(x>=0 and y>=1 and y<8 and z=="S" or z=="N"):
      if(y==2 and z=="N"):
                w=round(x*0.25,2)
                print("Valor a pagar: R$",w)
      elif(y==3 and z=="N"):
                w=round(x*0.25,2)
                print("Valor a pagar: R$",w)
      elif(y==5 and z=="N"):
					  w=round(x*0.25,2)
					  print("Valor a pagar: R$",w)
      elif(y==2 and z=="S"):
						 a=x*0.25
						 w=round((x-a)+20,2)
						 print("Valor a pagar: R$",w)
      elif(y==3 and z=="S"):
						  a=x*0.25
						  w=round((x-a)+20,2)
						  print("Valor a pagar: R$",w) 
      elif(y==5 and z=="S"):
						  a=x*0.25
						  w=round((x-a)+20,2)
						  print("Valor a pagar: R$",w)
      elif(y==1 and z=="N"):
						  w=round(x,2)
						  print("Valor a pagar: R$",w)
      elif(y==4 and z=="N"):
						  w=round(x,2)
						  print("Valor a pagar: R$",w)
      elif(y==6 and z=="N"):
						  w=round(x,2)
						  print("Valor a pagar: R$",w)
      elif(y==7 and z=="N"):
						  w=round(x,2)
						  print("Valor a pagar: R$",w)
      elif(y==1 and z=="S"):
						  w=round(x+20,2)
						  print("Valor a pagar: R$",w)
      elif(y==4 and z=="S"):
						  w=round(x+20,2)
						  print("Valor a pagar: R$",w)
      elif(y==6 and z=="S"):
						  w=round(x+20,2)
						  print("Valor a pagar: R$",w)
      elif(y==7 and z=="S"):
						  w=round(x+20,2)
						  print("Valor a pagar: R$",w)      
else:
	print("Dados invalidos")
