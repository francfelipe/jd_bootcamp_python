# Criar um programa onde o usuário digite dois valores e aparece o valor da soma

vl1 = input("Digite o primeiro valor: ")
vl2 = input("Digite o segundo valor: ")

vl1 = int(vl1)
vl2 = int(vl2)

vl3 = vl1 + vl2

print(f'O resultado de {vl1} + {vl2} é: {vl3}')

'''
Por definição ao inserir um dado através do input, o programa renhecerá como texto (str). 
Então, ao digitarmos um número, o programa gravará como texto.
Precisamos tratar convertendo para o tipo de dado que queremos. 

Resumindo:

"7" é diferente de 7 que é diferente de 7.0

"7" é um texto (str)
7 é inteiro (int)
7.0 é um decimal (float)

'''