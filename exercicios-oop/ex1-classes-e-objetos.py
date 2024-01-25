''' Exercícios Classes e Objetos

1. Crie uma classe que modele o objeto "carro".
2. Um carro tem os seguintes atributos: ligado, cor, modelo,
velocidade.
3. Um carro tem os seguintes comportamentos: liga, desliga, acelera,
desacelera.
4. Crie uma instância da classe carro.
5. Faça o carro "andar" utilizando os métodos da sua classe.
6. Faça o carro "parar" utilizando os métodos da sua classe. 

'''

class Carro:
    def __init__(self):
        self.ligado = ''
        self.cor = ''
        self.modelo = ''
        self.velocidade = 0
        self.estado = ''


    def ligar(self):
        if self.ligado != 'Ligado':
            self.ligado = 'Ligado'
        else:
            print('Não dá para ligar um carro que já está ligado!')

    def desligar(self):
        if self.ligado != 'Desligado':
            self.ligado = 'Desligado'
        else:
            print('Não dá para desligar um carro que já está desligado!')

    def andar(self):
        if self.ligado != 'Desligado':
            self.estado = 'Andando'
            self.velocidade += 1
        else:
            print('Não dá para andar com um carro desligado!')

    def parar(self):
        self.estado = 'Parado'
        self.velocidade = 0

    def __str__(self) -> str:
        return f'O carro de cor {self.cor} e modelo {self.modelo} está {self.ligado} e está {self.estado}, sua velocidade é {self.velocidade}'

carro = Carro()

carro.cor = 'vermelho'
carro.modelo = 'miata'
carro.ligar()
carro.andar()
print(carro)

carro.desligar()
carro.parar()
print(carro)

carro.ligar()
print(carro)







