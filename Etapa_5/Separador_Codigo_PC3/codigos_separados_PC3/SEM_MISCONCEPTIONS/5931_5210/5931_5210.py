minexc = float(input("min: "))
semtaxa = 45 + 0.97 * minexc
vivo = semtaxa * 42/100 + semtaxa
print(round(vivo, 2))