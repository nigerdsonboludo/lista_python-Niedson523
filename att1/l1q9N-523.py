#Lista de Exercício 1 - Questão 9
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

class Conversor:
    def converter_para_celsius(self, fahrenheit):
        celsius = 5 * ((fahrenheit - 32) / 9)
        return celsius


def obter_temperatura(mensagem):
    while True:
        try:
            temperatura = float(input(mensagem))
            return temperatura
        except ValueError:
            print("Erro: O valor digitado não é uma temperatura válida.")


if __name__ == "__main__":
    conversor = Conversor()

    fahrenheit = obter_temperatura("Digite a temperatura em graus Fahrenheit: ")

    celsius = conversor.converter_para_celsius(fahrenheit)
    print(f"A temperatura em graus Celsius é: {celsius:.2f}")
