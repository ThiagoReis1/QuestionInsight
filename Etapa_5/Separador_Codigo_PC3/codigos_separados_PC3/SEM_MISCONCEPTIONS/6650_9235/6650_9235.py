from numpy import*
conj_nota = array(eval(input("digite o alor da nota: ")))
media = conj_nota[0]*4 + conj_nota[1]*3
peso = 4,3
resultado = sum(media)/sum(peso)
print(round(resultado, 2))