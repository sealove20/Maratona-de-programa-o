n = int(input())
np = n
if n > 0 and n < 1000000:
    notas100 = n // 100
    n = n % 100
    notas50 = n // 50
    n = n % 50
    notas20 = n % 50 // 20
    n = n % 20
    notas10 = n % 20 // 10
    n = n % 10
    notas5 = n // 5
    n = n % 5
    notas2 = n // 2
    n = n % 2
    notas1 = n // 1
    print(np)
    print("%d nota(s) de R$ 100,00"%notas100)
    print("%d nota(s) de R$ 50,00"%notas50)
    print("%d nota(s) de R$ 20,00"%notas20)
    print("%d nota(s) de R$ 10,00"%notas10)
    print("%d nota(s) de R$ 5,00"%notas5)
    print("%d nota(s) de R$ 2,00"%notas2)
    print("%d nota(s) de R$ 1,00"%notas1)
