x= int(input())
y= int(input())
z= int(input())
print("Entradas:",x,",",y,",",z)
a=[180,230,250,350]
b=x-1

a1=[75,110,170,200]
b1=y-1

a2=[20,70,100,65]
b2=z-1

if(x>0 and y>0 and z>0):
	if(x==1 or x==2 or x==3 or x==4 and y==1 or y==2 or y==3 or y==4 and z==1 or z==2 or z==3 or z==4):
		if(x==[a] and y==[b] and z==1):
		print("Calorias:",a,"cal")
		elif(x==1 and y==1 and z==2):
			a=180+75+70
			print("Calorias",a,)
			
