'''2) Dado um conjunto de n registros e cada registro contendo um valor real, faça um programa que calcule
a média dos valores maiores que 10.'''

#Verificando valor do loop
registros = int(input('Quantidade de registros: '))
contador = 1
maior10 = []
#Criando loop
while contador != registros+1:
    while True:
        try:
            n1 = float(input(f'Digite o {contador}° valor: '))
        except:
            print('VALOR INVALIDO!')
        else:
            break
    contador += 1
    if n1 > 10:
        maior10.append(n1)

#prints
print(f'A média dos valores maiores que 10 resulta em: {sum(maior10):.2f}')