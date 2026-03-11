#Ingrid do Nascimento Mendes
#28/07/2016

h = int(input()) #habitantes 2000
v = int(input()) #vampiros 10
x = int(input()) #2 capacidade de cada vampiro transformar pessoas
y = int(input()) #5 vampiros mortos por dia
dias = 1

while (h>0):
	#v = v - y
	transf_dia = v * x
	#print ("transformou", transf_dia, "pessoas em vampiros")
	h = h - transf_dia
	#print ("restam", h, "habitantes")
	v = v - y + transf_dia
	#print ("restam", v, "vampiros")
	dias = dias + 1

print(dias)