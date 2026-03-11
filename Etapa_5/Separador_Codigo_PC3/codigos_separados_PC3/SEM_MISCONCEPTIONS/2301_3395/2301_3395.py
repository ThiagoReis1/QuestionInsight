from math import*


ladob=float(input("digite o valor de b"))
ladoc=float(input("digite o valor de c"))
anguloalfa=float(input("digite o valor de alfa:"))
variavel1=ladob**2
variavel2=ladoc**2
variavel3=radians(anguloalfa)
variavel4= float(sqrt (2*variavel1+variavel2))


cosseno=float(sqrt (2*ladob*ladoc*variavel3)
variavel5=float(cosseno-variavel4)
print(round(variavel5,2))