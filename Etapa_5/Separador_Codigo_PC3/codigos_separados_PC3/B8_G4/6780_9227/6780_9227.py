x = int(input("ano de nascimento:"))
p = input("pais que nasceu? B ou C:")
if p.upper()== "B" and 2023 - x >= 21:
	print("sim")
	print(2023 - x - 21 )
elif p.upper()== "C" and 2023 - x >= 24:
	print("sim")
	print( 2023 - x - 24)
elif p.upper()== "B" and 2023 - x < 21:
	print("nao")
	print(x - 2023 + 21 )
elif p.upper()== "C" and 2023 - x < 24:
	print("nao")
	print( x - 2023 + 24 )
elif p.upper != "B" or "C":
	print("invalido")