# Módulo de python e programação orientada a objetos

## Módulos e Namespaces
Módulos são locais onde você define os nomes e funções
que quer quer fiquem visíveis para o resto do sistema.
Módulos e Namespaces

Falando tecnicamente, um módulo é um “espaço que serve
para a declaração de nomes”, ou seja, um namespace.

Em um módulo podem ser definidos componentes reutilizáveis
em outros arquivos Python. Ex: variáveis, funções, classes, etc.

Variáveis que são definidas dentro de um namespace são
chamadas de atributos.

```
versao = '0.1.1'

def mostrar_mensagem(texto):
    print(texto)
```

```
import meu_modulo

mensagem = 'Usando versão ' + meu_modulo.versao
meu_modulo.mostrar_mensagem(mensagem)
```

## Pacotes

* Instalar um pacote individualmente


```pip install colorama```

* Instalar uma lista de pacotes


```pip install -r requirements.txt```

* requirements.txt


```colorama```


## Escopo

* Variáveis declaradas dentro de uma função não podem ser acessadas fora dela. Neste caso, dizemos que a
variável é local porque ela só existe dentro do seu escopo, que é a delimitado pela função onde é declarada.
* Variáveis declaradas fora de qualquer função são chamadas de globais. Elas se encontram em um escopo que é
acessível em qualquer parte do seu script e também por outros módulos.
* Uma aplicação comum de variáveis globais é o armazenamento de valores constantes no programa, que ficam
acessíveis para a todas as funções.
* Para alterar variáveis globais dentro de funções, precisamos indicar a função que estamos querendo alterar a
variável do escopo global. Caso contrário, outra variável de mesmo nome é criada dentro do escopo da função e é
alterada apenas localmente.

```

variavel_global = 'global teste'
def minha_funcao():
    variavel_local = 'local teste'
    variavel_global = 'outro valor'
```

## Programação Orientada a Objetos

### O que é a orientação a objetos

* Até o momento, nós vimos aqui a programação tradicional. Nela, programas são listas de instruções para o computador que definem dados (através de variáveis e tipos de dados) e trabalham com esses dados usando funções.
* Dados e funções são entidades diferentes, e que precisam ser combinadas para produzir o resultado esperado.
* Por causa dessa separação, muitas vezes a programação tradicional não nos dá uma forma muito intuitiva de representar a o mundo real.
* Isso faz com que a gente crie códigos como esse aqui.
```python
muda_canal_para_cima(televisao, canal) 
```
* A programação orientada a objetos é um **paradigma** de programação diferente dessa programação tradicional.
* Podemos pensar na programação orientada a objetos como uma forma de modelar os nossos programas como objetos. Ex: televisão é um objeto, livros, são objetos, mesas são objetos...
* Objetos tem dois componentes principais: **propriedades** e **comportamentos**.
  * Propriedades: cor, forma, pesa, tamanho, etc.
  * Comportamentos: são coisas que dá pra fazer com aquele objeto.
* Exemplo: considerando o objeto televisão:
  * Propriedades: se está ligada ou não, em qual canal está, quais são os canais máximo e mínimo que são permitidos na televisão, volume.
  * Comportamentos: mudar o canal pra cima e para baixo, ligar e desligar, aumentar e reduzir o volume.
* Na programação orientada a objeitos, as propriedades e os comportametos não ficam separados, eles ficam associados ao objeto. Isso leva a códigos desse estilo:
```python
televisao.mudar_canal_para_cima()
```
* Na programação orientada a objetos (POO), objetos não são _só_ variáveis (pedaços da memória que guardam valores). Eles também são representações de algo no mundo real (sujeito/ator), e reúnem propriedades e comportamentos desse sujeito.
* Objetos são auto-contidos e reutilizáveis:
```python
televisao.ligar()
televisao.aumentar_volume()
```
* Essa forma de modelar o mundo real cria códigos claros que mostram quem é o sujeito (**objeto**) e qual é o comportamento que está sendo invocado (**método**).
  * Métodos são funções associadas a uma classe e atuam sobre um objeto.
* POO não substitui a programação tradicional – ela te dá mais ferramentas para escrever um código limpo, conciso e legível.
* POO traz novos conceitos para a linguagem: classes, herança, encapsulamento, abstrações e polimorfismo.
* Como criar meus próprios objetos em Python? Utilizando classes.
* Classes estruturas usadas para definir um novo tipo de dados (criado pela programadora). Elas descrevem o que um objeto vai ser, mas elas não criam o objeto em si.

### televisao.py
* Classes são criadas com a palavra-chave `class`.
* Conveção para nomes de classes em Python: **PascalCasing**.
* Para instanciar um objeto de uma classe, adicionamos parênteses ao nome da classe. 
  * Uma classe pode ter várias instâncias, e cada uma delas é isolada da outra e tem seus próprios atributos e métodos.
  * Chamar um método em uma instância não altera a outra.
* Toda classe tem um método especial `__init__`, que é sempre chamado quando um novo objeto daquela classe é criado.
  * O método `__init__()` é chamado de **construtor** porque ele inicializa os valores padrão do objeto.
* O primeiro parâmetro dos métodos de uma classe é chamado de `self`. Ele representa a instância sobre a qual o método vai atuar.
  * `self` dá acesso a atributos e outros métodos daquela mesma instância.
  * Não é necessário passar o parâmetro `self` ao chamar os  métodos da classe porque o interpretador faz isso aumaticamente para nós.
  * Entretanto, não se esqueça de declarar `self` como o primeiro parâmetro de seus métodos.
* Quando chamamos o método `ligar()` em uma instância, estamos alterando o estado apenas dela. A outra televisão permanece desligada.
* Se tentamos imprimir o conteúdo do objeto, visualizamos uma representação estranha. O Python mostra o tipo do objeto e o endereço da memória em que aquele objeto foi guardado.
  * Quando imprimimos um objeto do tipo `Televisao`, o interpretador Python chama o método especial `__str__()` internamente e imprime o conteúdo retornado por esse método.
  * O método especial `__str__()` permite que nós criemos uma representação em `string` para uma instância que tenha o tipo definido pela nossa classe.
* Quando digitamos o nome da variável que contém o objeto no VSCode e incluímos o ponto final `.`, o VSCode mostra uma lista de opções de métodos e atributos relativos a nossa classe.
* No módulo `datetime` da biblioteca padrão, temos as classes `datetime`, `date` e `time`.
  * Passando o mouse em cima dos nomes no `import`, podemos ver que eles são classes.


## Modelagem OOP - Slides
* Todo software usa a mesma série de etapas para resolver problemas:
1. **Entrada de dados**: os dados são lidos de algum lugar, que pode ser o armazenamento de dados como um sistema de arquivos ou um banco de dados.
2. **Processamento**: os dados são interpretados e possivelmente alterados para serem preparados para exibição.
3. **Saída de dados**: os dados são apresentados para que um usuário físico ou um sistema possa lê-los e interagir com eles.
* A programação orientada a objetos cria **modelos** do mundo em que os dados são operados.
* Os modelos possuem classes que representam objetos ou atores do mundo real, e como eles interagem entre si.
* Durante a fase de modelagem, você examina uma descrição de um domínio e tenta analisar o texto sobre o que ocorre.
* A primeira etapa é identificar os **atores**. Eles são chamados de atores porque atuam no domínio e executam uma ação.
  * Por exemplo, uma impressora (ator) imprime (ação).
  * Atores serão objetos no nosso programa, geralmente são substantivos que representam do mundo real.
* Em seguida, você examina as descrições dos atores e de todos os **dados** necessários para executar a ação.
* Após identificar atores, você examina o que eles fazem, que é o **comportamento**.
* Os atores são transformados em objetos, as características são codificadas como dados nos objetos e os comportamentos são funções que também são adicionadas ao objeto.
* A ideia é que os dados nos objetos podem ser alterados chamando funções nos próprios objetos.
* Também há a noção de que os objetos interagem uns com os outros para chegar a um resultado tangível, gerando uma saída para o nosso programa.
* Modelagem trata-se de aprender a identificar os atores, os dados necessários e o tipo de interação que está ocorrendo.
* Você pode modelar um sistema investigando sua descrição, que é relacionada as **regras de negócio**.

## Modelagem de um estacionamento - slides
* Vamos fazer a modelagem de um sistema de estacionamento.
* Para isso, vamos levantar os requisitos.
* Então a gente conversa com um dono de estacionamento e ele nos explica o seguinte:
  * O estacionamento é um pátio de apenas um andar. Ele possui 50 vagas.
  * Há 5 vagas para carros e 5 vagas para motos. Vagas para carro são maiores do que as vagas para motos.
  * Carros e motos são identificados por suas placas.
  * Vagas são identificadas por um número. Cada vaga tem um número identificador único.
  * Carros só podem ser estacionado em vagas específicas para carros.
  * Motos preferencialmente são estacionadas em vagas de motos, mas se não houver mais vagas exclusivas de motos disponíveis, motos podem ser estacionadas em vagas de carros.
  * É preciso ter controle sobre qual carro está em qual vaga para agilizar a saída quando o dono vem buscar.
  * É preciso saber o número de vagas livres de carro e de moto para que o estacionamento saiba se pode novos carros e motos.
* O primeiro passo é identificar os atores, ou seja, os substantivos que vão se transformar em classes no nosso sistema.
  * Estacionamento, Carro, Moto e Vaga.
* Em seguida, identificamos os atributos de cada ator.
  * Estacionamento: vagas de carro, vagas de moto, carro_para_vaga, moto_para_vaga, total_de_vagas_livres_carro, total_de_vagas_livres_moto
  * Carro: placa
  * Moto: placa
  * Vaga: identificador, tipo
* Vamos então olhar identificar quem vao ser os dados de entrada, o processamento e a saída do nosso programa:
  * Em nosso sistema, a entrada vai ser um conjunto de carros (pode ser uma lista cheia de objetos dos tipos `Carro` e `Moto`, um dicionário, etc).
  * O processamento vai cuidar do estacionamento, sendo responsável por atualizar a entrada e saída de carros.
  * Ainda precisamos de algum tipo de controle para evitar que o mesmo objeto de carro o moto seja estacionado duas vezes dentro do estacionamento. Para isso, adicionamos um atributo `estacionado` nas classes `Carro` e `Moto` que será um valor booleano atualizado pelos métodos `estacionar()` e `sair_da_vaga()`.
  * Também precisamos de uma forma de mostrar qual é o estado atual do estacionamento, que é a nossa saída. Para isso, adicionamos o método `estado_do_estacionamento()` na classe `Estacionamento`.


## estacionamento.py
* Este módulo define as classes `Estacionamento`, `Carro`, `Moto` e `Vaga` que nós discutimos.
* As classes `Carro` e `Moto` são muito semelhantes.
* A classe `Vaga` recebe em seu construtor qual é o tipo daquela vaga, e possui métodos para realizar a sua ocupação e desocupação, salvando a placa do veículo que está ocupando a vaga no momento.
* A lógica mais interessante se concentra na classe `Estacionamento`:
  * O construtor inicializa os atributos que nós vimos anteriormente.
  * Utilizamos o método `inicializar_vagas` para preencher os dicionários `vagas_carro` e `vagas_motos` com objetos do tipo `Vaga`, onde cada chave é o identificador de vaga e cada valor é um objeto do tipo `Vaga`.
  * O primeiro `id` de vaga de moto é o próximo valor inteiro depois do  último `id` da vaga de carro.
  * O método `estacionar_carro()` busca a primeira vaga de carro livre na coleção de vagas de carro.
    * Se ele não encontra nenhuma vaga livre, uma exceção é lançada.
    * Se encontra, ele atualiza todas os atributos necessários para realizar o controle de ocupação da vaga.
    * O dicionário `carro_para_vaga` mantém um dicionário para agilizar a busca de em qual vaga o carro foi estacionado. 
  * O método `estacionar_moto()` funciona de forma semelhante, mas precisa levar em conta que motos podem ser estacionadas em vagas de carro caso todas as vagas de moto já estejam ocupadas.
  * O método auxiliar `buscar_id_da_proxima_vaga_livre()` inclui a lógica para buscar vagas de carro e de moto. É nele que incluímos a lógica que tenta buscar o identificador de vagas de moto e, em seguida, de carros caso não tenhamos vagas de moto livres.
  * Os métodos `remover_carro()` e `remover_moto()` encontram em qual vaga o veículo está estacionado e atualizam os valores de atributos pertinentes a remoção de veículo da vaga.
  * Finalmente, o estado do estacionamento é mostrado através de uma `string`.
  * Adicionamos o método especial `__str(self)__` para poder imprimir o estado do estacionamento com a função `print()`.


## modelagem.py
* Agora vamos utilizar as classes que criamos para simular um sistema de estacionamento.
* Começamos incluindo todas as classes do módulo `estacionamento` no _namespace_  corrente, já que vamos utilizar todas elas.
* Criamos duas listas: uma de carros e uma de motos. Utilizamos a biblioteca `random` para gerar valores inteiros aleatórios que representem as placas dos veículos.
* Em seguida, testamos as lógicas que criamos.

* O destrutor é chamado quando todas as referências para o objeto são extintas ou quando a execução do programa é encerrada.

# Aula 4 - Construtores e Destrutores

## 01_construtores.py
* Nós já vimos exemplos de métodos construtores nas aulas passadas.
* Construtores são métodos especiais que são chamados durante a instanciação de um objeto.
* A função de um construstor é inicializar valores aos dados que são membros da classe quando uma instância é criada.
* O método `__init__()` é chamado construtor e é sempre chamado quando um objeto é criado.
* Se você não definir o método construtor explicitamente, o interpretador faz isso automaticamente por baixo dos panos, criando o **construtor padrão**.
* O construtor **construtor padrão** é o método `__init__(self)` que não aceita nenhum argumento além do `self`.
* O construtor também pode ser customizado para receber parâmetros. Neste caso, ele deixa de ser o construtor padrão e se torna um **construtor parametrizado**.
  * Ao declarar um construtor parametrizado, o interpretador python não cria mais outro construtor na classe.

## 02_destrutores.py
* Destrutores são métodos análogos aos construtores, só que para o objetivo oposto: eles são executados quando um objeto é destruído.
* A função de um destrutor é liberar a memória que o objeto estava usando quando ela não é mais necessária.
* Objetos desnecessários são excluídos automaticamente. Isso libera o espaço de memória conhecido como **coleta de lixo**.
* O nome de um método destrutor é `__del__(self)`.
* Assim como o construtor padrão, o destrutor é criado automaticamente pelo interpretador Python na classe e também é **chamado automaticamente**.
  * Isso tira do programador a responsabilidade sobre o gerenciamento direto da memória ocupada pelo programa.
* O destrutor é chamado quando todas as referências para o objeto são extintas ou quando a execução do programa é encerrada.
  * Quando um programa termina, o **coletor de lixo** do python destrói todos os objetos em memória. Esta é a última coisa que acontece durante a execução.
* Em geral, não é comum ver destrutores em códigos Python porque eles são executados automaticamente. Ainda assim é importante ter a noção de que eles existem, porque isso ajuda a entender melhor o que está acontecendo enquanto o seu programa está rodando.

# Aula 6 - Herança e Herança Múltipla

## heranca.py
* A classe `Estudante` herda da classe `Pessoa`. A sintaxe para indicar isso é colocar o nome da "classe pai" dentro de um parênteses na frente do nome da "classe filha".
* Os métodos e variáveis da classe pai podem ser acessados com a função `super()`.
* É uma boa prática sempre chamar o construtor da classe pai no construtor da classe filha. É ele que garante que as propriedades da classe pai vão ser inicializadas corretamente.
* A classe `Estudante` herda os métodos e as propriedades públicas e protegidas da classe `Pessoa`.
* A classe `Estudante` pode sobrescrever os valores que foram herdados.
* Python provê funções nativas para testar se um objeto é instância de uma determinada classe, e se uma classe é derivada de outra.
* A classe `Trabalhador` também herda de `Pessoa`, e a classe `Professor` herda de trabalhador.
* `Professor` é um `Trabalhador` e também é uma `Pessoa`, portanto herda métodos e atributos de ambos.
* Atributos privados não podem ser alterados em classes filhas.
* Em Python, todas as classes herdam da classe `object`. Isso faz com que toda classe já comece com vários métodos e atributos.
* A função `dir()` mostra os atributos e métodos de um determinado objeto ou classe. Notem que as propriedades privadas aparecem aqui também, mas com nomes diferentes.

# Herança múltipla - Slide
* Em Python, uma classe pode herdar de mais de uma classe pai. Esse conceito é conhecido como herança múltipla.
* As vezes, classes que herdam de mais de uma classe são chamadas de **mixins**.
* Heraça múltipla é uma funcionalidade muito controversa, porque o uso dessa funcionalidade traz potencialmente muita complexidade para o código.
* Na maior parte das vezes onde alguém tenta resolver um problema com herança múltipla, existiriam soluções melhores e mais simples.
* O caso de uso mais legítimo é na criação de um _framework_.
* Ao trabalhar com Django, vocês podem ver casos onde uma classe vai herdar de duas ou mais classes.

# heranca_multipla.py
* A classe `Logavel` define o método `logar`. Qualquer classe que herdar dela vai conseguir escrever uma mensagem no log e nós vamos saber de onde a mensagem está vindo pelo atributo `nome_da_classe` que é inicializado no construtor.
  * Ter uma classe assim é interessante porque a lógica de criar um arquivo de log, escrever as mensagens dentro dele e fechar o arquivo depois fica todo em um lugar só.
  * Quem está escrevendo um software não precisa se preocupar em escrever essa lógica toda vez, é só herdar de `Logavel`.
* A classe `Conexao` serve para conectar a um servidor de banco de dados.
  * O servidor costuma ser um endereço de IP com uma porta.
* A classe `MySqlDatabase` é uma classe de exemplo que se conecta ao banco de dados **MySql**, que herda tanto de conexão quanto de logável.
* O meu `framework` super chique aqui é só um metódo que recebe um objeto chamado `item` e testa se esse objeto é uma instância de cada uma das classes. Ele só chama os métodos pertinentes se for.


# Aula 7 - Classes Abstratas

## Classes abstratas
* Uma classe abstrata pode ser considerada como um modelo para criar outras classes. 
* Em uma classe abstrata, nós criamos um conjunto de métodos que devem ser implementados dentro de qualquer classe filha criada a partir da classe abstrata.
* Um método abstrato é um método que tem uma declaração, mas não tem uma implementação.
* Uma classe que contém um ou mais métodos abstratos é chamada de classe abstrata.
* Não é possível instanciar uma classe abstrata diretamenta. Para criar um objeto do tipo de uma classe abstrata, precisamos instanciar uma das classes filhas.
* Enquanto estamos projetando grandes unidades funcionais, usamos uma classe abstrata. A ideia é fornecer uma interface comum para diferentes implementações de um componente, que vai ser representado pelas suas classes filhas.
* Python tem o módulo `ABC` (_Abstract Base Classes_) que fornece a funcionalidade de classes abstratas. A classe abstrata precisa herdar de `ABC` e métodos abstratos são marcados com o _decorator_ `@abstractmethod`.
* Uma classe filha derivada de uma classe abstrata precisa implementar todos os métodos e propriedades abstratas. Caso contrário, não é possível criar objetos da classe filha.

**Por que usar classes abstratas?**
* Ao criar classes abstratas, você define uma interface comum para que todas as classes filhas sigam, ou seja, as classes abstratas são usadas para definir a **API** de suas classes filhas.
* Definir uma API é uma capacidade importante na área de projeto e arquitetura de software.
* Você pode estar desenvolvendo uma biblioteca de Python que vai prover a definição de uma API que vai ser implementada por outros desenvolvedores.
* Outro caso de uso é o trabalho em uma equipe/empresa grande que vai precisar criar componentes que fazem coisas semelhantes em diferentes partes do software. Geralmente, um arquiteto define a API que deve ser seguida pelos diferentes componentes.
* Isso vai ficar mais claro com um exemplo.

## classes_abstratas.py
* Vamos supor que nós estamos desenvolvendo um jogo da franquia Pokémon.
* Pokémon é uma franquia grande e conhecida por ter vários jogos lançados. Novos jogos costumam trazer novos pokémons, que ainda não eram conhecidos anteriormente.
* O arquiteto de software precisa garantir que todas as classes que definem um pokemon sigam uma determinada API, que vai contér o ataque principal daquele pokemon, um método para garantir sua evolução e uma propriedade que guarda o seu tipo.
* A classe `BasePokemon` herda da classe `ABC` e se torna assim uma classe abstrata.
* Se tentarmos criar um objeto do tipo da classe base, não vamos conseguir.
* Criamos uma classe `Pikachu` que vai herdar de `BasePokemon`. Essa classe vai precisar definir no mínimo todos os métodos e propriedades abstratas da classe base.
* Notem que definimos sem as marcações de abstrato. Essas marcações só existem na classe base.
* Se algum dos métodos não for implementado, não conseguiremos instanciar o objeto da classe `Pikachu`.
* Novos métodos podem ser adicionados nas classes derivadas.


# Aula 7 - Tipagem Pato (_Duck Typing_)

* Quando inicializamos uma variável em python, podemos começar associando a ela um tipo (por exemplo, um inteiro).
* Depois podemos fazer a mesma variável apontar para um objeto de outro tipo (por exemplo, uma string).
```python
a = 1
a = "Maria"
```
* Isso acontece porque Python é uma linguagem que possui tipagem dinâmica.
* Em linguagens com tipagem dinâmica, o tipo de uma variável é determinado em tempo de execução, ou seja, durante a execução do programa.
* Como as variáveis não ficam "presas" a um tipo específico de dado, quando definimos uma função, não conseguimos ter certeza de qual o tipo de dados que vai ser passado como parâmetro.
* Essa forma de funcionamento é um contraste com o que acontece em linguagens com tipagem estática.
* Em linguagens com tipagem estática, o tipo de uma variável é determinado em tempo de compilação, ou seja, antes da execução do programa.
* Muitas linguagens de programação não funcionam assim. Por exemplo, em Java, o tipo de uma variável é definido no momento em que ela é criada e não pode ser alterado.

```python
def processar(animal):
    animal.quack()
    animal.andar()
    animal.voar()
    animal.nadar()
```
* A função `processar` recebe um parâmetro chamado `animal`. No entanto, a função não tem como garantir que o animal é de algum tipo específico, por exemplo, o tipo `Pato`.
* A única forma de saber se o animal faz tudo que precisamos é testar se o objeto possui todos os métodos que precisamos.
* Se o objeto passado como parâmetro possuir todos os métodos que precisamos, podemos dizer que ele é um pato.
* Esse conceito é chamado de **tipagem pato** (_duck typing_).
```
Se andar como um pato, fazer quack como um pato e voar como um pato, então é um pato.
```
* Ao fazermos isso, estamos testando durante a execução do programa se o objeto passado como parâmetro possui os métodos que precisamos sem saber se isso é realmente verdade.
* Para nós, o que importa é que o objeto se comporte como um pato. Se ele se comporta como um pato, ou seja, se possui todos os métodos esperados do tipo 'Pato', então isso é o suficiente para dizer que ele é do tipo `Pato`, ao invés de checar o tipo diretamente.