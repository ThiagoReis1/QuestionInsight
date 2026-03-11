a=float(input("minutos durante o mes: "))
b= 45 + 0.97 * a 
imposto= 42 * 0.97
e= b + imposto - a
print(round(e, 2))