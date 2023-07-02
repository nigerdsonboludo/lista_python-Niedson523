#Lista de Exercício 2 - Questão 14
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class Aluno:
    def __init__(self):
        self.nota1 = 0
        self.nota2 = 0

    def ler_notas(self):
        while True:
            try:
                self.nota1 = float(input("Digite a primeira nota: "))
                self.nota2 = float(input("Digite a segunda nota: "))
                break
            except ValueError:
                print("Valor inválido. Digite um número válido.")

    def calcular_media(self):
        return (self.nota1 + self.nota2) / 2

    def obter_conceito(self, media):
        if 9.0 <= media <= 10.0:
            return "A"
        elif 7.5 <= media < 9.0:
            return "B"
        elif 6.0 <= media < 7.5:
            return "C"
        elif 4.0 <= media < 6.0:
            return "D"
        else:
            return "E"

    def exibir_resultado(self):
        media = self.calcular_media()
        conceito = self.obter_conceito(media)

        print("Nota 1: {:.1f}".format(self.nota1))
        print("Nota 2: {:.1f}".format(self.nota2))
        print("Média: {:.1f}".format(media))
        print("Conceito: {}".format(conceito))

        if conceito in ["A", "B", "C"]:
            print("APROVADO")
        else:
            print("REPROVADO")


def main():
    aluno = Aluno()
    aluno.ler_notas()
    aluno.exibir_resultado()


if __name__ == "__main__":
    main()
