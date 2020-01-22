# Arquivos

# gerar um arquivo e escrever nele
#open('Arquivos/novo arquivo.txt', 'w')

#with (com essa função)

# with open('Arquivos/novo arquivo.txt', 'w') as f:
#     f.write ('Curso de Python')
    
# with open('Arquivos/novo arquivo.txt', 'r') as f:
#     f.read ('Curso de Python')

# with open('Arquivos/novo arquivo.txt', 'r') as f:
#    #inclui algo no arquivo
#     f.seek ()
#     f.write ('Teste 00')
#Funções e escopos

produtos=[]

def cadastrarProduto(produto):
   #para alterar a variavel global
   global produtos
   produtos.append(produto)

cadastrarProduto('Carro')

cadastrarProduto('Moto')

#print(produtos)

# def imprimir(produtos):
#    print(produtos)

# imprimir(produtos)

# def imprimir(produtos):
#    n=str()
#    for i in produtos:
#       n=n+i+','
#    print(n)
     
# imprimir(produtos)

usuarioX={'user':'camila', 'password':'@b@c@te123'}
#criar uma função que muda a senha do usuario X
# criar uma função para imprimir os dados do usuario X

# senhaNova=input("Digite a sua nova senha: ")

# def alterarSenha (usuario):
#    global usuarioX
#    usuario.update({'password': senhaNova})
#    print(usuario)

# def imprimirDados(usuario):
#    print(usuario)
# alterarSenha(usuarioX)
# imprimirDados(usuarioX)

# usuarios = {'users': {'user01':{'name':'camila','password':'abacaxi01'},
#                       'user02':{'name':'paulo','password':'abacaxi02'},
#                       'user03':{'name':'leo','password':'abacaxi03'},
#                       'user04':{'name':'mario','password':'abacaxi04'} }}

#  def verificUser(usuario):
#     while True:
#        Try:
#        if usuario not in usuarios['users'].keys():
#           raise NameError ('Usuario não cadastrado!')
#           continue
#         else:
#             print('Usuario não cadastrado')
#             break
#          except 

# verificaUser('user05')


# carrinho=[]
# produtos={'produtos':{'p001':{'nome':'Tenis','valor':21.70},
# 'p002':{'nome':'Meia','valor':10.0},
# 'p003':{'nome':'Camiseta','valor':17.30},
# 'p004':{'name':'Calça','valor':100.00}}

# def adicionarItens():
#    global carrinho
#    idProduto = input('Digite o ID do produto: ')
#    return carrinho.append(produtos['produtos'][idProduto])

# def imprimirCarrinho():
#    print(carrinho)

# def totalcarrinho():
#    valor=0
#    for i in carrinho:
#       valor+=i['valor']
#    return valor

# def cupomDesconto(cupom=''):
#    if cupom == 'gastemais'
#    return 1

# def alterarServidor (*valores):
#    print('O IP atual é {}'. format(valores[0]))
#    print('O novo IP é {}'.format(valores[3]))

#    alterarServidor ('10.0.0.1','192.168.1.2', outro)

#cria uma tupla
def ordenar(*valores):
   retun sorted(valores)

print(ordenar(2,5,6,8,97,5,8,6,55,8,7,555,8874))

#cria um dicionario
def imprimirK(**valores):
   print(valores)

imprimirk(var1='teste',var2='teste2')

vat=dict(var1="a",var2=teste2)


# adicionarItens()
# adicionarItens()
# adicionarItens()

# print('Total da compra: R$ {}')







