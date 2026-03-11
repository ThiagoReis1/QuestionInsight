peso_tripulante=(float(input("peso do tripulante ")))
if (peso_tripulante<3400):
	zylium=(0.8*peso_tripulante)
elif (peso_tripulante<3900):
	zylium=(1.3*peso_tripulante)
elif (peso_tripulante<4100):
	zylium=(2.1*peso_tripulante)
elif (peso_tripulante>=4100):
	zylium=3.0*peso_tripulante
print(round(zylium,1))