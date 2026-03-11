from math import*
#UNIVERSIDADE FEDERAL DO AMAZONAS
#ALUNA: LARISSA MAGNO LEAO
#MATRÍCULA:21551610
#EXERCICIO 2

volume= float(input("Digite o volume de agua:"))
conta=0.37* volume + 15.0
conta_com_icms= conta + 0.35* conta

print(round(conta_com_icms,2))