alt1= float(input("qual a altura:"))
alt2 = float(input("qual a altura:"))

if(alt1 > alt2):
	maior = alt1
	
else:
	maior = alt2
	
if(alt1 < 1.37 and alt2 < 1.37):
	permissao = ("Nao")
	
else:
	permissao = ("Sim")
	
print(permissao)
print(maior)