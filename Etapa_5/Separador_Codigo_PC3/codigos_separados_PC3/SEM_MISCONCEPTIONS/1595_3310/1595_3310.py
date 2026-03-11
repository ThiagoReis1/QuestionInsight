#MEDIA = MEDIA DAS NOTAS DO TRAB
# EXCETO A MENOR NOTA
#
from numpy import*
notas = array(eval(input("Digte a nota: ")))



media = (sum(notas)-min(notas))/(size(notas)-1)

print(round(media,2))











