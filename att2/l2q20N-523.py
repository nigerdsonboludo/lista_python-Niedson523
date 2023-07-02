#Lista de Exercício 2 - Questão 20
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class MediaNotas:
    def __init__(self):
        self.nota1 = 0
        self.nota2 = 0
        self.nota3 = 0

    def ler_notas(self):
        while True:
            try:
                self.nota1 = float(input("Digite a primeira nota: "))
                self.nota2 = float(input("Digite a segunda nota: "))
                self.nota3 = float(input("Digite a terceira nota: "))
                break
            except ValueError:
                print("Nota inválida. Digite um número válido.")

    def calcular_media(self):
        media = (self.nota1 + self.nota2 + self.nota3) / 3
        return media

    def exibir_resultado(self):
        media = self.calcular_media()

        if media == 10:
            print("Aprovado com Distinção. Média: {:.2f}".format(media))
        elif media >= 7:
            print("Aprovado. Média: {:.2f}".format(media))
        else:
            print("Reprovado. Média: {:.2f}".format(media))


def main():
    aluno = MediaNotas()
    aluno.ler_notas()
    aluno.exibir_resultado()


if __name__ == "__main__":
    main()
