X = int(input("Insira a idade:"))
Y = float(input("insira o peso:"))
if (X >=0 and X<=130) and (Y>=0 and Y<=550.0):
    if (X >= 12 and Y >= 60.0):
        Z = ("1000")
        print ("Entradas:", X, "anos e", Y, "kg")
        print ("Dosagem:", Z, "mg")
    elif (X >=12 and Y<60.0):
        Z = ("875")
        print ("Entradas:", X, "anos e", Y, "kg")
        print ("Dosagem:", Z, "mg")
    elif (X < 12 and Y>=0 and Y<=5.0):
        Z = ("75")
        print ("Entradas:", X, "anos e", Y, "kg")
        print ("Dosagem:", Z, "mg")
    elif (X < 12 and Y>5.0 and Y<=9.0):
        Z = ("125")
        print ("Entradas:", X, "anos e", Y, "kg")
        print ("Dosagem:", Z, "mg")
    elif (X < 12 and Y>9.0 and Y<=16.0):
        Z = ("250")
        print ("Entradas:", X, "anos e", Y, "kg")
        print ("Dosagem:", Z, "mg")
    elif (X < 12 and Y>16.0 and Y<=24.0):
        Z = ("375")
        print ("Entradas:", X, "anos e", Y, "kg")
        print ("Dosagem:", Z, "mg")
    elif (X < 12 and Y>24.0 and Y<=30.0):
        Z = ("500")
        print ("Entradas:", X, "anos e", Y, "kg")
        print ("Dosagem:", Z, "mg")
    elif (X < 12 and Y>30.0 and Y<=550.0):
        Z = ("750")
        print ("Entradas:", X, "anos e", Y, "kg")
        print ("Dosagem:", Z, "mg")
else:
    print ("Entradas:", X, "anos e", Y, "kg")
    print ("Dados invalidos")