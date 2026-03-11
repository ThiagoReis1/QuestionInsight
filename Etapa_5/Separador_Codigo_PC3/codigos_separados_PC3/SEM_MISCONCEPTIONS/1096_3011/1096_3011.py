valor=int(input("Digite um numero:"))

am= valor//100000
resto_am= valor % 100000

bm=resto_am//10000
resto_bm=resto_am % 10000

cm=resto_bm // 1000
resto_cm=resto_bm % 1000

dm=resto_cm // 100
resto_dm=resto_cm % 100

em=resto_dm // 10
resto_em= resto_dm % 10

fm=resto_em // 1
calculo= (am*10+bm)**3 + (cm*10+dm)**3 + (em*10+fm)**3
if(calculo ==valor):
	mensagem="atende"
else:
	mensagem="nao atende"
print(mensagem)
print(valor)

#Questão dificil pra ca