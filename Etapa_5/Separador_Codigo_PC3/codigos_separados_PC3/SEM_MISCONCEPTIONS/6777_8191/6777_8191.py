x = int(input("Digite um ano: "))
y = input("Digite uma letra: ")
p = 2023 - x

if y == "B" :
	if p >= 18 :
		print("sim")
		print(p - 18)
	if p < 18:
		print("nao")
		print(18 - p)
	if y == "I" :
		if p >= 17 :
		print("sim")
		print(p - 17)
	if p < 17 :
		print("nao")
		print(17 - p)
else: 
		print("invalido")






