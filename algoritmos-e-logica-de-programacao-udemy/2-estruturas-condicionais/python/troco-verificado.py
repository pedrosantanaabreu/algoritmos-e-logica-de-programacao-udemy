"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Udemy - Algoritmos e lógica de programação (https://www.udemy.com/course/curso-algoritmos-logica-de-programacao/)

PT-BR:
Fazer um programa para calcular o troco no processo de pagamento de um produto de uma mercearia.
O programa deve ler o preço unitário do produto, a quantidade de unidades compradas deste produto,
e o valor em dinheiro dado pelo cliente. Seu programa deve mostrar o valor do troco a ser devolvido
ao cliente. Se o dinheiro dado pelo cliente não for suficiente, mostrar uma mensagem informando o
valor restante conforme exemplo. 
"""

# Recebendo valores
preco_produto = float(input("Preço unitário do produto | R$ "))
quantidade_produto = int(input("Quantidade comprada | "))
dinheiro_recebido = float(input("Dinheiro recebido | R$ "))

# Calculando
troco = dinheiro_recebido - preco_produto * quantidade_produto
if troco < 0:
    print("\nDinheiro insuficiente, faltam | R$ {:.2f}".format(troco * -1))
else:
    print("\nTroco | R$ {:.2f}".format(troco))
