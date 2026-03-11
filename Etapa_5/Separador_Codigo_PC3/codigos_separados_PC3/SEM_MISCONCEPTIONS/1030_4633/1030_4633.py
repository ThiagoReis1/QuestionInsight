mes=45
y=float(input("minutos"))
plano= (mes + 0.97*y)
serviço= (mes + 0.97*y)*0.42
total= serviço + plano
print(round(total, 2))