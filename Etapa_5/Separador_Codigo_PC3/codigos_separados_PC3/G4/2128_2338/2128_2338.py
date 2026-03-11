from numpy import*

me = eval(input("digite um valor: "))

mf= (sum(me)-max(me))/3
print(round(mf,2))

if (mf >= 50):
	print("APROVADO")
else:
	print("REPROVADO")