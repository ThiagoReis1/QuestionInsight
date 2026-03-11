HP0 = int(input())
D1 = int(input())
D2 = int(input())
D3 = int(input())

HP = HP0 - 10 * (D1 + D2 + D3)

if (HP > 0):
	print(HP)
	print("VIVO")
else:
	HP = 0
	print(HP)
	print("MORTO")