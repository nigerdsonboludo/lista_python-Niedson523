#Lista de Exercício 1 - Questão 14
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

#oão Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas. 

def calcular_excesso_multa(peso_peixes):
    limite_peso = 50.0
    excesso = 0.0
    multa_por_quilo = 4.0
    multa = 0.0

    if peso_peixes > limite_peso:
        excesso = peso_peixes - limite_peso
        multa = excesso * multa_por_quilo

    return excesso, multa


def obter_peso_peixes():
    while True:
        try:
            peso_peixes = float(input("Digite o peso dos peixes em quilos: "))
            return peso_peixes
        except ValueError:
            print("Erro: O valor digitado não é um peso válido.")


if __name__ == "__main__":
    peso_peixes = obter_peso_peixes()

    excesso, multa = calcular_excesso_multa(peso_peixes)

    if excesso > 0:
        print(f"Peso dos peixes excedido: {excesso:.2f} kg")
        print(f"Valor da multa a ser paga: R$ {multa:.2f}")
    else:
        print("Peso dos peixes dentro do limite. Sem multa a pagar.")
