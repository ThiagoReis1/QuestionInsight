nome_do_aminoacido = input("ASPARATO ou CISTEINA: ").lower()

O = 15.9994
C = 12.011
N = 14.0067
S = 32.066
H = 1.00794

aspartato = ((C*4)+(H*6)+N+(O*4)) 


if (nome_do_aminoacido == "aspartato"):
	print (round(aspartato, 2))
else:
	cisteina = ((C*3)+(H*7)+N+(O*2)+S)
	print (round(cisteina, 2))