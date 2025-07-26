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