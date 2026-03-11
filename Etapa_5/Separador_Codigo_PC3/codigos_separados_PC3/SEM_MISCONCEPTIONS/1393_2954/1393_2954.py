p=float(input())

if(p<=4999.9):
  mensagem=0.05*p
else:
  mensagem=(0.04*p)+60.0
	
print(round(mensagem,2))