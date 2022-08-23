numero = int(input("Digite um número inteiro qualquer: "))

contador = 1
while contador <= 10:
    multiplicacao = numero * contador
    print(str(numero) + " x " + str(contador) + " = " +  str(multiplicacao))
    contador += 1