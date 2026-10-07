"""
EXERCÍCIO 05: Feliz Nataaal!
Disciplina: Lógica de Programação com Python

ENUNCIADO:
Receba um número inteiro I (nível de empolgação).
Utilize repetição para exibir a frase "Feliz natal!" repetindo a letra 'a'
da palavra natal exatamente I vezes (ex: I=5 -> "Feliz nataaaal!").
"""

# TODO: Desenvolva o algoritmo abaixo:
import time

print("Gerador de Feliz Natal")
time.sleep(1)
print("Quanto maior sua empolgação, mais longo será o feliz natal")
time.sleep(1.5)
i = int(input("Qual é o seu nível de empolgação? "))
if i < 1:
    print("Digite um número igual ou maior que 1.")
else:
    print("\nGerando seu Feliz Natal", end="", flush=True)
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    time.sleep(0.5)
    qtd_a = ""
    for _ in range(i):
        qtd_a += "a"
    print(f"\n\nFeliz nat{qtd_a}l!!!")