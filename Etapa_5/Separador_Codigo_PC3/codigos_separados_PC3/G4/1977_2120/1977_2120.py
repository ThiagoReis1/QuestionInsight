#start!

gen = input("Qual o genero da serie?")
sub = input("Qual o subgenero da serie?")

if(gen == "Investigativa" and sub == "Suspense"):
	print("DEXTER")
elif(gen == "Investigativa" and sub == "Drama"):
	print("NARCOS")
elif(gen == "Dramatica" and sub == "COM FICCAO"):
	print("LOST")
elif(gen == "Dramatica" and sub == "Aventura"):
	print("SHERLOCK")
else:
	print("SERIE NAO IDENTIFICADA")