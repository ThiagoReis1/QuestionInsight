tempo = float(input("Tempo de voo: "))#entrada do tempo

if(tempo > 200):#custo com tempo superior a 200min
	piloto = 8000
	minutos_i = 100 * 200
	minutos_f = (tempo-200)*90
else:#custo com tempo inferior a 200min
	piloto = 5000
	minutos_i = 100*tempo
	minutos_f = 0
custo = (piloto + minutos_i + minutos_f)#somatorio do custo
print(custo)