varia = input("Digite C para coxinha e E para esfirra: ")
q1 = int(input("Qual a quantidade de coxinhas ou esfirras: "))
q2 = int(input("Qual a quantidade de sucos: "))


c = 2
e = 4.5
s = 6

if varia == "C":
	var = (q1 * c) + (q2 * s)
	
else:
	var = (q1 * e) + (q2 * s)

print(round(var, 2))