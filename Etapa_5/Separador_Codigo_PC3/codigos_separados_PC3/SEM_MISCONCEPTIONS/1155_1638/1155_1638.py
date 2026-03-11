nc = int(input("numero de copias iniciais: "))
nl = int(input("numero inicial de leucocitos: "))
tx = float(input("numero taxa de multiplicação: "))
tx1 = float(input("numero taxa de leuucocitos: "))
tempo = 0
virus = nc
leucocitos = nl
mv = tx*0.01
ml = tx1*0.01
cont = 1

while(nl == 2*nc):
	conta = virus*mv + leucocitos*ml
	tempo = tempo + conta
	cont = cont + 1
print(tempo)