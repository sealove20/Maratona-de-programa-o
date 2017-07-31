consumo = 12  #KM/L
tempo = int(input()) #Horas
velocidade_media = int(input()) #KM/h
quantidade = tempo*velocidade_media/consumo
print("%.3f"%quantidade)
