a = input("Digite o nome do aminoácido ").lower()


aspartato = 4 * 12.011 + 6 * 1.0079 + 14.0067 + 4 * 15.9994
fenilalanina = 9 * 12.011 + 11 * 1.0079 + 2 * 15.9994 + 32.066
tirosina = 9 * 12.011 + 11 * 1.0079 + 14.0067 + 3 * 15.9994

if(a == "aspartato"):
	print(round(aspartato,2))
elif(a == "fenilalanina"):
	print(round(fenilalanina,2))
elif(a == "tirosina"):
	print(round(tirosina,2))
	
else:
	print("Entrada:", a)
	print("Dado Invalido")