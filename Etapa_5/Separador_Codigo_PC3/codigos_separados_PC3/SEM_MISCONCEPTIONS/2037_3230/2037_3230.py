menores = 0 
idade = int(input("Digite a idade:"))

while(idade != -1):
	if(idade < 18):
		menores = menores + 1
	idade = int(input("Digite a idade:"))
print(menores)
