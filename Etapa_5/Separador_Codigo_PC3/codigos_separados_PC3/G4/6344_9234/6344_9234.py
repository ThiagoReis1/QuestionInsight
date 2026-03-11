from numpy import*

name = input("digite your name: ")

if len(name) >= 5 and (name[4].lower()=='c'):
	print(name.upper())
else:
	
	print("nome invalido")
	