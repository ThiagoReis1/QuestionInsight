a = input("digite o aminoacido: ")

aspartato = (4*12.011+6*1.00794+1*14.0067+4*15.9994)
cisteina = (3*12.011+7*1.00794+1*14.0067+2*15.9994+1*32.066)

if(a == "aspartato"):
	print(round(aspartato,2))

if(a == "cisteina"):
	print(round(cisteina,2))