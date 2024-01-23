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