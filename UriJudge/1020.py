val = int(input())
ano = val // 365
mes = (val % 365) // 30
dia = (val % 365) % 30
print(ano,"ano(s)")
print(mes,"mes(es)")
print(dia,"dia(s)")
