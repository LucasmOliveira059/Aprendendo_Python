def gerador_fibonatti(n):
    p = 0
    s = 1
    while s < n:
        yield s
        p, s = s, s+p

y = int(input("Escolha o limite da sequência: "))
list = [x for x in gerador_fibonatti(y)]
print(list)

b1 = bin(y)
b2 = hex(y)

print(f'a versão bin de {y} é {b1} \na versão hexadecimal de {y} é {b2}')