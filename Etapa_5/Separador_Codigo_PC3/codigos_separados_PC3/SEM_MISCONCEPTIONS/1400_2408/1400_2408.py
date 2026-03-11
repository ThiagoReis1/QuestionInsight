tipo_de_ataque= input()
numero_de_rodadas= int(input())
dado1= int(input())
dado2= int(input()) 
n=dado1 + dado2
if(tipo_de_ataque == "constricao"):
	constricao = (n +1) *numero_de_rodadas
	print(constricao)
else:
	polen =(dado1 * dado2)
	print(polen)