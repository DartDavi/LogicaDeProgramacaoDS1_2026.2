"""
EXERCÍCIO 05: Média Ponderada da Avaliação Técnica
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Solicite as notas de três avaliações do curso técnico.
A primeira prova tem peso 2, a segunda peso 3 e a terceira peso 5.
Calcule e exiba a média final ponderada utilizando apenas operadores aritméticos.
"""

# TODO: Desenvolva o algoritmo abaixo:

nota1 = float(input("Digite a nota da primeira avaliação(peso 2): "))
nota2 = float(input("Digite a nota da segunda avaliação(peso 3): "))
nota3 = float(input("Digite a nota da terceira avaliação(peso 5): "))
media_final = (nota1 * 2 + nota2 * 3 + nota3 * 5) / 10
print (f"A média final ponderada é: {media_final: .2f}")