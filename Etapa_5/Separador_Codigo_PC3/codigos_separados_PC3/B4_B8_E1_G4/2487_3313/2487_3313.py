x = int(input("prato: "))
y = int(input("sobremesa: "))
z = int(input("bebida: "))
p1 = 180
s1 = 75
b1 = 20
p2 = 230
s2 = 110
b2 = 70
p3 = 250
s3 = 170
b3 = 100
p4 = 350
s4 = 200 
b4 = 65
print("Entradas:",x,",",y,",",z)
if(x<1)or(x>4)or(y<1)or(y>4)or(z<1)or(z>4):
	print("Dados invalidos")
elif(x==1)and(y==1)and(z==1):
	n = p1+s1+b1
	print("Calorias:",n,"cal")
elif(x==2)and(y==2)and(z==2):
	n = p2+s2+b2
	print("Calorias:",n,"cal")
elif(x==3)and(y==3)and(z==3):
	n = p3+s3+b3
	print("Calorias:",n,"cal")
elif(x==4)and(y==4)and(z==4):
	n = p4+s4+b4
	print("Calorias:",n,"cal")
elif(x==1)and(y==1)and(z==2):
	n = p1+s1+b2
	print("Calorias:",n,"cal")
elif(x==1)and(y==1)and(z==3):
	n = p1+s1+b3
	print("Calorias:",n,"cal")
elif(x==1)and(y==1)and(z==4):
	n = p1+s1+b4
	print("Calorias:",n,"cal")
elif(x==1)and(y==2)and(z==1):
	n = p1+s2+b1
	print("Calorias:",n,"cal")
elif(x==1)and(y==2)and(z==2):
	n = p1+s2+b2
	print("Calorias:",n,"cal")
elif(x==1)and(y==2)and(z==3):
	n = p1+s2+b3
	print("Calorias:",n,"cal")
elif(x==1)and(y==2)and(z==4):
	n = p1+s2+b3
	print("Calorias:",n,"cal")
elif(x==1)and(y==3)and(z==1):
	n = p1+s3+b1
	print("Calorias:",n,"cal")
elif(x==1)and(y==3)and(z==2):
	n = p1+s3+b2
	print("Calorias:",n,"cal")	
elif(x==1)and(y==3)and(z==3):
	n = p1+s3+b3
	print("Calorias:",n,"cal")
elif(x==1)and(y==3)and(z==4):
	n = p1+s3+b4
	print("Calorias:",n,"cal")
elif(x==1)and(y==4)and(z==1):
	n = p1+s4+b1
	print("Calorias:",n,"cal")
elif(x==1)and(y==4)and(z==2):
	n = p1+s4+b2
	print("Calorias:",n,"cal")
elif(x==1)and(y==4)and(z==3):
	n = p1+s4+b3
	print("Calorias:",n,"cal")
elif(x==1)and(y==4)and(z==4):
	n = p1+s4+b4
	print("Calorias:",n,"cal")	
elif(x==2)and(y==1)and(z==1):
	n = p2+s1+b1
	print("Calorias:",n,"cal")
elif(x==2)and(y==1)and(z==2):
	n = p2+s1+b2
	print("Calorias:",n,"cal")
elif(x==2)and(y==1)and(z==3):
	n = p2+s1+b3
	print("Calorias:",n,"cal")
elif(x==2)and(y==1)and(z==4):
	n = p2+s1+b4
	print("Calorias:",n,"cal")
elif(x==2)and(y==2)and(z==1):
	n = p2+s2+b1
	print("Calorias:",n,"cal")
elif(x==2)and(y==2)and(z==3):
	n = p2+s2+b3
	print("Calorias:",n,"cal")
elif(x==2)and(y==2)and(z==4):
	n = p2+s2+b4
	print("Calorias:",n,"cal")
elif(x==2)and(y==3)and(z==1):
	n = p2+s3+b1
	print("Calorias:",n,"cal")
elif(x==2)and(y==3)and(z==2):
	n = p2+s3+b2
	print("Calorias:",n,"cal")
elif(x==2)and(y==3)and(z==3):
	n = p2+s3+b3
	print("Calorias:",n,"cal")
elif(x==2)and(y==3)and(z==4):
	n = p2+s3+b4
	print("Calorias:",n,"cal")
elif(x==2)and(y==4)and(z==1):
	n = p2+s4+b1
	print("Calorias:",n,"cal")
elif(x==2)and(y==4)and(z==2):
	n = p2+s4+b2
	print("Calorias:",n,"cal")
elif(x==2)and(y==4)and(z==3):
	n = p2+s4+b3
	print("Calorias:",n,"cal")
elif(x==2)and(y==4)and(z==4):
	n = p2+s4+b4
	print("Calorias:",n,"cal")
elif(x==3)and(y==1)and(z==1):
	n = p3+s1+b1
	print("Calorias:",n,"cal")
elif(x==3)and(y==1)and(z==2):
	n = p3+s1+b2
	print("Calorias:",n,"cal")
elif(x==3)and(y==1)and(z==3):
	n = p3+s1+b3
	print("Calorias:",n,"cal")
elif(x==3)and(y==1)and(z==4):
	n = p3+s1+b4
	print("Calorias:",n,"cal")
elif(x==3)and(y==2)and(z==1):
	n = p3+s2+b1
	print("Calorias:",n,"cal")
elif(x==3)and(y==2)and(z==2):
	n = p3+s2+b2
	print("Calorias:",n,"cal")
elif(x==3)and(y==2)and(z==3):
	n = p3+s2+b3
	print("Calorias:",n,"cal")
elif(x==3)and(y==2)and(z==4):
	n = p3+s2+b4
	print("Calorias:",n,"cal")
elif(x==3)and(y==3)and(z==1):
	n = p3+s3+b1
	print("Calorias:",n,"cal")
elif(x==3)and(y==3)and(z==2):
	n = p3+s3+b2
	print("Calorias:",n,"cal")	
elif(x==3)and(y==3)and(z==4):
	n = p3+s3+b4
	print("Calorias:",n,"cal")
elif(x==3)and(y==4)and(z==1):
	n = p3+s4+b1
	print("Calorias:",n,"cal")
elif(x==3)and(y==4)and(z==2):
	n = p3+s4+b2
	print("Calorias:",n,"cal")
elif(x==3)and(y==4)and(z==3):
	n = p3+s4+b3
	print("Calorias:",n,"cal")
elif(x==3)and(y==4)and(z==4):
	n = p3+s4+b4
	print("Calorias:",n,"cal")
elif(x==4)and(y==1)and(z==1):
	n = p4+s1+b1
	print("Calorias:",n,"cal")
elif(x==4)and(y==1)and(z==2):
	n = p4+s1+b2
	print("Calorias:",n,"cal")
elif(x==4)and(y==1)and(z==3):
	n = p4+s1+b3
	print("Calorias:",n,"cal")
elif(x==4)and(y==1)and(z==4):
	n = p4+s1+b4
	print("Calorias:",n,"cal")
elif(x==4)and(y==2)and(z==1):
	n = p4+s2+b1
	print("Calorias:",n,"cal")
elif(x==4)and(y==2)and(z==2):
	n = p4+s2+b2
	print("Calorias:",n,"cal")
elif(x==4)and(y==2)and(z==3):
	n = p4+s2+b3
	print("Calorias:",n,"cal")
elif(x==4)and(y==2)and(z==4):
	n = p4+s2+b4
	print("Calorias:",n,"cal")
elif(x==4)and(y==3)and(z==1):
	n = p4+s3+b1
	print("Calorias:",n,"cal")
elif(x==4)and(y==3)and(z==2):
	n = p4+s3+b2
	print("Calorias:",n,"cal")
elif(x==4)and(y==3)and(z==3):
	n = p4+s3+b3
	print("Calorias:",n,"cal")
elif(x==4)and(y==3)and(z==4):
	n = p4+s3+b4
	print("Calorias:",n,"cal")
elif(x==4)and(y==4)and(z==1):
	n = p4+s4+b1
	print("Calorias:",n,"cal")
elif(x==4)and(y==4)and(z==2):
	n = p4+s4+b2
	print("Calorias:",n,"cal")
elif(x==4)and(y==4)and(z==3):
	n = p4+s4+b3
	print("Calorias:",n,"cal")