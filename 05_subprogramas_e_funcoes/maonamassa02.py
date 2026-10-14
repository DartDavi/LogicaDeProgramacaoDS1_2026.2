# TODO: Crie a função lambda aqui
calcular_acrescimo = lambda valor, percentual: valor * (1 + percentual / 100) # Substitua pela expressão lambda
# Teste
print(calcular_acrescimo(100, 10))
print(calcular_acrescimo(250, 15))
print(calcular_acrescimo(80, 0))
print(f"R$ {calcular_acrescimo(199.90, 5):.2f}")