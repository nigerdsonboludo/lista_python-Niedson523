#Lista de Exercício 3 - Questão 6
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class Numeros:
    def imprimir_vertical(self):
        for i in range(1, 21):
            print(i)
    
    def imprimir_horizontal(self):
        for i in range(1, 21):
            print(i, end=" ")

numeros = Numeros()
numeros.imprimir_vertical()
numeros.imprimir_horizontal()
