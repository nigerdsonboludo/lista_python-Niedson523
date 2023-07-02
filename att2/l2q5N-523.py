#Lista de Exercício 2 - Questão 5
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class Aluno:
    def __init__(self):
        self.nota1 = 0.0
        self.nota2 = 0.0

    def obter_notas(self):
        while True:
            try:
                self.nota1 = float(input("Digite a primeira nota: "))
                self.nota2 = float(input("Digite a segunda nota: "))
                break
            except ValueError:
                print("Entrada inválida. Digite apenas números.")

    def calcular_media(self):
        return (self.nota1 + self.nota2) / 2

    def verificar_aprovacao(self):
        media = self.calcular_media()
        if media == 10:
            return "Aprovado com Distinção"
        elif media >= 7:
            return "Aprovado"
        else:
            return "Reprovado"


def main():
    aluno = Aluno()
    aluno.obter_notas()

    resultado = aluno.verificar_aprovacao()
    media = aluno.calcular_media()

    print(f"A média do aluno é: {media}")
    print(f"Resultado: {resultado}")


if __name__ == '__main__':
    main()
