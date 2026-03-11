a=int(input())
b=int(input())

if(b==1):
	print(round(a-(a*0.3), 2))
elif(b==2):
	print(round(a-(a*0.28), 2))
elif(b==3):
	print(round(a-(a*0.4), 2))
elif(b==4):
	print(round(a-(a*0.38), 2))
else:
	print("Regiao invalida")