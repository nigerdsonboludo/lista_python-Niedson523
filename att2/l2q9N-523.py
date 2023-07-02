#Lista de Exercício 2 - Questão 9
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

def ordenar_numeros(num1, num2, num3):
    numeros = [num1, num2, num3]
    numeros.sort(reverse=True)
    return numeros

try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    num3 = float(input("Digite o terceiro número: "))

    numeros_ordenados = ordenar_numeros(num1, num2, num3)

    print("Números em ordem decrescente:", numeros_ordenados)

except ValueError:
    print("Erro: digite apenas números.")
