# faça seu código aqui!
string = input("Ler string: " ).upper()

i = 0
cont = 0

while i < len(string):
	if string[i] == "E":
		cont = cont +1
		
	i = i + 1	
				
print(cont)