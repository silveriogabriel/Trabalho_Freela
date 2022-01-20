'''
    1) Em uma turma com 55 alunos deseja-se saber o valor total de bolsas concedidas. Faça um algoritmo que
    leia a matricula, o nome e o valor da mensalidade. O percentual da bolsa corresponde a 16% do valor da mensalidade.
    Obs.
    O cálculo do valor da bolsa deve ser feito dentro de uma função.

'''

#Calculando Bolsa
def bolsa(valor):
    return (valor * 16) / 100

#Definindo listas
bolsasconcedidas = []
#Cabeçalho
print('=' * 30)
print('      CALCULO DE BOLSA')
print('=' * 30)
#Range para 55 alunos
for i in range(55):
    matricula = input("Digite a matricula: ")
    nome = input("Digite o nome: ")
    while True:
        try:
            valor = float(input("Digite o valor da mensalidade: "))
        except:
            print('Opção Invalida!')
        else:
            break
    bolsasconcedidas.append(bolsa(valor))
    print('=' * 30)

print(f'O valor de bolsas concedidas corresponde a {sum(bolsasconcedidas):.2f}R$')

#Prof Fernando André