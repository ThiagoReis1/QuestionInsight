vc=float(input("volume de agua "))
vesg=15
vf=0.37
vt=(vf*vc)+vesg
vtt=vt+(vt*(35/100))

print(round(vtt, 2))