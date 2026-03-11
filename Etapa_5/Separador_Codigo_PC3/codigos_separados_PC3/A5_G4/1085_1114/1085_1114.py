import math
n1 = float(input("Digite o valor da nota 1: "));
n2 = float(input("Digite o valor da nota 2: "));
n3 = float(input("Digite o valor da nota 3: "));
n4 = float(input("Digite o valor da nota 4: "));
n5 = float(input("Digite o valor da nota 5: "));
media = (n1 + n2 + n3 + n4 + n5) / 5
if(media >= 6.0):
	print(round(media,2));	
	print("Aprovado");
else:
	print(round(media,2));
	print("Reprovado")