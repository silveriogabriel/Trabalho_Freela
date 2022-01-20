'''1) Em uma turma com 55 alunos deseja-se saber o valor total de bolsas concedidas. Faça um algoritmo que
leia a matricula, o nome e o valor da mensalidade. O percentual da bolsa corresponde a 16% do valor da mensalidade.
Obs.
O cálculo do valor da bolsa deve ser feito dentro de uma função.'''

#Cauculando  bolsa
def calculobolsa(value):
    return value * 0.16
    
#Declarando listas e variaveis necessarias
registros = []
totbolsas = []
contador = 0

#Cabeçalho

print('=-' * 17)
print('   Trabalgo Prof Fernando André')
print('=-' * 17)

#Loop dos alunos
while contador < 55:
    matricula = input('Matricula: ')
    nome = input('Nome: ')
    while True:
        try:
            valor = float(input('Mensalidade: '))
        except:
            print('Valor digitado invalido!')
        else:
            break
    registros.append([matricula,nome,valor])
    contador += 1
    print('=-' * 17)
#Pegando valores da bolsa
for i in registros:
    totbolsas.append(calculobolsa(i[2]))
#Printando resultados
print(f'Valor de bolsa concedidas {sum(totbolsas):.2f}R$')