ano=int(input())
pais= input().upper()
if pais=='B':
	total= (2023-ano)
	if total>=18:
		print("sim")
		print(total-18)
	else:
		print("nao")
		print(18-total)
elif pais=='J':
	total=(2023-ano)
	if total>=16:
		print("sim")
		print(total-16)
	else:
		print("nao")
		print(16-total)
else:
	print("invalido")
