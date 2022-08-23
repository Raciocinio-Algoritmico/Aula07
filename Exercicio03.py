numero = int(input("Digite um numero inteiro qualquer: "))
soma = 0
contador = 0

while numero != -1:
    soma += numero
    contador += 1
    numero = int(input("Digite outro numero inteiro qualquer: "))

resultado = soma / contador
print("A média da soma dos valores é " + str(resultado))