from numpy import*
etiq = input(": ").upper()
custo = 0
for caractere in etiq:
	if caractere in "AEIOU":
		custo += 0.25
	else:
		custo += 0.27
print(round(custo,2))