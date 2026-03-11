g = input(" ")
o = 15.9994
c = 12.011
n = 14.0067
h = 1.00794
ami = "GLUTAMINA"

if(g.upper() == ami):
	mensagem = 5*c + 8*h + 1*n + 4*o
else:
   mensagem = 4*c + 9*h +1*n + 3*o	

print(round(mensagem,2))
