p= int(input("numero do prato:"))
s=int(input("numero da sobremesa: "))
b= int(input("numero da bebida: "))

print("Entradas: ",p,",",s,",",b)

if p>0 and p<=4 and s>0 and s<=4 and b>0 and b<=4:
	if p==1: 
		c1=180
	elif p==2:
		c1=230
	elif p==3:
		c1=250
	elif p==4:
		c1= 350
if	 p>0 and p<=4 and s>0 and s<=4 and b>0 and b<=4:
	if s==1: 
		c2=75
	elif s==2:
		c2=110
	elif s==3:
		c2=170
	elif s==4:
		c2= 200
if  p>0 and p<=4 and s>0 and s<=4 and b>0 and b<=4:		
	if b==1:
		c3= 20
		print("Calorias: ",c1+c2+20,"cal")
	elif b==2:
		c3= 70
		print("Calorias: ",c1+c2+70,"cal")		
	elif b==3:
		c3= 100	
		print("Calorias: ",c1+c2+100,"cal")		
	elif b==4:
		c3= 65	
		print("Calorias: ",c1+c2+65,"cal")
else:
	print("Dados invalidos")

			
	
