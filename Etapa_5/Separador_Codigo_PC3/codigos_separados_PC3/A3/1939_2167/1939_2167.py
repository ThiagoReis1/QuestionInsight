aminoacido = str(input("nome do aminoacido "))
o = 15.999
c = 12.011
n = 14.00674
h = 1.00794

if (aminoacido == "asparagina"):
	mensagem = ((c * 4) + (h * 8) + (n * 2) + (o * 3))
	
if (aminoacido == "triptofano"):
	mensagem = ((c * 11) + (h * 11) + (n * 2) + (o * 2))
	
print(round(mensagem, 2))
	
	

