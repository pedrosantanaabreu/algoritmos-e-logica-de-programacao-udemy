"""
@Pedro Santana Abreu (https://linktr.ee/pedrosantanaabreu)
@Udemy - Algoritmos e lógica de programação (https://www.udemy.com/course/curso-algoritmos-logica-de-programacao/)

PT-BR:
Uma lanchonete possui vários produtos. Cada produto possui um código
e um preço. Você deve fazer um programa para ler o código e a
quantidade comprada de um produto (suponha um código válido), e daí
informar qual o valor a ser pago, com duas casas decimais, conforme
tabela de produtos ao lado

Código do
produto
Preço do
produto
1 R$ 5.00
2 R$ 3.50
3 R$ 4.80
4 R$ 8.90
5 R$ 7.32 
"""

# Recebendo valores
codigo_produto = int(input("Digite o código do produto | "))
quantidade_comprada = int(input("Digite a quantidade comprada | "))

# Calculando
if codigo_produto == 1:
    preco_produto = 5
elif codigo_produto == 2:
    preco_produto = 3.5
elif codigo_produto == 3:
    preco_produto = 4.8
elif codigo_produto == 4:
    preco_produto = 8.9
else:
    preco_produto = 7.32

valor_pagar = preco_produto * quantidade_comprada

# Exibindo resultado
print("\nValor a pagar | R$ {:.2f}".format(valor_pagar))
