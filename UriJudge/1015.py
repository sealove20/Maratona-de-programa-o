from math import sqrt
p1 = []
p2 = []

for i in range(2):
    var, var2 = input().split()
    if i == 0:
        p1.append(var)
        p1.append(var2)
    else:
        p2.append(var)
        p2.append(var2)

distancia = sqrt((float(p2[0])-float(p1[0]))**2+(float(p2[1])-float(p1[1]))**2)
print("%.4f" %distancia)
