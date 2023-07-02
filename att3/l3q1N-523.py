#Lista de Exercício 3 - Questão 1
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
                resposta = input("Resposta inválida. Digite S (sim) ou N (não): ").upper()
            self.respostas.append(resposta)

    def classificar_participacao(self):
        if self.respostas.count("S") == 2:
            return "Suspeita"
        elif 3 <= self.respostas.count("S") <= 4:
            return "Cúmplice"
        elif self.respostas.count("S") == 5:
            return "Assassino"
        else:
            return "Inocente"

    def exibir_classificacao(self):
        classificacao = self.classificar_participacao()
        print("Classificação: {}".format(classificacao))


def main():
    crime = ClassificacaoCrime()
    crime.fazer_perguntas()
    crime.exibir_classificacao()


if __name__ == "__main__":
    main()
