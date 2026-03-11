Ent= input("Qual a unidade em que a medida esta?")
V= float (input("Qual o valor da medida?"))


A=  2.47105 * V
H= V/2.47105

if (Ent=="A"):
	print(round(H,2))

else:
	print (round(A,2))