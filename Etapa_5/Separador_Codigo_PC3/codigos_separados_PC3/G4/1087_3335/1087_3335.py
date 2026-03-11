n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())

ma = (n1+n2+n3+n4)/4
mf = round(ma,2)
if(mf >= 7.0):
	m = "Aprovado"
else:
	m = "Reprovado"
print(mf)
print(m)