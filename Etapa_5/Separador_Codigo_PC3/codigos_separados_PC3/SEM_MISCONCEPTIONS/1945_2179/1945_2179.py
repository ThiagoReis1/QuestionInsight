nome_do_aminoacido = input("nome do aminoacido: ")

o = 15.9994
c = 12.011
n = 14.0067
s = 32.066
h = 1.00794

aspartato = c*4 + h*6 + n + o*4
cisteina = c*3 + h*7 + n + o*2 + s

if(nome_do_aminoacido.lower() == "aspartato"):
	peso = aspartato
else:
	peso = cisteina

print(round(peso, 2))