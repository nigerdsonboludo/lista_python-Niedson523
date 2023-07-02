#Lista de Exercício 1 - Questão 5
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que converta metros para centímetros.

class Conversor:
    def converter_para_centimetros(self, metros):
        return metros * 100


def obter_valor(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("Erro: O valor digitado não é válido.")


if __name__ == "__main__":
    conversor = Conversor()

    metros = obter_valor("Digite o valor em metros: ")

    centimetros = conversor.converter_para_centimetros(metros)
    print(f"{metros} metros equivalem a {centimetros} centímetros.")
