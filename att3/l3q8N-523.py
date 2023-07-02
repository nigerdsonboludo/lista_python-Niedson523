#Lista de Exercício 3 - Questão 8
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class Numeros:
    def calcular_soma_media(self):
        numeros = []
        for i in range(5):
            try:
                numero = float(input("Digite um número: "))
                numeros.append(numero)
            except ValueError:
                print("Valor inválido. Digite um número válido.")
                return
        soma = sum(numeros)
        media = soma / len(numeros)
        print("A soma dos números é:", soma)
        print("A média dos números é:", media)

numeros = Numeros()
numeros.calcular_soma_media()
