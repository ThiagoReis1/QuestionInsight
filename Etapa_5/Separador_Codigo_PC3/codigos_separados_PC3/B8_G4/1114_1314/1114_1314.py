v=float(input("Qual a velocidade do trem?"))
t=float(input("Digite o tempo:"))
print("Entradas:",v,"km/h","e",t,"h")
d=v*t
if d>0:    
    if(d==0):
        print("Proxima parada: Bravos")
    elif(d==100)or(100<d<200):
        print("Proxima parada: Castamere")
    elif(d==200)or(200<d<400):
        print("Proxima parada: Doriath")
    elif(d==400)or(200<d<600):
        print("Proxima parada: Edoras")
    elif(d==600)or(600<d<750):
        print("Proxima parada: Fangorn")
    elif(d==750)or(750<d<1150):
        print("Proxima parada: Godor")
    elif(d==1150)or(1150<d<1400):
        print("Proxima parada: Hogsmead")
else:
    print("Dados invalidos")
