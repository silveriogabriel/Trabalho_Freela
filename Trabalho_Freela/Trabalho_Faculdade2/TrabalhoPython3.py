'''3) Para cada nota de compra, tem-se o Nome do produto comprado, o valor e o imposto. Faça um programa
em Python que escreva o valor total do produto, o valor total do imposto e o valor total cobrado de todas as
notas. Considere 10 notas fiscais.'''

#Definindo variaveis
impostos = []
valores = []
cont = 0
print('-=' * 20)
print('        Cadastro de compras')
print('-=' * 20)

#Loop para cadastros
while cont < 10:
    nomeproduto = input('Produto: ')
    while True:
        try:
            valorproduto = float(input('Valor do produto R$'))
            impostoproduto = float(input('Valor do imposto R$'))
        except:
            print('Valor invalido!')
        else:
            break
    valores.append(valorproduto)
    impostos.append(impostoproduto)
    print(f'Valor total {valorproduto + impostoproduto:.2f}R$')
    cont += 1
    print('-=' * 20)

#Prints
print(f'O valor total dos produtos foi {sum(valores):.2f}R$')
print(f'O valor total de impostos foi {sum(impostos):.2f}R$')
print(f'O valor total da compra foi {sum(valores) + sum(impostos):.2f}R$')
