gen = input("qual o genero da serie: ")
sub = input("qual o subgenero da serie: ")

if(gen=="Investigativa" and sub=="Suspense"):
	print("dexter".upper())
elif(gen=="Investigativa" and sub=="Drama"):
	print("narcos".upper())
elif(gen=="Dramatica" and sub=="Com ficcao"):
	print("lost".upper())
elif(gen=="Dramatica" and sub=="Aventura"):
	print("sherlock".upper())
else:
	print("SERIE NAO IDENTIFICADA")