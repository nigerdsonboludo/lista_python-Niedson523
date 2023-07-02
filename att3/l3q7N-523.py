#Lista de Exercício 3 - Questão 7
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class Numeros:
    def encontrar_maior(self):
        numeros = []
        for i in range(5):
            try:
                numero = float(input("Digite um número: "))
                numeros.append(numero)
            except ValueError:
                print("Valor inválido. Digite um número válido.")
                return
        maior = max(numeros)
        print("O maior número é:", maior)

numeros = Numeros()
numeros.encontrar_maior()
