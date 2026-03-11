ni=float(input("numero de celulas cancerosa:"))
tr=float(input("taxa de reduçao:"))
nnovos=float(input("numero de novas celulas  cancerigenas:"))

quinzena=1
tr=tr*ni
while(ni<500000):			
			ni=ni-tr+nnovos
			quinzena=quinzena+1
			tr=tr*ni

print(quinzena)