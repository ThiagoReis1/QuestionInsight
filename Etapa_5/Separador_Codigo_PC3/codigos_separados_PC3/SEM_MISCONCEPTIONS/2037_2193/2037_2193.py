idade = int(input(""))
menor = 0
while (idade != -1):
	if (idade < 18):
		menor = menor + 1
	idade = int(input(""))
print(menor)