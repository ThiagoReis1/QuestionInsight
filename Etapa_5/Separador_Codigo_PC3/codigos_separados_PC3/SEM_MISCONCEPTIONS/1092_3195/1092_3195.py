numero=int(input())
d1=numero//100
d2=(numero//10)%10
d3=numero%10
x=(d1**3+d2**3+d3**3)
if x==numero:
	mensagem="atende"
	print(numero,mensagem)
	
else:
	mensagem="nao atende"
	print(numero,mensagem)
	
