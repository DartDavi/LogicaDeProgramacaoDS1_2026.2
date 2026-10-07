"""
EXERCÍCIO 04: Positivos e Média
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Leia 6 valores numéricos.
Conte quantos foram estritamente positivos (> 0) e calcule a média aritmética deles.
Imprima a quantidade de positivos e a média formatada com 1 casa decimal.
"""

# TODO: Desenvolva o algoritmo abaixo:
contador = 0
soma = 0
for i in range(6):
    valor = float(input(f"Digite o valor {i + 1}: "))
    if valor > 0:
        contador += 1
        soma += valor
print(f"{contador} valores positivos")
if contador > 0:
    media = soma / contador
    print(f"Média dos positivos: {media:.1f}")
else:
    print("Não ha valores positivos, sem medias")