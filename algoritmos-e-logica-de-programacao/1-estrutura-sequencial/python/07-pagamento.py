"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Udemy - Algoritmos e lógica de programação (https://www.udemy.com/course/curso-algoritmos-logica-de-programacao/)

PT-BR:
Fazer um programa para ler o nome de um(a) funcionário(a), o valor que ele(a) recebe por hora, e a
quantidade de horas trabalhadas por ele(a). Ao final, mostrar o valor do pagamento do funcionário com
uma mensagem explicativa, conforme exemplo
"""

# Recebendo valores
nome = input("Digite o nome | ")
valor_hora = float(input("Digite o valor por hora | R$ "))
horas_trabalhadas = int(input("Digite as horas trabalhadas | "))

# Calculando
salario_final = valor_hora * horas_trabalhadas

# Exibindo resultado
print("\nO pagamento para {} deve ser R$ {:.2f}".format(nome, salario_final))
