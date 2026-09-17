"""
EXERCÍCIO 02: Consumo da Kawasaki Versys 300
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Para planejar uma viagem técnica de Tianguá até o Beach Park (Aquiraz),
solicite:
1. A distância total percorrida (em Km).
2. O total de combustível gasto (em Litros).

Calcule e imprima o consumo médio da motocicleta (Km/L) formatado com 2 casas decimais.
"""

# TODO: Desenvolva o algoritmo abaixo:

distancia_percorrida = float(input("Qual a distancia total percorrida em quilometros: "))
combustivel_gasto = float(input("Qual o total de combustivel gasto em litros: "))
consumo_m = distancia_percorrida / combustivel_gasto
print(f"O consumo medio em km/l é de: {consumo_m: .2f}")