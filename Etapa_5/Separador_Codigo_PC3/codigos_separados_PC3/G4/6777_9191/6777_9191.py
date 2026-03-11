N=int(input("numero inteiro:"))
P=input("B/I?:").upper()

x=2023-N
if P=="I":
	if x>=17:
		print("sim")
		y=(2023-N)-17
		print(y)
	else:
		print("nao")
		y=17-(2023-N)
		print(y)
elif P=="B":
	if x>=18:
		print("sim")
		y=(2023-N)-18
		print(y)
	else:
		print("nao")
		y=18-(2023-N)
		print(y)
else:
		print("invalido")