# TODO: Desenvolva seu algoritmo aqui
# 1. Leia o valor da conta (float)
# 2. Leia o número de pessoas (int)
# 3. Calcule o valor por pessoa
# 4. Imprima formatado usando f-string

valor_conta = float(input("Digite o valor total da conta: "))
num_pessoas = int(input("Digite a quantidade de pessoas: "))
valor_pessoa = valor_conta / num_pessoas
print(f"O valor para cada pessoa deve pagar é: R$ {valor_pessoa:.2f}")