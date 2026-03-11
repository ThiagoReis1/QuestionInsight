#Instituto de Computacao - UFAM
#LAb 02
#02/04/2018

#hertz = 1 segundo
#cameras: fm = 30 Hz
#sensoes: fm = 20 Hz 

#LEIA: FREQUENCIA DO SENSOR E TEMPO DE COLETA MINUTOS
fs = int(input("Digite a frequencia do sensor: "))
t = int(input("Digite o tempo em minutos: "))

#f = quantidade de amostras/ 1 segundo

qa = fs * (t * 60)

#saida: quantidade de amostras
print(qa)








