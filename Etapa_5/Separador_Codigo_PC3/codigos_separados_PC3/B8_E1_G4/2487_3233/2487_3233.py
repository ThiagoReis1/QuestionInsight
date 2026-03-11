p = int(input("numero do prato: "))
s = int(input("numero da sobremesa: "))
b = int(input("numero da bebida: "))

if (p<1 or p>4 or s<1 or s>4 or b<1 or b>4):
	print("Entradas: ", p, ", ", s, ", ", b)
	print("Dados invalidos")
elif(p==1):
   cp = 180
elif(p==2):
   cp = 230
elif(p==3):
   cp = 250
elif(p==4):
   cp = 350
if(s==1):
   cs = 75
elif(s==2):
   cs = 110
elif(s==3):
   cs = 170
elif(s==4):
   cs = 200
if(b==1):
   cb = 20
elif(b==2):
   cb = 70
elif(b==3):
   cb = 100
elif(b==4):
   cb = 65
c = cp + cs + cb
print("Entradas: ", p, ", ", s, ", ", b)
print("Calorias: ", c, "cal")
	