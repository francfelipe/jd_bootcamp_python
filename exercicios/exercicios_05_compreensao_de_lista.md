# 1. O que são Compreensões de Listas?

As compreensões de listas (também conhecidas como "list comprehensions") são uma maneira elegante e concisa de criar novas listas em Python. Elas combinam a funcionalidade de loops for e instruções if em uma única linha, permitindo filtrar e transformar elementos de forma eficiente.

# 2. Estrutura Básica:

```Python
[expressão for elemento in sequência if condição]
```

- **Expressão**: Define o que será criado para cada elemento da sequência.  
- **Elemento**: Variável que itera sobre a sequência.  
- **Sequência**: Lista, string ou outro conjunto de dados iterável.  
- **Condição (opcional)**: Filtro que determina quais elementos da sequência serão incluídos na nova lista.  

# 3. Exemplos para Praticar:

## 1. Criando uma lista de quadrados dos números de 1 a 10:

```Python
quadrados = [numero * numero for numero in range(1, 11)]
print(quadrados)  # Resultado: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

## 2. Filtrando números pares de uma lista:

```Python
pares = [numero for numero in range(1, 21) if numero % 2 == 0]
print(pares)  # Resultado: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

### 3. Extraindo nomes de uma lista de dicionários:

```Python
nomes = [pessoa["nome"] for pessoa in dados_pessoas]
print(nomes)  # Resultado: ['João', 'Maria', 'Pedro', 'Ana'] (supondo 'dados_pessoas' seja uma lista de dicionários com chave 'nome')
```

## 4. Manipulando strings:

```Python
maiusculas = [letra.upper() for letra in frase]
print(maiusculas)  # Resultado: ['A', 'B', 'C', 'D', 'E', 'F'] (converte cada letra de 'frase' para maiúscula)
```

## 5. Usando módulos e funções:

```Python
import math
numeros_primos = [numero for numero in range(2, 20) if all(numero % divisor != 0 for divisor in range(2, math.sqrt(numero)))]
print(numeros_primos)  # Resultado: [2, 3, 5, 7, 11, 13, 17, 19] (encontra números primos até 20)
```

## 6. Compreensões de Listas Aninhadas:

```Python
matriz = [[linha[coluna] * 2 for coluna in range(len(linha))] for linha in matriz_original]
print(matriz)  # Resultado: [[2, 4, 6], [4, 8, 12], [6, 12, 18]] (dobra cada elemento da matriz original)
```

## 7. Usando Compreensões de Dicionários:

```Python
dicionario_quadrados = {numero: numero * numero for numero in range(1, 11)}
print(dicionario_quadrados)  # Resultado: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
```

## 8. Compreensões de Conjuntos:

```Python
conjunto_unicos = {elemento for elemento in lista if elemento not in conjunto_existente}
print(conjunto_unicos)  # Resultado: {elemento1, elemento2, ..., elementon} (remove elementos duplicados da lista)
```

# Exercícios para Afiar Suas Habilidades com Compreensão de Listas (com Resoluções)

1. Crie uma lista com o dobro de todos os números pares de 1 a 10.

```Python
dobro_pares = [numero * 2 for numero in range(1, 11) if numero % 2 == 0]
print(dobro_pares)  # Resultado: [4, 8, 12, 16, 20]
```

2. Crie uma lista com todas as palavras em maiúsculas de uma frase separada por espaços.

```Python
frase = "Esta é uma frase de exemplo."
maiusculas = [palavra.upper() for palavra in frase.split()]  # Separa por espaços e converte para maiúsculo
print(maiusculas)  # Resultado: ['ESTA', 'É', 'UMA', 'FRASE', 'DE', 'EXEMPLO']
```

3. Crie uma lista com todas as vogais de uma string.

```Python
texto = "Python é uma linguagem de programação poderosa."
vogais = [letra for letra in texto if letra.lower() in "aeiou"]  # Converte para minúsculo e verifica se é vogal
print(vogais)  # Resultado: ['o', 'e', 'u', 'a', 'o', 'a', 'i', 'o', 'a', 'e']
```

4. Crie uma lista com os quadrados perfeitos de 1 a 100 (um quadrado perfeito é o resultado de multiplicar um número inteiro por si mesmo).

```Python
quadrados_perfeitos = [numero * numero for numero in range(1, 11) if numero * numero <= 100]
print(quadrados_perfeitos)  # Resultado: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

5. Crie uma lista com os comprimentos de cada palavra em uma frase.

```Python
frase = "Aqui estamos praticando compreensões de lista."
comprimentos = [len(palavra) for palavra in frase.split()]
print(comprimentos)  # Resultado: [4, 9, 14, 8, 7, 5] (comprimento de cada palavra)
```

6. Dada uma lista de temperaturas em Celsius, crie uma lista com as temperaturas convertidas para Fahrenheit (F = (C * 9/5) + 32).

```Python
celsius = [10, 20, 30, 40]
fahrenheit = [round((celsius * 9/5) + 32, 2) for celsius in celsius]  # Arredonda para duas casas decimais
print(fahrenheit)  # Resultado: [50.0, 68.0, 86.0, 104.0]
```

7. Crie uma lista com todas as frutas de uma lista de dicionários, onde cada dicionário possua uma chave "tipo" com o valor "fruta".

```Python
dados = [
    {"nome": "Maçã", "tipo": "fruta"},
    {"nome": "Tomate", "tipo": "verdura"},
    {"nome": "Laranja", "tipo": "fruta"},
    {"nome": "Batata", "tipo": "verdura"}
]

frutas = [item["nome"] for item in dados if item["tipo"] == "fruta"]
print(frutas)  # Resultado: ['Maçã', 'Laranja']
```

8. Crie um dicionário com o quadrado de cada número de 1 a 5 como chave e o próprio número como valor.

```Python
quadrados = {numero: numero * numero for numero in range(1, 6)}
print(quadrados)  # Resultado: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

