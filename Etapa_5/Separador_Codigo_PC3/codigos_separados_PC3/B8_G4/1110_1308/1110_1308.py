x=int(input("Digite o prato:"))
y=int(input("Digite a sobremesa:"))
z=int(input("Digite a bebida:"))
print("Entradas:",x,",",y,",",z)
if x==1:
    p=180
elif x==2:
    p=230
elif x==3:
    p=250
elif x==4:
    p=350
if y==1:
    s=75
elif y==2:
    s=110
elif y==3:
    s=170
elif y==4:
    s=200
if z==1:
    b=20
elif z==2:
    b=70
elif z==3:
    b=100
elif z==4:
    b=65
if (x==4 or x==3 or x==2 or x==1) and (y==4 or y==3 or y==2 or y==1) and (z==4 or z==3 or z==2 or z==1):
   total=p+s+b    
   print("Calorias: ",total," cal")   
else:
   print("Dados invalidos")