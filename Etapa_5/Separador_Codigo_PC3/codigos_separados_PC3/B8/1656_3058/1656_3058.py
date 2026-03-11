from numpy import*
s= input("Digite o vetor com origem das pessoas: ").upper().split(",")
soma= 0
soma1= 0
soma2= 0
soma3= 0
soma4= 0

for i in range(len(s)):
	if(s[i]== "BE"):
		soma= soma + 1
	elif(s[i]== "ES"):
		soma1= soma1 + 1
	elif(s[i]== "FR"):
		soma2= soma2 + 1
	elif(s[i]== "IT"):
		soma3= soma3 + 1
	elif(s[i]== "PT"):
		soma4= soma4 + 1
soma5= [soma, soma1, soma2, soma3, soma4]
print(max(soma5))

v0= zeros(5, dtype= int)
for i in range(len(s)):
	if(s[i]== "BE"):
		v0[0]= v0[0] + 1
	elif(s[i]== "ES"):
		v0[1]= v0[1] + 1
	elif(s[i]== "FR"):
		v0[2]= v0[2] + 1
	elif(s[i]== "IT"):
		v0[3]= v0[3] + 1
	elif(s[i]== "PT"):
		v0[4]= v0[4] + 1
print(v0)


	
		
	
	