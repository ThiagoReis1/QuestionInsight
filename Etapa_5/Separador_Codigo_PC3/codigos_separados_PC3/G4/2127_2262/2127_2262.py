from numpy import*
n = array(eval(input("notas das 3 avs: ")))
nf = (n[0]+n[1]+n[2]+n[3]-min(n))/3
print(round(nf, 2))
if (nf >= 50):
	print("APROVADO")
else:
	print("REPROVADO")