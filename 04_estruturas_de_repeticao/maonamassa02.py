# TODO: Desenvolva o acumulador com parada no 0

# Escreva a estrutura de repetição while
soma = 0
while True:
    valor = int(input("Digite um número(Digite 0 para encerrar): "))
    if valor == 0:
        break
    soma += valor
print("A soma total é: ",soma)