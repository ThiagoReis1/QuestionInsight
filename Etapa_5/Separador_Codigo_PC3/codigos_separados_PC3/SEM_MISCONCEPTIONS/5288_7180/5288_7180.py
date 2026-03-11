num = int(input("Idade: "))
idade = 0
menor = 0


while (num !=-1):	
	idade = idade + 1
	if(num<18):
		menor = menor + 1

	num = int(input("Idade: "))
	
print (idade)
print(round(100*menor/idade,2))

