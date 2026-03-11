ps=float(input('peso inicial do saco de racao:'))
qd=float(input('quantidade diaria de racao:'))
qsemanal=(qd*3)*5
qtotal=ps-qsemanal+201.1
print(round(qtotal,2))