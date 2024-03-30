# #### try-except e if

# 22: Verificador de Palíndromo

def converter_temperatura(valor, tipo_conversao):
    if tipo_conversao == "1":  # Celsius para Fahrenheit
        return (valor * 9/5) + 32
    elif tipo_conversao == "2":  # Fahrenheit para Celsius
        return (valor - 32) * 5/9
    elif tipo_conversao == "3":  # Celsius para Kelvin
        return valor + 273.15
    elif tipo_conversao == "4":  # Kelvin para Celsius
        return valor - 273.15
    else:
        print("Tipo de conversão não reconhecido.")
        return None

while True:
    print("Digite o tipo de conversão que deseja realizar:")
    print("1: Celsius para Fahrenheit")
    print("2: Fahrenheit para Celsius")
    print("3: Celsius para Kelvin")
    print("4: Kelvin para Celsius")
    tipo_conversao = input()

    entrada = input("Agora, digite o valor da temperatura a ser convertido: ")
    try:
        valor = float(entrada)
        resultado = converter_temperatura(valor, tipo_conversao)
        if resultado is not None:
            print(f"Resultado da conversão: {resultado} graus")
        break
    except ValueError:
        print("Valor inválido. Por favor, digite um número.")


# 23: Calculadora Simples

def solicitar_numero(mensagem):
    """Solicita ao usuário um número, repetindo até que um valor válido seja fornecido."""
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Isso não é um número válido. Por favor, digite um número.")

def realizar_operacao(operacao, n1, n2):
    """Realiza a operação matemática selecionada."""
    if operacao == '1':
        return n1 + n2
    elif operacao == '2':
        return n1 - n2
    elif operacao == '3':
        return n1 * n2
    elif operacao == '4':
        try:
            return n1 / n2
        except ZeroDivisionError:
            return "Erro: Divisão por zero não é permitida."

def main():
    print("Calculadora Simples")
    print("Escolha a operação:")
    print("1: Adição")
    print("2: Subtração")
    print("3: Multiplicação")
    print("4: Divisão")
    operacao = input("Digite o número da operação desejada: ")

    if operacao in ['1', '2', '3', '4']:
        num1 = solicitar_numero("Digite o primeiro número: ")
        num2 = solicitar_numero("Digite o segundo número: ")
        resultado = realizar_operacao(operacao, num1, num2)
        print(f"Resultado: {resultado}")
    else:
        print("Operação inválida. Por favor, escolha uma operação entre 1 e 4.")

if __name__ == "__main__":
    main()

# 24: Classificador de Números
# 25: Conversão de Tipo com Validação