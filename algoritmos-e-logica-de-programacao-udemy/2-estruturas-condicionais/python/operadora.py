"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Udemy - Algoritmos e lógica de programação (https://www.udemy.com/course/curso-algoritmos-logica-de-programacao/)

PT-BR:
Uma operadora de telefonia cobra R$ 50.00 por um plano básico que dá direito a 100 minutos de
telefone. Cada minuto que exceder a franquia de 100 minutos custa R$ 2.00. Fazer um programa para
ler a quantidade de minutos que uma pessoa consumiu, daí mostrar o valor a ser pago. 
"""

# Recebendo valores
minutos = int(input("Digite a quantidade de minutos | "))

# Calculando
valor_pagar = 50
if minutos > 100:
    valor_pagar += (minutos - 100) * 2

# Exibindo resultado
print("\nValor a pagar | R$ {:.2f}".format(valor_pagar))
