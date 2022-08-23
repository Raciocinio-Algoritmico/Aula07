numero = 0
pares = 0
impares = 0
contador = 0

while contador < 10:
    numero = int(input("Digite um número inteiro qualquer: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    contador += 1

print("A quantidade de números pares é " + str(pares))
print("A quantidade de números ímpares é " + str(impares))