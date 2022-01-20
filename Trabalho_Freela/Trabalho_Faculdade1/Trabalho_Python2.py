'''
    2) Dado um conjunto de n registros e cada registro contendo um valor real, faça um programa que calcule
    a média dos valores maiores que 10.
'''

#Definindo Quantidade De Registros
while True:
    try:
        n = int(input('Quantos registros: '))
    except:
        print('Opção invalida!')
    else:
        break
#Variavel para armazenar os valores maiores que 10
mdez = []
#Contador
cont = 0
#Loop for para pedir os valores
for i in range(n):
    while True:
        try:
            valorreal = float(input(f'Digite o {i + 1}° valor real: '))
        except:
            print('Opção invalida!')
        else:
            break
    if valorreal > 10:
        #Armazenando na lista
        mdez.append(valorreal)
        cont += 1
#verificando se foi digitado um valor maior que 10 e printando resultado.
if mdez == []:
    print('Nao foi digitado nenhum valor maior que 10.')
else:
    print(f'Foram digitados {cont} valores maiores que 10 e a média dos maiores são {sum(mdez)/len(mdez):.2f}')


#Prof Fernando André