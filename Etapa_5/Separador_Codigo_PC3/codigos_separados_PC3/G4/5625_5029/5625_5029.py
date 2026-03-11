x = input("Digite T (tapioca) ou S(salgado): ")
if (x.upper() == "T") :
	t = int(input("Quantidade de tapiocas: "))
if (x.upper() == "S") :
	s = int(input("Quantidade de salgados: "))
a = int(input("Quantidade de acais: "))

tapioca = 5.50
salgado = 4.00
acai = 10.00

if (x == "T") :
	pf = (t*tapioca)+(a*acai)
	print(pf)
else:
	pf_ = (s*salgado)+(a*acai)
	print(pf_)