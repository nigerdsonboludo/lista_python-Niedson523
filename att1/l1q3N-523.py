#Lista de Exercício 1 - Questão 3
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

#3. Faça um Programa que peça dois números e imprima a soma. 

class Calculadora:
    def somar(self, num1, num2):
        return num1 + num2


def obter_numero(mensagem):
    while True:
        try:
            numero = float(input(mensagem))
            return numero
        except ValueError:
            print("Erro: O valor digitado não é um número válido.")


if __name__ == "__main__":
    calculadora = Calculadora()

    numero1 = obter_numero("Digite o primeiro número: ")
    numero2 = obter_numero("Digite o segundo número: ")

    resultado = calculadora.somar(numero1, numero2)
    print(f"A soma é: {resultado}")

        
    