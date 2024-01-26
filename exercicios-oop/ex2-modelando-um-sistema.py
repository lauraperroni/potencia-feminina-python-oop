'''
Exercícios Modelando um Sistema

1. O banco Banco Delas é um banco moderno e eficiente, com
vantagens exclusivas para clientes mulheres.
Modele um sistema orientado a objetos para representar contas
correntes do Banco Delas seguindo os requisitos abaixo:

    ● Cada conta corrente pode ter um ou mais clientes como
titular.

    ● O banco controla apenas o nome, o telefone e a renda
mensal de cada cliente.

    ● A conta corrente apresenta um saldo e uma lista de
operações de saques e depósitos.

    ● Quando a cliente fizer um saque, diminuiremos o saldo da
conta corrente. Quando ela fizer um depósito,
aumentaremos o saldo.

    ● Clientes mulheres possuem em suas contas um cheque
especial de valor igual à sua renda mensal, ou seja, elas
podem sacar valores que deixam a sua conta com valor
negativo até renda_mensal.

    ● Clientes homens por enquanto não têm direito a cheque
especial.

Para modelar seu sistema, utilize obrigatoriamente os conceitos
"classe", "herança", "propriedades", "encapsulamento" e "classe
abstrata".
'''

# CLASSES PRINCIPAIS ============================================================

# CLASSE CONTA ============================
class Conta:
    def __init__(self, titulares):
        self.titulares = titulares
        self.saldo = 0
        self.operacoes = []

    def depositar(self, valor):
        self.saldo += valor
        self.operacoes.append(f'Depósito de {valor} realizado.')

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append(f'Saque de {valor} realizado.')
        else:
            print("Saldo insuficiente.")

    def __str__(self):
        return f'Conta com saldo {self.saldo} e titulares: {", ".join([str(t) for t in self.titulares])}'


class Titulares:
    def __init__(self):
        self.titulares = []

    def adicionar_titular(self, cliente):
        self.titulares.append(cliente)

    def __str__(self):
        return ', '.join([str(t) for t in self.titulares])


class Cliente:
    def __init__(self, nome, telefone, renda, sexo):
        self.nome = nome
        self.telefone = telefone
        self.renda = renda
        self.sexo = sexo

    def __str__(self):
        return f'Cliente: {self.nome}, Tel: {self.telefone}, Renda: {self.renda}, Sexo: {self.sexo}'


quant = int(input('Quantos titulares esta conta vai ter? '))
titulares = Titulares()

for i in range(quant):
    nome = input(f'Digite o nome do cliente novo: ')
    telefone = int(input(f'Digite o telefone do cliente novo: '))
    renda = float(input(f'Digite a renda do cliente novo: '))
    sexo = input(f'Digite o sexo do cliente novo: ')
    cliente = Cliente(nome, telefone, renda, sexo)
    titulares.adicionar_titular(cliente)

conta = Conta(titulares)
print(conta.saldo)
print(conta)