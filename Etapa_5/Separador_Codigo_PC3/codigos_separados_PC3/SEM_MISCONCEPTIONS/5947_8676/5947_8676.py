tipo_de_s = input("C ou E: ")

Q = float(input("Q de Salg: "))
qntd = float(input("Q de Suc: "))

if tipo_de_s.upper() == "C":
	total = Q * 2.0 + qntd * 6
else:
	total = Q * 4.5 + qntd * 6 

print(round(total,2))
