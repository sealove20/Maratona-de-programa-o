n = int(input())
minutos = n//60
horas = minutos//60
minutos = minutos%60
segundos = n%60
print(str(horas)+":"+str(minutos)+":"+str(segundos))
