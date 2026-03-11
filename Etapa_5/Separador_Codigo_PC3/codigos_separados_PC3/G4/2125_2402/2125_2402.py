from numpy import*
array(eval(input()))
np = float(input())
nt = float(input())
ns = float(input())

nf = ((np*3.0)+(nt*3.0)+(ns*4.0))/10.0

print(round(nf, 2))

if(nf>=5):
	print("APROVADO")
else:
	print("REPROVADO")