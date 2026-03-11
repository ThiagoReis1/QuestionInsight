
s=input("insira:")
vogal=0
consoante=0
for i in s:
	if(i=="a"):
		vogal=vogal+1
	elif(i=="e"):
		vogal=vogal+1
	elif(i=="i"):
		vogal=vogal+1
	elif(i=="o"):
		vogal=vogal+1
	elif(i=="u"):
		vogal=vogal+1
	else:
		consoante=consoante+1
print(vogal)
print(consoante)