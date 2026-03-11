alimento = input("tapioca(T) ou salgado(S) : ")
quantidade = int(input(" quantidade : "))
acai = int(input("quantos acai : "))

if alimento == "T" :
	print(quantidade*5.5 + acai*10)
else :
	print(quantidade*4 + acai*10)