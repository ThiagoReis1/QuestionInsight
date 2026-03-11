#Aluno PAtrick Chessmam
#Matricula 21200931
#1 Avaliação
#16.06.2016


consumo = float(input("Digite o consumo do mes: "))
taxafix = 10.00
#formula conta
conta = 0.43 * consumo + taxafix

icms = conta * 0.25

total = conta + icms
print(round(total,2))
