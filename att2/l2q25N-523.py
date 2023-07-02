#Lista de Exercício 2 - Questão 25
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class ClassificacaoCrime:
    def __init__(self):
        self.respostas = []

    def fazer_perguntas(self):
        perguntas = [
            "Telefonou para a vítima?",
            "Esteve no local do crime?",
            "Mora perto da vítima?",
            "Devia para a vítima?",
            "Já trabalhou com a vítima?"
        ]

        for pergunta in perguntas:
            resposta = input(pergunta + " (S/N): ").upper()
            while resposta not in ["S", "N"]:
                resposta = input("Resposta inválida. Digite S para Sim ou N para Não: ").upper()
            self.respostas.append(resposta)

    def classificar_participacao(self):
        quantidade_positivas = self.respostas.count("S")

        if quantidade_positivas == 2:
            return "Suspeita"
        elif quantidade_positivas >= 3 and quantidade_positivas <= 4:
            return "Cúmplice"
        elif quantidade_positivas == 5:
            return "Assassino"
        else:
            return "Inocente"

    def exibir_resultado(self):
        classificacao = self.classificar_participacao()
        print("Classificação: {}".format(classificacao))


def main():
    crime = ClassificacaoCrime()
    crime.fazer_perguntas()
    crime.exibir_resultado()


if __name__ == "__main__":
    main()
