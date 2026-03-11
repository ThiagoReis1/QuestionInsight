ar = int(input("quantidade de votos para candidato ambrosio rutra: "))
do = int(input("quantidade de votos para candidato demelza olecram: "))

#print(ar)
#print(do)

total = ar + do

#print(total)

if ar > do:
	print("Ambrosio Rutra")
else:
	print("Demelza Olecram")
	
a = ar * 100 / total
b = do * 100 / total

if a > b:
	print(round(a,2))
else:
	print(round(b,2))
