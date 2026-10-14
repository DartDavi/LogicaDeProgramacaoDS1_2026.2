"""
EXERCÍCIO 04: Função Lambda de Desconto Casas Paulino
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Escreva uma função anônima (lambda) que receba o valor de um produto
e retorne o valor com 15% de desconto à vista aplicado.
"""

# TODO: Desenvolva a expressão lambda e teste-a abaixo:
desconto_avista = lambda valor: valor * 0.85
print("Casas Paulino - Desconto à Vista")
valor_produto = float(input("Digite o valor do produto (R$): "))
valor_final = desconto_avista(valor_produto)
print(f"Valor com 15% de desconto à vista: R$ {valor_final:.2f}")