#ENTRADA DE DADOS
x = int (input("Digite qtd ini: "))
d = int (input("Digite despesa mensal: "))
m = int (input("Digite moedas coletadas: "))
r = int (input("Digite qtd roubada: "))
#CONSTANTES
meses = 0
renda = x
roubado = (r + d)
#LACO E CONDICAO PARADA
while (renda > 0) :
	renda = renda + m - roubado
	meses = meses + 1
print (meses)