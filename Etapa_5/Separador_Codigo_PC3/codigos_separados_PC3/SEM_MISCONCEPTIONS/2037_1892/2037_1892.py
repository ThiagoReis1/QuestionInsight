idade = int(input("Idade das pessoas: "))
i = 0
total = 0
while(idade != -1):
	idade = int(input("Idade das pessoas: "))
	if(idade >= 18):
		i = i + 1
	else:
		total = idade - total
		i = i + 1
print(i)
		
		

	