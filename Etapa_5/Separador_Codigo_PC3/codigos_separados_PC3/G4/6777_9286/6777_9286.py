a = int(input("Ano de nascimento:"))
p = input("Pais de origem(B ou I):").upper()
m = 2023 - a
if (m>=18) and (p=='B'):
	t = m - 18 
	print("sim")
	print(t)
elif (m>=17) and (p=='I'):
	t = 17-m
	print("sim")
	print(t)
elif(m<18) and (p=='B'):
	t = 18 - m 	
	print("nao")
	print(t)
elif (m<17) and (p=='I'):
	t = 17 - m
	print("nao")
	print(t)
else: 
	print("invalido")

