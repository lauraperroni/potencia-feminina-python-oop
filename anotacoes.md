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