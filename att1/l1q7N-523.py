#Lista de Exercício 1 - Questão 7
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário

class Calculadora:
    def calcular_area_quadrado(self, lado):
        return lado ** 2


def obter_lado(mensagem):
    while True:
        try:
            lado = float(input(mensagem))
            if lado >= 0:
                return lado
            else:
                print("Erro: O lado do quadrado deve ser um valor positivo ou zero.")
        except ValueError:
            print("Erro: O valor digitado não é um lado válido.")


if __name__ == "__main__":
    calculadora = Calculadora()

    lado = obter_lado("Digite o lado do quadrado: ")

    area = calculadora.calcular_area_quadrado(lado)
    dobro_area = area * 2

    print(f"A área do quadrado é: {area}")
    print(f"O dobro da área do quadrado é: {dobro_area}")
