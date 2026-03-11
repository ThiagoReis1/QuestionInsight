s_t= input('insira se e salgado ou tapiocas: ')
quanti_st= int(input("insira quanti. : "))
quant_a= int(input('isira a quanti de acai: '))

t=5.5
s=4.0
a=10

if s_t ==  "S":
	total= (s * quanti_st) + (a * quant_a)
else: 
	total= (t * quanti_st) + (a * quant_a)

print(round(total, 1))
	
