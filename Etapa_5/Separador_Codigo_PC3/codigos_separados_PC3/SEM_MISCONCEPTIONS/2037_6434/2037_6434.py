idade =int(input("Imforme sua idade: "))
i = 0

while(idade != -1):
	if( idade < 18):
		i = i+1
		
	idade = int(input("Informe sua idade: "))
print(i)	