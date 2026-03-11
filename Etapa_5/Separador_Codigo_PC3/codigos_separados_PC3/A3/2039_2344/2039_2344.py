sg= input("Digite uma sequencia genetica:").upper()
Adenina= "A"
Guanina= "G"
Citosina= "C"
Timina= "T"

men= "A"
i= 0

while (sg != "S"):
	if (sg == "A"):
		i= i + 1
	sg= input("Digite uma sequencia genetica:").upper()
print(i)	