#Lista de Exercício 1 - Questão 2
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

#2.Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número]. 

class Mensagem:
    def __init__(self, numero):
        self.numero = numero
    def mostrar(self):
        print(f"O número informado foi {self.numero}")
def obter_numero():
    while True:
        try:
             numero = int(input("Digite um número: "))
             return numero
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro")

def main():
        numero = obter_numero()
        mensagem = Mensagem(numero)
        mensagem.mostrar()    
if __name__ == "__main__":
    main()