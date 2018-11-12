n = float(input())
n = n + 0.001 #tem que colocar isso por causa de um problema do python ao fazer cálculos com muitas casas decimais
if n >= 0 and n <= 1000000:
    notas100 = n // 100
    n = n - (notas100 * 100)
    notas50 = n // 50
    n = n - (notas50 * 50)
    notas20 = n % 50 // 20
    n = n - (notas20 * 20)
    notas10 = n % 20 // 10
    n = n - (notas10 * 10)
    notas5 = n // 5
    n = n - (notas5 * 5)
    notas2 = n // 2
    n = n - (notas2 * 2)
    moedas1 = n // 1
    n = n - (moedas1 * 1)
    moedas50 = n // 0.5
    n = n - (moedas50 * 0.5)
    moedas25 = n // 0.25
    n = n - (moedas25 * 0.25)
    moedas10 = n // 0.10
    n = n - (moedas10 * 0.10)
    moedas05 = n // 0.05
    n = n - (moedas05 * 0.05)
    moedas01 = n // 0.01
    n = n - (moedas01 * 0.01)
    print("NOTAS:")
    print("%d nota(s) de R$ 100.00"%notas100)
    print("%d nota(s) de R$ 50.00"%notas50)
    print("%d nota(s) de R$ 20.00"%notas20)
    print("%d nota(s) de R$ 10.00"%notas10)
    print("%d nota(s) de R$ 5.00"%notas5)
    print("%d nota(s) de R$ 2.00"%notas2)
    print("MOEDAS:")
    print("%d moeda(s) de R$ 1.00"%moedas1)
    print("%d moeda(s) de R$ 0.50"%moedas50)
    print("%d moeda(s) de R$ 0.25"%moedas25)
    print("%d moeda(s) de R$ 0.10"%moedas10)
    print("%d moeda(s) de R$ 0.05"%moedas05)
    print("%d moeda(s) de R$ 0.01"%moedas01)
