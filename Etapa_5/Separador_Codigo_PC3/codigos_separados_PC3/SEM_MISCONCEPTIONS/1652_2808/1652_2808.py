from numpy import*

string = input("Insira os dados:").upper().split(',')

contador = zeros(5, dtype = int)

for i in string:
	if(i == "B"):
		contador[0] = contador[0] + 1
	if(i == "PA"):
		contador[1] = contador[1] + 1
	if(i == "PR"):
		contador[2] = contador[2] + 1
	if(i == "A"):
		contador[3] = contador[3] + 1
	if(i == "I"):
		contador[4] = contador[4] + 1
		
print(max(contador[0], contador[1], contador[2], contador[3], contador[4]))
print(contador)
		

