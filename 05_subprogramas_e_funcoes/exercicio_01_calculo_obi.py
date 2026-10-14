"""
EXERCÍCIO 01: Pontuação OBI (Astro Lume Devs)
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Crie uma função nomeada `calcular_pontuacao_total(fase1, fase2, fase3)` com a diretiva `def`
que receba as 3 notas como parâmetros e retorne a pontuação total da equipe.
"""

# TODO: Desenvolva a função e os testes abaixo:
def calcular_pontuacao_total(fase1, fase2, fase3):
    return fase1 + fase2 + fase3
print("Pontuação OBI - Astro Lume Devs")
fase1 = float(input("Digite a nota da fase 1: "))
fase2 = float(input("Digite a nota da fase 2: "))
fase3 = float(input("Digite a nota da fase 3: "))
total = calcular_pontuacao_total(fase1, fase2, fase3)
print("Pontuação total da equipe:", total)