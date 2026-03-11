from numpy import*
notas=array(eval(input("digite as notas: ")))
i=0
while(i < size(notas) ):
	NotaFinal = (notas[0] * 5.0 + notas[1] * 3.0 + notas[2] * 2.0) / 10.0
	i=i+1
if( NotaFinal > 5):
	print(round(NotaFinal,2))
	print("APROVADO")
else:
	print(round(NotaFinal,2))
	print("REPROVADO")