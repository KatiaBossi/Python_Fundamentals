#Faça um programa de calculo de media que receba 4 notas e retorne a média.
'''n1 = float(input("Informe a primeira nota: "))
n2 = float(input("Informe a segunda nota: "))
n3 = float(input("Informe a terceira nota: "))
n4 = float(input("Informe a quarta nota: "))
media = (n1+n2+n3+n4)/4
print(media)'''

#faça um programa que imprime na tela as seguintes informações
# Camiseta, branca, G
# Calça,42, verde
# Camiseta, branca,42
produtos = ['Camiseta', ['p','m','g'], 'Calça',['40','42','48'],['branca','amarela','verde']]
print (produtos[0]+','+produtos[4][0]+','+ produtos [1][2])
print(produtos [2]+','+produtos[3][1]+','+produtos[4][2])
print(produtos [0]+','+ produtos[4][0]+','+ produtos[3][1])
