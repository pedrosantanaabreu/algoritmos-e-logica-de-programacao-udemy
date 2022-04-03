"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Udemy - Algoritmos e lógica de programação (https://www.udemy.com/course/curso-algoritmos-logica-de-programacao/)

PT-BR:
Fazer um programa para calcular o troco no processo de pagamento de um produto de uma mercearia.
O programa deve ler o preço unitário do produto, a quantidade de unidades compradas deste produto,
e o valor em dinheiro dado pelo cliente (suponha que haja dinheiro suficiente). Seu programa deve
mostrar o valor do troco a ser devolvido ao cliente. 
"""

# Recebendo valores
preco_unitario = float(input("Digite o preço unitário | R$ "))
quantidade_comprada = int(input("Digite a quantidade comprada | "))
dinheiro_recebido = float(input("Digite o dinheiro recebido | R$ "))

# Calculando
troco = dinheiro_recebido - preco_unitario * quantidade_comprada

# Exibindo resultado
print("\nTroco | R$ {:.2f}".format(troco))
