#Lista de Exercício 1 - Questão 12
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58 

def calcular_peso_ideal(altura):
    peso_ideal = (72.7 * altura) - 58
    return peso_ideal


def obter_altura():
    while True:
        try:
            altura = float(input("Digite a altura da pessoa em metros: "))
            return altura
        except ValueError:
            print("Erro: O valor digitado não é uma altura válida.")


if __name__ == "__main__":
    altura = obter_altura()
    peso_ideal = calcular_peso_ideal(altura)
    print(f"O peso ideal para uma pessoa com altura {altura:.2f} metros é: {peso_ideal:.2f} kg")
