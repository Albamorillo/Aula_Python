print('Hola Mundo')

## VARIABLES
nome = 'Alba'
idade = 31
altura = 1.65
eh_maior = True

print('nome',nome, 'idade',idade, 'altura',altura, 'eh_maior',eh_maior)

##3 - entrada de usuario
nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

print(f"Ola, {nome}, voce tem {idade} anos.")

## 4- Estruturas condicionais (if, else, elif)
idade = int(input('Digite sua idade: '))
if idade >= 18:
    print('Voce e maior de idade')
elif idade >= 16:
    print('voce pode votar, mas nao dirigir')
else:
    print('voce e menor de idade')

## 5 laços de repetição (for, while)
## for (percorrer uma lista)

frutas = ['maçã', 'banana', 'laranja']
for fruta in frutas:
    print(fruta)

## while (executa ate uma condição ser falsa)
contador = 0

while contador < 5:
    print('Contador:', contador)
    contador += 1

## 6- Funções
def saudacao(nome):
    return f"Olá, {nome}!"

print(saudacao('Alba'))

## 7- listas e dicionários
## Listas
numeros = [1, 2, 3, 4, 5]
numeros.append(6)  # Adiciona um item
print(numeros[2]) # Acessa o terceiro item (indice 2)

## Dicionários
pessoa = {"nome": "Alba", "idade": 31,}
pessoa = {"nome": "João", "idade": 25,}

print(pessoa["nome"])  # Acessa o valor associado à chave "nome"
print(pessoa["idade"])  # Acessa o valor associado à chave "idade"

print(pessoa['nome'], "idade", pessoa['idade'])

