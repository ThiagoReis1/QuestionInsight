ler = input("respostas dos clientes: ")

i = 0
k = 0

while (ler.upper() != "S"):
	k = k + 1
	if (ler.upper() == "SIM"):
		i = i + 1
	ler = input("respostas dos clientes: ")
print(round(k))	
print(round((i / k)* 100, 2))
