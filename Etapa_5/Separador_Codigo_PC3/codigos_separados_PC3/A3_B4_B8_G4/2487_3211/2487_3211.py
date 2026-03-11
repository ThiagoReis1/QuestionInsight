p=int(input())
s=int(input())
b=int(input())

p1=180
p2=230
p3=250
p4=350
s1=75
s2=110
s3=170
s4=200
b1=20
b2=70
b3=100
b4=65

print("Entradas: ",p," , ",s," , ",b)

if(1>p>4)or(1>s>4)or(1>b>4):
	print("Dados invalidos")
elif(p==1)and(s==1)and(b==1):
	x=p1+s1+b1
	print("Calorias: ",x," cal")
elif(p==1)and(s==1)and(b==2):
	x=p1+s1+b2
	print("Calorias: ",x," cal")
elif(p==1)and(s==1)and(b==3):
	x=p1+s1+b3
	print("Calorias: ",x," cal")
elif(p==1)and(s==1)and(b==4):
	x=p1+s1+b4
	print("Calorias: ",x," cal")
elif(p==1)and(s==2)and(b==1):
	x=p1+s2+b1
	print("Calorias: ",x," cal")
elif(p==1)and(s==2)and(b==2):
	x=p1+s2+b2
	print("Calorias: ",x," cal")
elif(p==1)and(s==2)and(b==3):
	x=p1+s2+b3
	print("Calorias: ",x," cal")
elif(p==1)and(s==2)and(b==4):
	x=p1+s1+b1
	print("Calorias: ",x," cal")
elif(p==1)and(s==3)and(b==1):
	x=p1+s3+b1
	print("Calorias: ",x," cal")
elif(p==1)and(s==3)and(b==2):
	x=p1+s3+b2
	print("Calorias: ",x," cal")
elif(p==1)and(s==3)and(b==3):
	x=p1+s3+b3
	print("Calorias: ",x," cal")
elif(p==1)and(s==3)and(b==4):
	x=p1+s3+b4
	print("Calorias: ",x," cal")
elif(p==1)and(s==4)and(b==1):
	x=p1+s4+b1
	print("Calorias: ",x," cal")
elif(p==1)and(s==4)and(b==2):
	x=p1+s4+b2
	print("Calorias: ",x," cal")
elif(p==1)and(s==4)and(b==3):
	x=p1+s4+b3
	print("Calorias: ",x," cal")
elif(p==1)and(s==4)and(b==4):
	x=p1+s4+b4
	print("Calorias: ",x," cal")
elif(p==2)and(s==1)and(b==1):
	x=p2+s1+b1
	print("Calorias: ",x," cal")
elif(p==2)and(s==1)and(b==2):
	x=p2+s1+b2
	print("Calorias: ",x," cal")
elif(p==2)and(s==3)and(b==3):
	x=p2+s1+b1
	print("Calorias: ",x," cal")