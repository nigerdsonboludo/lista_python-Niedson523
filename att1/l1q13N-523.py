#Lista de Exercício 1 - Questão 13
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7 

def calcular_peso_ideal(altura, sexo):
    if sexo.lower() == "homem":
        peso_ideal = (72.7 * altura) - 58
    elif sexo.lower() == "mulher":
        peso_ideal = (62.1 * altura) - 44.7
    else:
        raise ValueError("Sexo inválido. Informe 'homem' ou 'mulher'.")

    return peso_ideal


def obter_altura():
    while True:
        try:
            altura = float(input("Digite a altura da pessoa em metros: "))
            return altura
        except ValueError:
            print("Erro: O valor digitado não é uma altura válida.")


def obter_sexo():
    while True:
        sexo = input("Digite o sexo da pessoa (homem/mulher): ")
        if sexo.lower() in ["homem", "mulher"]:
            return sexo
        else:
            print("Erro: Sexo inválido. Informe 'homem' ou 'mulher'.")


if __name__ == "__main__":
    altura = obter_altura()
    sexo = obter_sexo()

    peso_ideal = calcular_peso_ideal(altura, sexo)
    print(f"O peso ideal para uma pessoa do sexo {sexo} com altura {altura:.2f} metros é: {peso_ideal:.2f} kg")

