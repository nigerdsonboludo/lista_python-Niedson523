#Lista de Exercício 1 - Questão 4
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

class Calculadora:
    def calcular_media(self, notas):
        return sum(notas) / len(notas)


def obter_nota(mensagem):
    while True:
        try:
            nota = float(input(mensagem))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Erro: A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Erro: O valor digitado não é uma nota válida.")


if __name__ == "__main__":
    calculadora = Calculadora()

    notas = []
    for i in range(4):
        nota = obter_nota(f"Digite a {i+1}ª nota: ")
        notas.append(nota)

    media = calculadora.calcular_media(notas)
    print(f"A média é: {media}")
