cargaFrete = float(input()) * 43.21

freteTax = float(cargaFrete) + 25

impostoEroubo = float(freteTax) * 62/100

freteFinal = float(freteTax) + float(impostoEroubo)


print(round(freteFinal, 2))