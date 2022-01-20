'''3) Para cada nota de compra, tem-se o Nome do produto comprado, o valor e o imposto. Faça um programa
em Python que escreva o valor total do produto, o valor total do imposto e o valor total cobrado de todas as
notas. Considere 10 notas fiscais.'''

valores = []
impostos = []
print('=' * 30)
print('     CADASTRO DE PRODUTOS')
print('=' * 30)
for i in range(10):
    nome = input(f"Digite o nome do {i+1}° produto: ")
    while True:
        try:
            valor = float(input("Digite o valor do produto: "))
        except:
            print('Valor invalido digitado')
        else:
            break
    while True:
        try:
            imposto = float(input("Digite o valor do imposto: "))
        except:
            print('Valor invalido digitado')
        else:
            break      
    valores.append(valor)
    impostos.append(imposto)
    print(f'Valor total {valor + imposto:.2f}')
    print('=' * 30)

print(f'O valor total dos produtos são: R${sum(valores):.2f}')
print(f'O valor total do imposto é: R${sum(impostos):.2f}')
print(f'O valor de todas as notas resulta em: R${sum(valores) + sum(impostos):.2f}')

#Professor Fernando André