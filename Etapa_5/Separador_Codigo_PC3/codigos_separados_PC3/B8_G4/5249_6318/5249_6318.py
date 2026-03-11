p=int(input())
s=int(input())
b=int(input())

cal=0

if(p>0 and p<5) and (s>0 and s<5) and (b>0 and b<5):
	if(p==1):
		cal= cal  + 180
	elif(p==2):
		cal= cal + 230
	elif(p==3):
		cal= cal + 250
	elif(p==4):
		cal= cal + 350
	if(s==1):
		cal= cal + 75
	elif(s==2):
		cal= cal + 110
	elif(s==3):
		cal= cal + 170
	elif(s==4):
		cal = cal + 200
	if(b==1):
		cal = cal + 20
	elif(b==2):
		cal = cal + 70
	elif(b==3):
		cal = cal + 100
	elif(b==4):
		cal = cal + 65
		
	print("Calorias:",cal,"cal")
else:
	print("Dados invalidos")