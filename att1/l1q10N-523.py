#Lista de Exercício 1 - Questão 10
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit. 

class Conversor:
    def converter_para_fahrenheit(self, celsius):
        fahrenheit = (celsius * 9/5) + 32
        return fahrenheit


def obter_temperatura(mensagem):
    while True:
        try:
            temperatura = float(input(mensagem))
            return temperatura
        except ValueError:
            print("Erro: O valor digitado não é uma temperatura válida.")


if __name__ == "__main__":
    conversor = Conversor()

    celsius = obter_temperatura("Digite a temperatura em graus Celsius: ")

    fahrenheit = conversor.converter_para_fahrenheit(celsius)
    print(f"A temperatura em graus Fahrenheit é: {fahrenheit:.2f}")
