min=float(input("Minutos consumidos:"))
if   (min<=100):
		valor=(min*1.20)
else: 
		valor=(min*1.40)+25
print(round(valor, 2))