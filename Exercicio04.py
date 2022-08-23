numero = int(input("Digite quantos inteiros quer imprimir após o 1: "))
contador = 1
soma = 0

while contador <= numero:
    soma += contador
    contador += 1

print("A soma dos " + str(numero) + " números a partir do 1 é " + str(soma))