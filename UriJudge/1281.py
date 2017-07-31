n = int(input())
l5 = []
for i in range(n):
    nome_disponivel = []
    valor_disponivel = []
    nome_compra = []
    valor_compra = []
    total = 0.0
    fra = ''
    k=0
    m = int(input())
    for j in range(m):
        var, var2 = input().split()
        nome_disponivel.append(var)
        valor_disponivel.append(var2)

    p = int(input())
    if p >= 1 and p <= m:
        for i in range(p):
            var, var2 = input().split()
            if len(var) <=50:
                nome_compra.append(var)
                valor_compra.append(var2)



        for i in range(len(nome_disponivel)):
            for j in range(len(nome_compra)):
                if nome_compra[j] == nome_disponivel[i]:
                    total += float(valor_disponivel[i]) * int(valor_compra[j])

        fra = total
        l5.append(fra)

    else:
        break

for i in range(len(l5)):
    print("R$ %.2f" %l5[i])
