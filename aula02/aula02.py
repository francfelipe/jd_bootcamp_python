'''
Precisamos ter cuidado ao desenvolver pois sempre pensamos no caminho feliz do usuário.
Num programa simples de divisão onde pedimos dois números pensamos que o usuário colocará dois números divisíveis. 
E se ele colocar 2 dividido por 0? O programa trava! ZeroDivisionError
E se pedimos para ele colocar um valor inteiro e ele colocar uma string ou float?

Sempre que desenvolvemos precisamos pensar no caminho infeliz do usuário.
Tratar erros e direcionar o usuário ao caminho feliz.

Ver documentação: docs.python.org/3/library/exceptions.html

Um bom engenheiro de dados é um cara pessimista com atitude. Sempre coloque os testes no cronograma.
Se você desenvolve em 1 semana, fique mais 1 ou 2 testanto e tentando antecipar os caminhos infelizes da sua entrega.

É bem pior o erro acontecer quando está rodando em produção!

---

Try: tente fazer isso
    input
Except: Se nao der faça isso

'''

# try:
#     v1 = input("Digite o primeiro valor (int): ")
#     v2 = input("Digite o segundo valor (int): ")
#     v1 = int(v1)
#     v2 = int(v2)
#     v3 = v1 // v2 
#     print(f'O resultado é: {v1} / {v2} = {v3}.')
# except:
#     print(f'Confira se você digitou números inteiros válidos: primeiro: {v1} segundo: {v2}')
    
    
'''
Se você depende de coisas que não estão em seu controle (chamado testes de integração), exemplos: um valor que o usuário
vai digitar, uma api que vai consultar, um banco de dados que você vai inserir dados, um excel que você vai receber. 
um site que você vai fazer webscraping. 

Enfim, qualquer coisa que você vai interagir que fuja do seu controle, faça um try para não interromper o programa.

tente alguma coisa (try)
se der erro faça (except)

Eu posso explicitar o tipo de erro podendo ter vários tipos de erros (veja documentação de exceptions)

'''

# try:
#     v1 = input("Digite o primeiro valor (int): ")
#     v2 = input("Digite o segundo valor (int): ")
#     v1 = int(v1)
#     v2 = int(v2)
#     v3 = v1 // v2 
#     print(f'O resultado é: {v1} / {v2} = {v3}.')
# except ZeroDivisionError:
#     print('Você não pode dividir um número por zero.')
# except KeyboardInterrupt:
#     print('Acho que você interrompeu o programa')
# except TypeError as e: # vai printar a mensagem de erro ao usuário
#     print(e)
# except ValueError:
#     print('Você não digitou um valor inteiro')
# except:
#     print(f'Confira se você digitou números inteiros válidos: primeiro: {v1} segundo: {v2}')
    
    
'''
Você pode imprimir a mensagem de erro na tela do usuário.
Como boa prática, você pode gravar estes erros em uma tela de log e acompanhar periodicamente para evoluir seu código.

Podemos incluir um else no processo Então a lógica será 
try: tente fazer isso
except TypeError as e: se não deu certo por este tipo de erro (TypeError) faça isso
else: se deu certo faça isso

O else neste contexto do try é diferente no contexto do if.
else no try: fala o try e faça o else
else no if: faça o if OU faça o else

'''

# try:
#     resultado = len(3)
#     print(resultado)
# except TypeError as e:
#     print(e)
# else:
#     print("tudo ocorreu bem")
    
    
'''
temos também o finally no qual, indepedentemente do que ocorrer ele vai executar este processo.
'''

# try:
#     resultado = len(3)
#     print(resultado)
# except TypeError as e:
#     print(e)
# else:
#     print("tudo ocorreu bem")
# finally:
#     print("O processo finalizou")
    
# try:
#     resultado = len("felipe")
#     print(resultado)
# except TypeError as e:
#     print(e)
# else:
#     print("tudo ocorreu bem")
# finally:
#     print("O processo finalizou")
    
    
'''

validador ISINSTANCE

Ele é parecido com o try

if isinstance(numero, int): # avalie para mim se numero é inteiro
    print('O número é um inteiro')
else:
    print('O número não é inteiro')

'''

# numero = input('Insira um número: ')
# if isinstance(numero, int):
#     print('O valor digitado é um inteiro')
# else:
#     print('O valor digitado não é um inteiro')
    
    
# # Inicia um loop infinito que só quebra quando um valor válido é inserido
# while True:
#     entrada_usuario = input("Digite o valor do seu salário (entre 1400 e 100000): ")
    
#     # Tentar converter a entrada para float
#     try:
#         salario = float(entrada_usuario)
        
#         # Verifica se o salário está dentro do intervalo e não é zero
#         if 1400 <= salario <= 100000:
#             print("Valor válido. Obrigado!")
#             break  # Sai do loop
#         else:
#             print("Valor fora do intervalo permitido. Por favor, tente novamente.")
    
#     except ValueError:  # Captura o erro se a conversão para float falhar
#         print("Por favor, insira um valor numérico válido, sem espaços ou texto.")

# # Continua com a lógica do programa usando o valor de 'salario'



'''
Condicional IF
'''

# objeto em caixa alto para identificar uma constante, que não será alterada
# IDADE_MININA_PARA_DIRIGIR = 18
# IDADE_PARA_TIRAR_A_CARTEIRA = 18

# if idade < IDADE_MININA_PARA_DIRIGIR:
#     print('Não pode dirigir')
# elif idade == IDADE_PARA_TIRAR_A_CARTEIRA:
#     print('Uhul! Completou 18 este ano, pode tirar a carteira')
# else:
#     print('Pode tirar a carteira')
