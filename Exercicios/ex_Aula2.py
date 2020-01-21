dados={
    'estados':{
        'sp':{
            'nome':'São Paulo',
            'municipio':645,
            'população':44.04
        },
        'rj':{
            'nome': 'Rio de Janeiro',
            'municipio':92,
            'população':16.72
        },
        'mg':{
            'nome':'Minas Gerais',
            'municipio':31,
            'população':20.87
        }
    }
}
#imprima as seguintes informações:
# padrão: Nome: nome_estado
        # Municipios: y
        # População: x
# 1. nomes dos estados
# 2. nomes dos estados e suas populações em milhões 
# 3 - nomes dos estados e e seus municipios


#print('Nomes: {},{},{}'.format(dados['estados']['sp']['nome'],dados['estados']['rj']['nome'],dados['estados']['mg']['nome']))
#print('Nome do estado:{}\n População: {}'.format(,))
#print('Nome dos Estados: {}\n Municipios: {}'. format(,))

# for i in dados ['estados']:
#     print ('nome: {}'.format (dados ['estados'][i]['nome']))
#     print('\n')
# for i in dados ['estados']:
#     print('nome: {}\nPopulação: {} milhões' .format (dados ['estados'][i]['nome'],dados ['estados'][i]['população'] ))
#     print('\n')
# for i in dados ['estados']:
#     print('nome: {}\nMunicipio: {}' .format (dados ['estados'][i]['nome'],dados ['estados'][i]['municipio'] ))
#     print('\n')

# software de imposto de renda
# peça ao usuario o valor do salario mensal.
# se o salario for maior ou igual a 4600 a aliquota 27%
# se o salário for menor que 4600 e maior que 3700, a aliquota 22%
# se o salário for menor que 3700 e maior que 2800 a aliquota é de 15%
# se o salario for menor que 2800 aliquota é 0

# sal = float(input("Informe o salário: "))
# if sal < 2800:
#     valor = 0
# elif sal >= 2800 and sal<3700:
#     valor=sal*0.15
# elif sal>=3700 and sal<4600:
#     valor=sal*0.22
# elif sal>=4600:
#     valor=sal*0.27
# print("Valor do imposto: {}". format(valor))

frutas=["banana", "maça", "abacate"]
#for num, item in enumerate (frutas):
#   print("Fruta {} está na posição {}. format(item,num)")

# lista=[]
# for num in range (20):
#     if num %2==0:
#         continue
#     else:
#         lista. append(num)
# print(lista)

users=['maria','carlos','pedro']


login=input('Digite seu usuario ')
if login in users:
    print("Acesso permitido!")
else:
    print("Acesso negado!")
    




