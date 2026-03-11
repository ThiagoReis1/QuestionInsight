ML = float(input("media dos laboratorios: "))
MT = float(input("media dos trabalhos: "))
MP = float(input("media das provas: "))

nfinal = (ML*0.25) + (MT*0.30) + (MP*0.45)
print(round(nfinal,2))