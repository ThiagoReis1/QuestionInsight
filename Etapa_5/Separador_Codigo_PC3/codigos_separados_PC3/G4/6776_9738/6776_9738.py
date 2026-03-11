ano= int(input())
pais= input().upper()

idade= 2023 - ano

if pais == "B"  :
	if idade >= 18:
		i=idade-18
		print("sim")
		print(i)
	else:
		i=18 - idade
		print("nao")
		print(i)
		
elif pais == "R":
	if idade >= 17:
		i= idade - 17
		print("sim")
		print(i)
	else:
		i= 17 - idade
		print("nao")
		print(i)
		
else:
   print("invalido")
