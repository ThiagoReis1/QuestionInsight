aminoacido = input("qual aminoacido ?:")
o =15.999
c =12.011 
n =14.00674
h =1.00794

prolina =  (c * 5) + (h * 10) + n + (o * 2)

histidina = (c * 6) + (h * 10) + (n * 3) + (0 * 2)

if (aminoacido == prolina):
    peso =  (c * 5) + (h * 10) + n + (o * 2)
else:
	 peso = (c * 5) + (h * 10) + n + (o * 2)
		
print(round(peso, 2))