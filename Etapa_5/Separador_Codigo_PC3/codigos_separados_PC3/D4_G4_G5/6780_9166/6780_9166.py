ano_consulta = 2023
minimo_brasil = 21
minimo_china = 24

def idade_minima(a: int, p: str) -> str:
	idade = ano_consulta - a
	# BRASIL ------------------------------------
	if (p == "B" and idade < 21):
		print("nao")
		print(minimo_brasil - (ano_consulta - a))
		
	elif (p == "B" and idade >= 21):
		print("sim")
		print((ano_consulta - a) - minimo_brasil)
	# CHINA --------------------------------------
	elif (p == "C" and idade < 24):
		print("nao")
		print(minimo_china - (ano_consulta - a))
		
	elif (p == "C" and idade >= 24):
		print("sim")
		print((ano_consulta - a) - minimo_china)
	# NENHUM -------------------------------------
	else:
		print("invalido")
		
if __name__ == "__main__":
	ano_nascimento = int(input(""))
	pais_nascimento = input("").upper()
	
	idade_minima(ano_nascimento, pais_nascimento)