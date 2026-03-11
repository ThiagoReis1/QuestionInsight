aminoacido = input("qual o aminoacido desejado?")

O = 15.9994
C = 12.011
N = 14.0067
S = 32.066
H = 1.00794

peso_molecular1 = ((4*C) + (6*H) + (N) + (4*O))
peso_molecular2 = ((3*C) + (7*H) + (N) + (2*O) + (S))

if (aminoacido == "aspartato".lower()):
	print(round(peso_molecular1, 2))

elif (aminoacido == "cisteina".lower()):
	print(round(peso_molecular2, 2))