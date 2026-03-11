#Luiz Inácio
#Av.03 Ex.01

velocidade=float(input("Digite a velocidade do trem:"))
tempo=float(input("Digite o tempo de viagem:"))

parada=velocidade*tempo

if ((velocidade<=0) or (tempo<=0)):
	print ("Entradas: %.1f km/h e %.1f h"%(velocidade,tempo))
	print ("Dados invalidos")
elif (parada<=100):
	print ("Entradas: %.1f km/h e %.1f h"%(velocidade,tempo))
	print ("Proxima parada: Castamere")
elif (parada<=300)and(parada>100):
	print ("Entradas: %.1f km/h e %.1f h"%(velocidade,tempo))
	print ("Proxima parada: Doriath")
elif (parada<=500)and(parada>300):
	print ("Entradas: %.1f km/h e %.1f h"%(velocidade,tempo))
	print ("Proxima parada: Edoras")
elif (parada<=650)and(parada>500):
	print ("Entradas: %.1f km/h e %.1f h"%(velocidade,tempo))
	print ("Proxima parada: Fangorn")
elif (parada<=1050)and(parada>650):
	print ("Entradas: %.1f km/h e %.1f h"%(velocidade,tempo))
	print ("Proxima parada: Gondor")
elif (parada>1050)and(parada<=1300):
	print ("Entradas: %.1f km/h e %.1f h"%(velocidade,tempo))
	print ("Proxima parada: Hogsmead")
elif (parada>1400):
	print ("Entradas: %.1f km/h e %.1f h"%(velocidade,tempo))
	print ("Proxima parada: Hogsmead")
else:
	print ("Entradas: %.1f km/h e %.1f h"%(velocidade,tempo))
	print ("Dados invalidos")				  