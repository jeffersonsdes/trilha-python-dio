

texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

#Exemplo utilizando iterável

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

else:
    print() #adiciona quebra de linha


#Exemplo2: Utilizando range com for

for numero in range(0, 11):
    print(numero, end=" ")

print() #adiciona uma quebra de linha

#Exemplo utilizando bulit-in range

for numero in range(0, 51, 5):
    print(numero, end=" ") 




