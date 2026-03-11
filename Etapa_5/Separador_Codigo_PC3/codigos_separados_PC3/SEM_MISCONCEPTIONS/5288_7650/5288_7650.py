idade = int(input("Idade: "))

menor = 0
total = 0

while(idade != -1):
	if(idade < 18):
		menor = menor + 1
	total = total + 1
	idade = int(input("Idade: "))
print(total)
print(round(menor / total * 100 , 2))