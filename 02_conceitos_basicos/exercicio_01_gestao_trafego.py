"""
EXERCÍCIO 01: Gestão de Tráfego Casas Paulino
Disciplina: Lógica de Programação com Python

ENUNCIADO:
A loja Casas Paulino está veiculando anúncios no Meta Ads em Tianguá.
Escreva um programa que leia:
1. O valor total investido na campanha (em R$).
2. O número total de cliques obtidos.

Calcule e mostre na tela o Custo Por Clique (CPC) médio da campanha formatado em reais.
"""

# TODO: Desenvolva o algoritmo abaixo:

print("Loja Casas Paulino")
print("Meta ADS Média da campanha")
valor_investido = float(input("Digite o valor investido (R$): "))
cliques_obt = int(input("Digite a quantidade de cliques: "))
custo_click = valor_investido / cliques_obt
print("O custo por click(CPC) foi:", custo_click)