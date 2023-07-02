#Lista de Exercício 2 - Questão 10
#Dupla: 2021324069 - Niedson David
#Disciplina: Programação Web
#Professor: Italo Arruda

class TurnoEstudo:
    def __init__(self, turno):
        self.turno = turno

    def saudacao(self):
        if self.turno.upper() == 'M':
            return "Bom Dia!"
        elif self.turno.upper() == 'V':
            return "Boa Tarde!"
        elif self.turno.upper() == 'N':
            return "Boa Noite!"
        else:
            return "Valor Inválido!"

try:
    turno = input("Em que turno você estuda? Digite M para matutino, V para vespertino ou N para noturno: ")

    turno_estudo = TurnoEstudo(turno)
    mensagem = turno_estudo.saudacao()

    print(mensagem)

except KeyboardInterrupt:
    print("\nPrograma interrompido pelo usuário.")
