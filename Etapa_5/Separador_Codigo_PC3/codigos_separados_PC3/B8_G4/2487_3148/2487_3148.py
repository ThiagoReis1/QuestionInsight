p=int(input())
s=int(input())
b=int(input())

print("Entradas",p,',',s,',',b)

if(1>p>4):
	if(p==1):
		x1=180
	elif(p==2):
		x1=230
	elif(p==3):
		x1=250
	elif(p==4):
		x1=350
else:
	print("Dados invalidos")
if(1>s>4):
	if(s==1):
		x2=180
	elif(s==2):
		x2=230
	elif(s==3):
		x2=250
	elif(s==4):
		x2=350
else:
	print("Dados invalidos")
if(1>b>4):
	if(b==1):
		x3=180
	elif(b==2):
		x3=230
	elif(b==3):
		x3=250
	elif(b==4):
		x3=350
else:
	print("Dados invalidos")
w= x1 + x2 +x3
print(w)
	
		

