# Python by DayCardoso

# Linguagem de programação Python

### ****O que é Python?****

Descubra o que é a linguagem de programação Python e como ela pode ser usada.

- Python é uma linguagem de programação de alto nível. É fácil de aprender e tem uma sintaxe simples, o que a torna uma ótima linguagem para iniciantes.
- Python é usado para tarefas como web development, machine learning, data science, e muito mais.
- É compatível com sistemas operacionais como Windows, Mac OS e Linux.
- Python tem bibliotecas poderosas que permitem que os programadores criem programas complexos rapidamente.
- Python também tem frameworks como Django e Flask, que permitem que os programadores criem aplicativos web rapidamente.
- Python é uma **linguagem interpretada**. ***Interpretado*** significa que não há um processo de compilação que traduz o código fonte em algum código nativo, que o seu computador entende. A [documentação do Python](https://docs.python.org/3/glossary.html) confirma isso, no entanto também menciona a presença de um compilador:
    
    > ***"Python is an interpreted language, as opposed to a compiled one, though the distinction can be blurry because of the presence of the bytecode compiler."***
    > 
    
    > Traduzido livremente: **"Python é uma linguagem interpretada, em oposição às compiladas, embora a distinção possa ficar desfocada devido à presença do compilador de bytecode."**
    > 

### Operações Escalares

| Operação | Operador | Exemplo |
| --- | --- | --- |
| Adição | + | 2 + 2 = 4 |
| Subtração | - | 4 - 2 = 2 |
| Multiplicação | * | 2 * 2 = 4 |
| Divisão | / | 10 / 2 = 5 |
| Módulo | % | 11 % 5 = 1 |
| Exponenciação | ** | 2 ** 3 = 8 |
| Divisão inteira | // | 3 // 2 = 1 |

### Operadores Relacionais

| Significado | Operador |
| --- | --- |
| Igual a | == |
| Diferente de | != |
| Maior que | > |
| Menor que | < |
| Maior ou igual que | >= |
| Menor ou igual que | <= |

### Operadores lógicos

| Significado | Operador | Sintaxe |
| --- | --- | --- |
| E | and | x and y |
| OU | or | x or y |
| Negado | not | not x |

### Tipos de Variáveis

```
class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def __lt__(self, outra):
        if self.idade != outra.idade:
            return self.idade < outra.idade
        return self.nome < outra.nome

pessoas = [Pessoa("João", 35, "Rua A"), Pessoa("Maria", 30, "Rua B"), Pessoa("Pedro", 40, "Rua C")]

for pessoa in sorted(pessoas):
    print(pessoa.nome, pessoa.idade)
```

<aside>
💡 O Python utiliza por convenção o padrão **s*nake_case*** para nomes de variáveis (ou identificadores).

Um exemplo de variáveis em **s*nake_case*** são:

```python
idade_esposa = 20
perfil_vip = 'Flávio Almeida'
recibos_em_atraso = 30
```

</aside>

| Tipo de Variável | Formato | Sintaxe | Exemplo |
| --- | --- | --- | --- |
| Inteiro (int) | Números Inteiros | x = int(5) | x = 5 |
| Ponto Flutuante ou Decimal (float) | Números Decimais | x = float(3.14) | x = 3.14 |
| Complexo (complex) | Números Complexos | x = complex(1j) | x = 1j |
| String (str) | Sequências de Caracteres | x = str("Hello World") | x = "Hello World" |
| Boolean (bool) | Valores Verdadeiro ou Falso | x = bool(True) | x = True |
| Listas (list) | Sequências Mutáveis | x = list(["Apple", "Banana", "Cherry"]) | x = ["Apple", "Banana", "Cherry"] |
| Tuplas (tuple) | Sequências Imutáveis | x = tuple(("Apple", "Banana", "Cherry")) | x = ("Apple", "Banana", "Cherry") |
| Dicionários (dict) | Coleções Não-Ordenadas | x = dict({"name": "John", "age": 36}) | x = {"name": "John", "age": 36} |

### Tabela de Formatação de Numérica

Python possui um método simples e intuitivo para formatar números. O método `format()` pode ser usado para formatar os números para vários fins, como mostrado na tabela a seguir:

| Formato | Descrição |
| --- | --- |
| {:f} | Formata o número como um número de ponto flutuante com o número padrão de casas decimais. |
| {:.2f} | Formata o número como um número de ponto flutuante com 2 casas decimais. |
| {:.3f} | Formata o número como um número de ponto flutuante com 3 casas decimais. |
| {:d} | Formata o número como um inteiro. |
| {:x} | Formata o número como uma representação hexadecimal. |
| {:b} | Formata o número como uma representação binária. |

**Exemplo**:

```python
numero = 3.14159

print(f"O número é {numero:f}") # O número é 3.141590
print(f"O número é {numero:.2f}") # O número é 3.14
print(f"O número é {numero:.3f}") # O número é 3.142
print(f"O número é {numero:d}") # O número é 3
print(f"O número é {numero:x}") # O número é b.a
print(f"O número é {numero:b}") # O número é 11.1001000010101111111010100001010

```

### Funções Trigonométricas

A seguir, está uma tabela das principais funções trigonométricas em Python.

| Função | Descrição | Sintaxe |
| --- | --- | --- |
| sin | Seno | np.sin(x) |
| cos | Cosseno | np.cos(x) |
| tan | Tangente | np.tan(x) |
| arcsin | Seno inverso | np.arcsin(x) |
| arccos | Cosseno inverso | np.arccos(x) |
| arctan | Tangente Inversa | np.arctan(x) |
| sinh | Seno hiperbólico | np.sinh(x) |
| cosh | Cosseno hiperbólico | np.cosh(x) |
| tanh | Tangente hiperbólica | np.tanh(x) |
| arcsinh | Seno hiperbólico inverso | np.arcsinh(x) |
| arccosh | Cosseno hiperbólico inverso | np.arccosh(x) |
| arctanh | Tangente hiperbólica inverso | np.arctanh(x) |
| radians | Converte de graus para radianos | np.radians(x) |
| degrees | Converte de radianos para graus | np.degrees(x) |

## Principais Built-in Functions

| Função | Descrição | Sintaxe Básica |
| --- | --- | --- |
| abs() | Retorna o valor absoluto de um número | abs(x) |
| aiter() | Retorna um iterador de async | aiter(x) |
| all() | Retorna se todos os elementos são verdadeiros ou se a coleção está vazia | all(iterable) |
| any() | Retorna se qualquer elemento é verdadeiro ou se a coleção está vazia | any(iterable) |
| anext() | Retorna o próximo valor de um iterador de async | anext(iterator[, default]) |
| ascii() | Retorna uma representação de string de objetos | ascii(obj) |
| bin() | Retorna a representação binária de um inteiro | bin(x) |
| bool() | Retorna o valor booleano de um objeto | bool([x]) |
| breakpoint() | Entra em um modo de depuração | breakpoint() |
| bytearray() | Retorna um array de bytes mutável | bytearray(source[, encoding[, errors]]) |
| bytes() | Retorna um array de bytes imutável | bytes(source[, encoding[, errors]]) |
| callable() | Retorna se um objeto é chamável | callable(obj) |
| chr() | Retorna um string de caractere de um inteiro | chr(i) |
| classmethod() | Retorna um método de classe | classmethod(function) |
| compile() | Compila o código em um objeto de código | compile(source, filename, mode[, flags[, dont_inherit]]) |
| complex() | Retorna um número complexo | complex([real[, imag]]) |
| delattr() | Deleta um atributo de um objeto | delattr(object, name) |
| dict() | Cria um dicionário | dict(**kwarg) |
| dir() | Retorna uma lista de atributos e métodos de um objeto | dir([object]) |
| divmod() | Retorna a divisão inteira e o resto de dois números | divmod(a, b) |
| enumerate() | Retorna um iterador de tuplas contendo índice e valor | enumerate(iterable[, start]) |
| eval() | Avalia um expressão | eval(expression[, globals[, locals]]) |
| exec() | Executa código de Python | exec(object[, globals[, locals]]) |
| filter() | Retorna um filtro de um iterável | filter(function, iterable) |
| float() | Retorna um float de um número ou string | float([x]) |
| format() | Retorna uma string formatada | format(value[, format_spec]) |
| frozenset() | Retorna um conjunto imutável | frozenset(iterable) |
| getattr() | Retorna o valor de um atributo de um objeto | getattr(object, name[, default]) |
| globals() | Retorna o dicionário global | globals() |
| hasattr() | Retorna se um atributo existe em um objeto | hasattr(object, name) |
| hash() | Retorna o valor de hash de um objeto | hash(object) |
| help() | Exibe a documentação de um objeto | help([object]) |
| hex() | Retorna a representação hexadecimal de um inteiro | hex(x) |
| id() | Retorna o identificador único de um objeto | id(object) |
| input() | Leitura de dados de entrada | input([prompt]) |
| int() | Retorna um inteiro de um número ou string | int([x[, base]]) |
| isinstance() | Retorna se um objeto é uma instância de uma classe | isinstance(object, classinfo) |
| issubclass() | Retorna se uma classe é subclasse de outra | issubclass(class, classinfo) |
| iter() | Retorna um iterador | iter(object[, sentinel]) |
| len() | Retorna o tamanho de um objeto | len(s) |
| list() | Retorna uma lista de um iterável | list(iterable) |
| locals() | Retorna um dicionário contendo variáveis locais | locals() |
| map() | Retorna um mapa de um iterável | map(function, iterable) |
| max() | Retorna o maior elemento de um iterável | max(iterable[, *args[, key]]) |
| memoryview() | Retorna uma visão de memória de um objeto | memoryview(obj) |
| min() | Retorna o menor elemento de um iterável | min(iterable[, *args[, key]]) |
| next() | Retorna o próximo elemento de um iterador | next(iterator[, default]) |
| object() | Retorna um novo objeto | object() |
| oct() | Retorna a representação octal de um inteiro | oct(x) |
| open() | Retorna um arquivo | open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None) |
| ord() | Retorna o inteiro Unicode de um caractere | ord(c) |
| pow() | Retorna o resultado de x elevado a y | pow(x, y[, z]) |
| print() | Imprime os argumentos na saída padrão | print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False) |
| property() | Retorna um propriedade de um objeto | property(fget=None, fset=None, fdel=None, doc=None) |
| range() | Retorna um sequência de números | range(start, stop[, step]) |
| repr() | Retorna uma representação de string de um objeto | repr(object) |
| reversed() | Retorna um iterador reverso | reversed(sequence) |
| round() | Retorna um número arredondado | round(number[, ndigits]) |
| set() | Retorna um conjunto de um iterável | set(iterable) |
| setattr() | Define um atributo de um objeto | setattr(object, name, value) |
| slice() | Retorna um slice de um objeto | slice(start, stop[, step]) |
| sorted() | Retorna uma lista ordenada de um iterável | sorted(iterable[, key][, reverse]) |
| staticmethod() | Retorna um método estático | staticmethod(function) |
| str() | Retorna uma string de um objeto | str(object='') |
| sum() | Retorna a soma de elementos de um iterável | sum(iterable[, start]) |
| super() | Retorna um objeto proxy para superclasses | super([type[, object-or-type]]) |
| tuple() | Retorna uma tupla de um iterável | tuple(iterable) |
| type() | Retorna o tipo de um objeto | type(object) |
| vars() | Retorna o dicionário de variáveis de um objeto | vars([object]) |
| zip() | Retorna um iterador de tuplas | zip(*iterables) |
| import() | Importa um módulo | import(name[, globals[, locals[, fromlist[, level]]]]) |

## Imprimir

Imprime os valores em um fluxo ou em sys.stdout por padrão.

```python
print(*args, sep=' ', end='\n', file=None, flush=False)
```

`set`string inserido entre valores, padrão um espaço.
`end`string acrescentado após o último valor, o padrão é uma nova linha.
`file`um objeto tipo arquivo (stream); o padrão é o sys.stdout atual.
`flush`se forçar a descarga do fluxo

### Interpolação de String em Python

A interpolação de strings é uma prática comum na programação que permite aos programadores inserir variáveis em strings usando sintaxe simples e intuitiva. Isso é muito útil para criar strings de saída personalizadas com dados de entrada.

No Python, a interpolação de strings é feita usando a sintaxe `f-string`. Esta é uma maneira concisa e poderosa de adicionar variáveis às strings. A sintaxe é simples: basta inserir o nome da variável dentro de chaves `{}` dentro da string, como mostrado abaixo.

```python
nome = "João"
print(f"Olá, {nome}!") # Olá, João!
```

A interpolação de strings também pode ser usada para formatar números e datas usando o método `format()`. Por exemplo, para formatar um número decimal para ter 3 casas decimais, você pode usar o seguinte código:

```python
numero = 3.14159
print(f"O número é {numero:.3f}") # O número é 3.142
```

A interpolação de strings é uma técnica útil que pode ajudar a tornar seu código mais legível e conciso. É uma prática comum utilizada por programadores experientes e vale a pena aprender.

## Como Importar Bibliotecas em Python

O Python possui um enorme conjunto de bibliotecas pré-instaladas que podem ser usadas para realizar tarefas específicas. Essas bibliotecas incluem módulos, classes, funções e outras variáveis que podem ser usadas para realizar tarefas específicas. Para usar uma biblioteca, ela primeiro precisa ser importada no programa.

O Python possui diversos métodos para importar bibliotecas, tais como:

- **`import`** - Esta é a forma mais simples de importar uma biblioteca. Esta sintaxe importa todo o conteúdo da biblioteca para o seu programa. Sintaxe:

```python
import nome_da_biblioteca

# Exemplo:

import pandas

```

- **`from`** - Esta sintaxe permite importar apenas partes específicas de uma biblioteca, como módulos, classes ou funções. Sintaxe:

```python
from nome_da_biblioteca import nome_do_modulo

# Exemplo:

from pandas import DataFrame

```

- **`as`** - Esta sintaxe permite dar um novo nome à biblioteca importada. Isso é útil se você quiser usar uma abreviatura para a biblioteca. Sintaxe:

```python
import nome_da_biblioteca as abreviatura

# Exemplo:

import pandas as pd

```

Com esses métodos, você pode importar qualquer biblioteca necessária para o seu programa e começar a aplicar seu conhecimento.

## Como Definir uma Função em Python

Em Python, uma função é definida usando a palavra-chave `def` seguida do nome da função e de parênteses contendo os parâmetros. Os parâmetros são variáveis que serão usadas dentro da função. A sintaxe básica é a seguinte:

```python
def nome_da_função(parametros):
    declarações

```

**Exemplo**:

```python
def soma(a, b):
    return a + b

```

No exemplo acima, a função `soma()` recebe dois parâmetros `a` e `b` e retorna a soma deles. A função pode então ser chamada passando dois números como argumentos.

```python
resultado = soma(2, 3)

# Saída:
# 5

```

Além disso, as funções podem ter argumentos opcionais, que são argumentos que podem ou não ser passados para a função.

```python
def soma(a, b, c=0):
    return a + b + c

```

No exemplo acima, a função `soma()` tem um argumento opcional `c`. Se nenhum valor for passado para `c`, o valor padrão será 0.

```python
resultado = soma(2, 3)

# Saída:
# 5

```

Com esses conceitos básicos, você pode definir funções para realizar qualquer tarefa desejada.

## List Comprehension

List Comprehension é uma ferramenta poderosa que permite aos programadores Python criar listas de forma eficiente. É uma notação de simplificação que permite que você crie listas, dicionários e conjuntos usando uma sintaxe concisa. A sintaxe básica de uma List Comprehension é a seguinte:

```python
[expressão for item in lista if condição]
```

A **expressão** é aplicada a cada **item** da **lista** e é inserida na nova lista se a **condição** for verdadeira.

Por exemplo, imagine que você tem uma lista de números e quer criar uma nova lista com apenas os números pares:

**Exemplo**:

```python
# Cria uma lista de números inteiros
inteiros = [1, 2, 3, 4, 5]

# Usando List Comprehension para criar uma lista de números ao quadrado
quadrados = [x**2 for x in inteiros]

# Saída:
# [1, 4, 9, 16, 25]

```

No exemplo acima, a expressão `x**2` é aplicada a cada item na lista inteiros, e os resultados são adicionados à lista quadrados.

- Além disso, também é possível usar condicionais para filtrar os resultados:

```python
# Cria uma lista de números inteiros
inteiros = [1, 2, 3, 4, 5]

# Usando List Comprehension para criar uma lista de números pares
pares = [x for x in inteiros if x % 2 == 0]

# Saída:
# [2, 4]

```

No exemplo acima, a condicional `x % 2 == 0` é usada para filtrar os resultados e adicionar apenas os números pares à lista pares.

- List Comprehension também é útil para trabalhar com estruturas de dados mais complexas, como dicionários. Por exemplo, imagine que você tem um dicionário de pessoas e quer criar uma nova lista com apenas os nomes:

```python
pessoas = {
    "Alice": 25,
    "Bob": 30,
    "Charlie": 35
}
nomes = [nome for nome, idade in pessoas.items()]
print(nomes) 

# Saída:
# ['Alice', 'Bob', 'Charlie']
```

- Um exemplo de List Comprehension mais complexo:

Imagine que você tem uma lista de strings que representam os nomes de pessoas e outra lista que representa suas idades. E você quer criar uma lista de dicionários que tenham nome e idade como chaves:

```python
nomes = ["Alice", "Bob", "Charlie", "David"]
idades = [25, 30, 35, 40]
pessoas = [{"nome": nome, "idade": idade} for nome, idade in zip(nomes, idades)]
print(pessoas)
# [{'nome': 'Alice', 'idade': 25},#  {'nome': 'Bob', 'idade': 30},#  {'nome': 'Charlie', 'idade': 35},#  {'nome': 'David', 'idade': 40}]
```

Neste exemplo, usamos a função **`zip`** para combinar as duas listas **`nomes`** e  **`idades`** em um único iterável e, em seguida, usamos a List Comprehension para criar a lista de dicionários **`pessoas`**. Observe como a List Comprehension permite que você crie uma nova estrutura de dados a partir de duas listas diferentes de forma concisa e elegante.

<aside>
<img src="https://www.notion.so/icons/light-bulb_orange.svg" alt="https://www.notion.so/icons/light-bulb_orange.svg" width="40px" /> A List Comprehension é uma ferramenta versátil e poderosa para criar listas em Python. Ela é muito útil para codificação rápida e eficiente e para manipulação de dados de uma forma concisa e legível.

</aside>

## Como Importar um arquivo python para dentro de outro arquivo python?

Python possui um mecanismo para importar arquivos dentro de outros arquivos, conhecido como importação de módulos. Para importar um arquivo para dentro de outro, você deve usar o comando `import`. Por exemplo, para importar o arquivo `arquivo.py` em outro arquivo, você usaria o seguinte comando:

```python
import arquivo

```

Também é possível importar apenas partes de um arquivo, usando o comando `from`. Por exemplo, para importar uma função específica do arquivo `arquivo.py`, você usaria o seguinte comando:

```python
from arquivo import nome_da_função

```

Se você deseja importar todas as funções de um arquivo, você pode usar o seguinte comando:

```python
from arquivo import *

```

É importante observar que, quando você importa um arquivo, você não está executando seu código. O código só é executado quando você chama uma função ou classe definida no arquivo importado.

# Condicionais em Python 3.11

Uma função condicional é um conjunto de regras que informam ao computador como reagir a um determinado conjunto de dados. Em Python, podemos usar as instruções condicionais para controlar o fluxo de execução de um programa.

### Lista das funções condicionais

- **`if`** - Esta é a instrução mais comum usada no Python para fazer um teste lógico. Se a condição for verdadeira, então a declaração relacionada é executada. Sintaxe:
    
    ```python
    if condição:
        declaração
    
    #ou:
    
    if(acertou):
        print("Parabéns! Você acertou.")
    ```
    
    **Exemplo**:
    
    ```python
    if x > 0:
      print("x é positivo")
    ```
    
- **`if-else**` - Esta é uma estrutura condicional usada para especificar duas possíveis ações, uma para quando a condição é verdadeira e outra para quando ela é falsa. Sintaxe:
    
    ```python
    if condição:
        declaração
    else:
        declaração
    ```
    
    **Exemplo**:
    
    ```python
    if x > 0:
      print("x é positivo")
    else:
      print("x é negativo")
    ```
    
- **`elif`** - Esta é uma instrução condicional usada para especificar uma série de possíveis condições e seus respectivos resultados. Sintaxe:
    
    ```python
    if condição:
        declaração
    elif condição:
        declaração
    ```
    
    **Exemplo**:
    
    ```python
    if x > 0:
      print("x é positivo")
    elif x < 0:
      print("x é negativo")
    ```
    
- **`while`** - Esta instrução é usada para especificar um laço de repetição. O laço continua a ser executado enquanto a condição for verdadeira. Sintaxe:
    
    ```python
    while condição:
        declaração
    ```
    
    **Exemplo**:
    
    ```python
    while x > 0:
      print("x é positivo")
      x = x - 1
    ```
    
- **`For` -** Instrução de repetição usada para iterar sobre sequências, como listas, tuplas ou strings. Ele permite que o programador execute uma ou mais instruções em cada item da sequência. Sintaxe:
    
    ```python
    for item in sequência:
        declaração
    #Onde item é uma variável que irá receber cada item da sequência na cada iteração do laço, e sequência é a lista, string, tupla ou outra estrutura de dados que deseja iterar.
    ```
    
    **Exemplo**:
    
    ```
    lista = [1, 2, 3, 4]
    
    for item in lista:
      print(item)
    
    # Saída:
    # 1
    # 2
    # 3
    # 4
    ```
    
    ### Exemplo usando for e `range()`
    
    O laço `for` pode ser usado com a função `range()` para iterar sobre um intervalo de números. A função `range()` recebe um número inteiro como parâmetro e retorna uma sequência de números inteiros dentro do intervalo especificado. A sintaxe básica é a seguinte:
    
    ```python
    range(início, fim, passo)
    ```
    
    `início` é opcional e, se não for especificado, o `range()` começará no 0.
    
    `fim` é obrigatório e especifica o número final da sequência (não incluído).
    
    `passo` é opcional e, se não for especificado, o `range()` usará um passo de 1.
    
    **Exemplo**:
    
    ```python
    for contador in range(1, 11):
        print(contador)
    
    # Saída:
    # 0
    # 1
    # 2
    # 3
    # 4
    # 5
    # 6
    # 7
    # 8
    # 9
    #10
    ```
    
    No exemplo acima, a função `range()` foi chamada com o parâmetro `10`, o que resultou em uma sequência de números inteiros de 0 a 9. Esta sequência foi então usada pelo laço `for` para iterar sobre os números, imprimindo cada número na tela.
    
    ### Diferenças entre `Break` e `Continue`
    
    Break e continue são dois comandos usados para controlar o fluxo de um programa. O break interrompe a execução do programa e sai do loop atual, enquanto o continue causa a interrupção da iteração atual, mas o loop continua.
    
    **Exemplos**:
    
    `Break`
    
    ```python
    for i in range(10):
        if i == 5:
            break
        print(i)
    
    # Saída:
    # 0
    # 1
    # 2
    # 3
    # 4
    
    ```
    
    `Continue`
    
    ```python
    for i in range(10):
        if i == 5:
            continue
        print(i)
    
    # Saída:
    # 0
    # 1
    # 2
    # 3
    # 4
    # 6
    # 7
    # 8
    # 9
    ```
    
    <aside>
    💡 Como você pode ver no exemplo acima, o `break` interrompeu a execução do laço ao encontrar o número 5, enquanto o `continue` ignora o número 5 e continua a iteração do laço.
    
    </aside>
    

# Orientação a Objeto

Orientação a objeto é um paradigma de programação que se baseia na representação da realidade através de objetos e na manipulação desses objetos para resolver problemas. Em Python, você pode usar a orientação a objeto para modelar a realidade de forma mais abstrata, organizada e reutilizável.

Em Python, um objeto é uma instância de uma classe. Uma classe é uma definição de um objeto, que descreve seus atributos (ou características) e comportamentos (ou ações). Por exemplo, você pode criar uma classe **`Pessoa`** que tenha atributos como **`nome`**, **`idade`** e **`altura`** e comportamentos como **`caminhar`** e **`falar`**.

A sintaxe básica de uma classe em Python é:

```python
class NomeDaClasse:
  # Construtor (opcional)
  def __init__(self, argumentos):
    # Inicialização dos atributos
    self.atributo1 = argumentos

  # Métodos (opcionais)
  def metodo1(self, argumentos):
    # Instruções do método
```

Onde **`NomeDaClasse`** é o nome da classe, **`argumentos`** são os argumentos do construtor (opcionais), **`atributo1`** é o nome de um atributo e **`metodo1`** é o nome de um método.

Exemplo:

```python
class Pessoa:
  def __init__(self, nome, idade, altura):
    self.nome = nome
    self.idade = idade
    self.altura = altura

  def caminhar(self):
    print(self.nome + " está caminhando.")

  def falar(self, mensagem):
    print(self.nome + " diz: " + mensagem)
```

Você pode criar objetos a partir da classe usando o seguinte código:

```python
pessoa1 = Pessoa("John", 30, 1.75)
pessoa2 = Pessoa("Jane", 25, 1.60)
```

Você pode acessar os atributos e chamar os métodos dos objetos:

```python
print(pessoa1.nome)
pessoa1.caminhar()
pessoa1.falar("Olá, mundo!")
```

A saída seria:

```powershell
John
John está caminhando.
John diz: Olá, mundo!
```

### Herança

Em Python, é possível herdar de uma classe existente para criar uma nova classe com as mesmas características e comportamentos, acrescentando ou modificando atributos e métodos conforme necessário. Para isso, você precisa incluir o nome da classe pai na definição da nova classe, como mostrado abaixo: 

```python
class Filha(Pai):
  # Construtor (opcional)
  def __init__(self, argumentos):
    # Inicialização dos atributos
    Pai.__init__(self, argumentos)
    self.atributo_filha = argumentos

  # Métodos (opcionais)
  def metodo_filha(self, argumentos):
    # Instruções do método
```

Neste exemplo, a classe **`Filha`** herda da classe **`Pai`** e pode acessar todos os atributos e métodos da classe pai, além de incluir um novo atributo **`atributo_filha`** e um novo método **`metodo_filha`**.

Além disso, em Python é possível usar o conceito de sobrecarga de métodos (overloading) para forçar uma classe filha a sobrescrever um método da classe pai. Para isso, você precisa incluir um método com o mesmo nome na classe filha, como mostrado abaixo:

```python
class Filha(Pai):
  # Construtor (opcional)
  def __init__(self, argumentos):
    # Inicialização dos atributos
    Pai.__init__(self, argumentos)
    self.atributo_filha = argumentos

  # Métodos (opcionais)
  def metodo_filha(self, argumentos):
    # Instruções do método
  def metodo_pai(self, argumentos):
    # Instruções do método
    # Sobrescrita do método pai
```

Neste exemplo, a classe **`Filha`** sobrescreve o método **`metodo_pai`** da classe **`Pai`**. Quando você criar um objeto a partir da classe **`Filha`** e chamar o método **`metodo_pai`**, as instruções da classe filha serão executadas.

Herança é um conceito fundamental da orientação a objetos e permite a reutilização de código. No exemplo que mencionei anteriormente, podemos criar uma classe **`Estudante`** que herda da classe **`Pessoa`**. A classe **`Estudante`** terá as mesmas características (nome, idade e altura) e comportamentos (caminhar e falar) da classe **`Pessoa`**, além de novos atributos e métodos específicos de um estudante.

A sintaxe para herdar de uma classe em Python é:

```python
class Estudante(Pessoa):
    def __init__(self, nome, idade, altura, matricula, curso):
        Pessoa.__init__(self, nome, idade, altura)
        self.matricula = matricula
        self.curso = curso
```

Neste exemplo, a classe **`Estudante`** está herdando da classe **`Pessoa`**. O construtor **`__init__`** da classe **`Estudante`** chama o construtor da classe **`Pessoa`** com **`Pessoa.__init__(self, nome, idade, altura)`** para inicializar os atributos **`nome`**, **`idade`** e **`altura`**. Em seguida, adiciona novos atributos **`matricula`** e **`curso`**.

Assim, todas as características e comportamentos da classe **`Pessoa`** estarão disponíveis para a classe **`Estudante`**, permitindo que você crie objetos **`Estudante`** com as informações específicas de um estudante e ainda assim utilize os comportamentos da classe **`Pessoa`**.

```python
estudante = Estudante("João", 22, 1.75, "1234567", "Ciência da Computação")
estudante.caminhar()
estudante.falar()
```

Neste exemplo, estamos criando um objeto **`estudante`** da classe **`Estudante`** e chamando os métodos **`caminhar`** e **`falar`** da classe **`Pessoa`**, mesmo que esses métodos não tenham sido explicitamente definidos na classe **`Estudante`**.

### Polimorfismo

Polimorfismo é um conceito importante da orientação a objetos que permite que objetos de diferentes classes compartilhem o mesmo comportamento. Em Python, você pode usar polimorfismo para criar funções e métodos genéricos que podem trabalhar com objetos de diferentes classes.

Por exemplo, você pode criar uma função genérica que aceita qualquer objeto como seu argumento e chama o método `caminhar()` desse objeto. Se o argumento for um objeto da classe `Pessoa`, a função chamará `Pessoa.caminhar()`. Se o argumento for um objeto da classe `Estudante`, a função chamará `Estudante.caminhar()`.

```python
def caminhar(objeto):
    objeto.caminhar()

```

Neste exemplo, a função `caminhar()` pode ser chamada com qualquer objeto, independentemente de sua classe. A função chamará o método `caminhar()` do objeto passado como argumento. Assim, ao usar polimorfismo, você não precisa escrever código específico para cada classe. Você só precisa escrever o código uma vez e ele será aplicado a todos os objetos, independentemente de sua classe.

### Diferença entre Herança e Polimorfismo

Herança é quando você pode criar classes filhas que herdam atributos e funções do pai. Eles são frequentemente usados quando você tem uma classe abrangente mais geral, mas deseja definir classes mais específicas que podem ser semelhantes, mas não exatamente iguais. Fazemos isso para evitar copiar e colar um zilhão de vezes.

Neste exemplo, usamos cães como exemplo de como a herança pode ser usada. Demonstro como criar uma classe pai (superclasse) e uma classe filha (subclasse) e inicializar ambas.

Também podemos ter herança múltipla, que é quando uma subclasse pode ter vários pais e herdar as funções e atributos exclusivos de ambos. Um exemplo é o `ViraLata`!

O polimorfismo está relacionado à herança. Polimorfismo significa assumir muitas formas. Em OOP, isso geralmente está relacionado a subclasses que substituem o método pai para que a classe mais específica possa seguir um conjunto diferente de instruções. No meu exemplo, uso diferentes latidos de diferentes raças de cachorros.

```python
class Cachorro:
    def __init__(self, nome, idade, amigavel):
        self.nome = nome
        self.idade = idade
        self.amigavel = amigavel

    def gosta_de_passear(self):
        # Todo cachorro gosta depassear então sempre Thrue
        return True 
    
    def latido(self):
        return 'Woooof!'
    
class Caramelo(Cachorro):
    def __init__(self, nome, idade, amigavel):
        super().__init__(nome, idade, amigavel)
        
    def brincalhao(self):
        return "Fiquei esperando o dia todo pra você brincar comigo!"
    
    def latido(self):
        return 'AuAu Auu!'
    
class GoldenRetriever(Cachorro):
    def __init__(self, nome, idade, amigavel):
        super().__init__(nome, idade, amigavel)
        
    def bagunceiro(self):
        return "Amo fazer uma bagunça, não deixa um chinelo ou uma carteira na minha frente que eu mastigo hahhaha"
    
    #def latido(self):
    #    return 'Hauf hauf hauf!'

class HuskySiberiano(Cachorro):
    def __init__(self, nome, idade, amigavel):
        super().__init__(nome, idade, amigavel)
        
    def barulhento(self):
        return "Eu só to tentando te contar como foi o meu dia!!"
    
    def latido(self):
        return 'wuff, wuff; wau!'
        
class ViraLata(Caramelo, GoldenRetriever):
    def __init__(self, nome, idade, amigavel):
        super().__init__(nome, idade, amigavel)
        
    def latido(self):
       return 'voff, voff!'
    

bebeto = Caramelo('Bebeto', 3, 10)

print("Seu nome é {}, ele tem {} anos e seu nivel de amabilidade é {}/10".format(bebeto.nome, bebeto.idade, bebeto.amigavel))
print("Ele gosta de passear? R: {}".format(bebeto.gosta_de_passear()))

pitchula = ViraLata('Pitchula', 12, 10)

#Note que eu não declarei brincalhao ou bagunceiro em ViraLata mas ele herdou isso dos pais.
print(pitchula.brincalhao(),"\n",pitchula.bagunceiro()) 

lily = GoldenRetriever('Lily', 7, 10)
romeu = HuskySiberiano('Romeu', 5, 10)

# Usando polimorfismo
cachorros = [bebeto, pitchula, romeu, lily]
for raca in cachorros:
    print("Meu nome é {} e eu faço {}".format(raca.nome,raca.latido()))
```

### Segue mais dois exemplos para ajudar a entender o conceito de orientação a objeto e herança em Python:

**1º Exemplo:**

> Vamos imaginar que temos uma classe chamada **`Animal`** que possui os atributos **`nome`**, **`cor`** e **`idade`** e os métodos **`comer`**, **`dormir`** e **`andar`**. Essa classe pode ser usada para criar objetos que representam animais.
> 
> 
> ```python
> class Animal:
>   def __init__(self, nome, cor, idade):
>     self.nome = nome
>     self.cor = cor
>     self.idade = idade
> 
>   def comer(self):
>     print(self.nome + " está comendo.")
> 
>   def dormir(self):
>     print(self.nome + " está dormindo.")
> 
>   def andar(self):
>     print(self.nome + " está andando.")
> 
> ```
> 
> Agora, nós podemos criar um objeto da classe **`Animal`** chamado **`cachorro`**:
> 
> ```python
> cachorro = Animal("Toby", "marrom", 3)
> 
> ```
> 
> E podemos acessar os atributos e chamar os métodos deste objeto:
> 
> ```python
> print(cachorro.nome)
> cachorro.comer()
> cachorro.dormir()
> cachorro.andar()
> 
> ```
> 
> A saída seria:
> 
> ```powershell
> Toby
> Toby está comendo.
> Toby está dormindo.
> Toby está andando.
> 
> ```
> 
> Agora, vamos imaginar que queremos criar um objeto da classe **`Animal`** que represente um cachorro especial, um **`Salsicha`**. Para isso, nós podemos criar uma nova classe chamada **`Salsicha`** que herde da classe **`Animal`** e adicione um novo atributo e um novo método:
> 
> ```python
> class Salsicha(Animal):
>   def __init__(self, nome, cor, idade, tamanho):
>     Animal.__init__(self, nome, cor, idade)
>     self.tamanho = tamanho
> 
>   def rosnar(self):
>     print(self.nome + " está rosnando.")
> 
> ```
> 
> A classe **`Salsicha`** herda da classe **`Animal`**, portanto ela possui todos os atributos e métodos definidos na classe **`Animal`**, além de um novo atributo **`tamanho`** e um novo método **`rosnar`**.
> 
> Agora, podemos criar um objeto da classe **`Salsicha`** chamado **`salsicha`**:
> 
> ```python
> salsicha = Salsicha("Bolota", "branco", 1, "pequeno")
> 
> ```
> 
> E podemos acessar os atributos e chamar os métodos deste objeto:
> 
> ```python
> print(salsicha.nome)
> salsicha.comer()
> salsicha.dormir()
> salsicha.andar()
> salsicha.rosnar()
> 
> ```
> 
> A saída seria:
> 
> ```powershell
> Bolota
> Bolota está comendo.
> Bolota está dormindo.
> Bolota está andando.
> Bolota está rosnando.
> 
> ```
> 
> Neste exemplo, a criança pode entender como a classe **`Salsicha`** herda da classe **`Animal`** e como usar herança para criar objetos com características es
> 

**2° Exemplo**

> Imagine que você quer construir um jogo de avatares em que cada avatar tem um nome, uma idade e uma cor de cabelo. Além disso, todos os avatares têm a capacidade de se mover e falar.
> 
> 
> Você pode começar criando uma classe **`Avatar`** que representa os atributos e comportamentos comuns a todos os avatares:
> 
> ```python
> class Avatar:
>     def __init__(self, nome, idade, cor_cabelo):
>         self.nome = nome
>         self.idade = idade
>         self.cor_cabelo = cor_cabelo
> 
>     def mover(self):
>         print(f"{self.nome} está se movendo.")
> 
>     def falar(self):
>         print(f"{self.nome} está falando.")
> ```
> 
> Em seguida, você pode criar uma classe **`Crianca`** que herda da classe **`Avatar`** e adiciona um novo atributo, **`altura`**, e um novo comportamento, **`pular`**:
> 
> ```python
> class Crianca(Avatar):
>     def __init__(self, nome, idade, cor_cabelo, altura):
>         Avatar.__init__(self, nome, idade, cor_cabelo)
>         self.altura = altura
> 
>     def pular(self):
>         print(f"{self.nome} está pulando.")
> ```
> 
> Agora você pode criar objetos da classe **`Crianca`** e utilizar seus atributos e comportamentos:
> 
> ```python
> crianca = Crianca("Lara", 7, "loira", 1.20)
> print(crianca.nome) # Lara
> print(crianca.idade) # 7
> print(crianca.cor_cabelo) # loira
> print(crianca.altura) # 1.20
> crianca.mover() # Lara está se movendo.
> crianca.falar() # Lara está falando.
> crianca.pular() # Lara está pulando.
> ```
> 
> Neste exemplo, a classe **`Crianca`** herda todos os atributos e comportamentos da classe **`Avatar`**, além de adicionar um novo atributo e comportamento. Desta forma, você pode reutilizar o código da classe **`Avatar`** e ainda assim ter a flexibilidade de adicionar ou modificar atributos e comportamentos específicos da classe **`Crianca`**.
> 

### Duck typing

Duck typing é um paradigma de programação orientada a objetos que segue a premissa de que "se algo parece um pato e anda como um pato, então deve ser um pato". Em outras palavras, ao invés de verificar explicitamente se um objeto pertence a determinada classe, o código que usa o objeto simplesmente verifica se o objeto possui os métodos e atributos necessários - não importa a classe do objeto. Com o duck typing, o código pode trabalhar facilmente com objetos de classes diferentes, desde que eles possuam os mesmos métodos e atributos.

### Utilizar o `__eq__`

A função `__eq__` ****é utilizada em Python para implementar a operação de igualdade (==) entre objetos de uma classe. A utilização desta função permite que os objetos da classe sejam comparados de maneira específica, e não apenas comparados pelo endereço de memória, como é o caso padrão.  O `__eq__`é um método especial que deve ser definido por qualquer classe que deseja suportar comparações.  Por exemplo, se um objeto possui atributos nome e idade, você pode definir o método `__eq__` para que dois objetos sejam considerados iguais se os seus atributos nome e idade forem iguais.

Para usar o `__eq__`, você precisa criar um método `__eq__`dentro da classe que deseja comparar. O método `__eq__`deve ter pelo menos um parâmetro e deve retornar um valor booleano (True ou False).

- **Quando devemos usar o `__eq__`?**

 O `__eq__` é útil quando queremos comparar objetos de diferentes classes para verificar se eles possuem os mesmos atributos. Por exemplo, se você estiver trabalhando com objetos que possuem nome e idade, poderá usar o `__eq__` para verificar se dois objetos possuem o mesmo nome e a mesma idade.

Usar o `__eq__` também é útil quando queremos verificar se dois objetos são iguais. Isso significa que se dois objetos possuírem os mesmos atributos, eles serão considerados iguais. Isso pode ser útil se você quiser verificar se dois objetos em uma lista são iguais ou se um objeto já existe em uma lista.

O exemplo a seguir mostra como definir e usar o método `__eq__`para comparar dois objetos da classe Aluno:

```python
class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __eq__(self, outro):
        return self.nome == outro.nome and self.idade == outro.idade

aluno1 = Aluno('João', 20)
aluno2 = Aluno('João', 20)

if aluno1 == aluno2:
    print('Os alunos são iguais.')
else:
    print('Os alunos são diferentes.')

# A saída deste código será:
#	'Os alunos são iguais.'
```

### Usar o `isinstance`

Usar o `isinstance` em Python é uma forma de verificar se um objeto pertence a determinada classe ou tipo. Por exemplo, você pode usar o `isinstance` para verificar se um objeto é do tipo `int`, `str`, `list` ou `dict`. Isso é útil quando você está trabalhando com objetos de classes diferentes e precisa verificar se eles são do mesmo tipo.

Quando usar o `isinstance` depende do que você está tentando alcançar. Por exemplo, se você estiver trabalhando com objetos de classes diferentes e precisar verificar se eles são do mesmo tipo, o `isinstance` pode ser útil. Se você estiver verificando se um objeto pertence a uma determinada classe, o `isinstance` também pode ser útil. Além disso, o `isinstance` pode ser usado para verificar se um objeto é uma instância de uma determinada classe ou de qualquer uma de suas subclasses.

Usar o `isinstance` é uma forma eficiente de verificar se um objeto pertence a determinada classe ou se ele é do mesmo tipo que outro objeto. Ao usar o `isinstance`, você pode ter certeza de que está verificando corretamente os tipos de objetos, o que é útil para evitar erros de execução. Além disso, usar o `isinstance` é mais eficiente do que usar a função padrão `type`, pois o `isinstance` não precisa verificar a herança da classe.

A sintaxe de **`isinstance`** é:

```python
scssCopy code
isinstance(obj, cls)
```

Onde **`obj`** é o objeto a ser verificado e **`cls`** é a classe ou tipo que desejamos comparar.

Exemplo:

```python
pythonCopy code
class Pessoa:
    pass

class Funcionario(Pessoa):
    pass

funcionario = Funcionario()

print(isinstance(funcionario, Funcionario)) # True
print(isinstance(funcionario, Pessoa)) # True
print(isinstance(funcionario, object)) # True
print(isinstance(funcionario, str)) # False
```

Neste exemplo, a classe **`Funcionario`** é uma subclasse de **`Pessoa`**, então a expressão **`isinstance(funcionario, Pessoa)`** retorna **`True`**. Além disso, todas as classes em Python são subclasses de **`object`**, por isso **`isinstance(funcionario, object)`** também retorna **`True`**.

### Usar o `__lt__`

O método `__lt__` é usado em Python para implementar a operação de comparação menor que (<). A utilização desta função permite que os objetos da classe sejam comparados de maneira específica, e não apenas comparados pelo endereço de memória, como é o caso padrão. O `__lt__` é um método especial que deve ser definido por qualquer classe que deseja suportar comparações.

- **Quando devemos usar o `__lt__`?**

O `__lt__` é útil quando queremos verificar se um objeto é menor que outro. Por exemplo, se um objeto possui um atributo chamado `idade`, você pode usar o `__lt__` para verificar se uma idade é menor que a outra.

Usar o `__lt__` também é útil quando queremos ordenar objetos de acordo com determinadas condições. Por exemplo, se você estiver trabalhando com objetos que possuem nome e idade, poderá usar o `__lt__` para ordenar os objetos pela idade.

Exemplo: Imagine que você tem uma classe **`Pessoa`** que representa informações sobre uma pessoa, incluindo nome, idade e endereço. Se você quiser ordenar uma lista de objetos da classe **`Pessoa`** por idade, você precisaria definir o método **`__lt__`** para que o operador "menor que" compare as idades das pessoas.

```python
class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def __lt__(self, outra):
        return self.idade < outra.idade

pessoas = [Pessoa("João", 35, "Rua A"), Pessoa("Maria", 30, "Rua B"), Pessoa("Pedro", 40, "Rua C")]

for pessoa in sorted(pessoas):
    print(pessoa.nome, pessoa.idade)

# Saída:
# Maria 30
# João 35
# Pedro 40
```

Sem o método **`__lt__`**, a função **`sorted`** não saberia como comparar os objetos da classe **`Pessoa`**, resultando em um erro.

- Mas e se algum deles tiver a mesma idade? Posso ter um segunda regra

```python
class Pessoa:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def __lt__(self, outra):
        if self.idade != outra.idade:
            return self.idade < outra.idade
        return self.nome < outra.nome

pessoas = [Pessoa("João", 30, "Rua A"), Pessoa("Maria", 30, "Rua B"), Pessoa("Pedro", 40, "Rua C")]

for pessoa in sorted(pessoas):
    print(pessoa.nome, pessoa.idade)

# Saída:
# João 30
# Maria 30
# Pedro 40
```

Usar o `__lt__` é uma forma eficiente de verificar se um objeto é menor que outro ou de ordenar objetos de acordo com determinadas condições. Ao usar o `__lt__`, você pode ter certeza de que está verificando corretamente os tipos de objetos, o que é útil para evitar erros de execução.

# Collections

No Python, as Collections são estruturas de dados especializadas que permitem armazenar e acessar dados de maneira eficiente. Existem vários tipos de Collections disponíveis no Python, incluindo `listas`, `tuplas`, `dicionários` e `conjuntos`.

Uma **lista** é uma sequência **mutável** de objetos que podem ser acessados usando índices. É possível adicionar, remover e modificar elementos da lista. Por exemplo, a lista abaixo contém três elementos:

```python
lista = [1, 2, 3]

```

Uma **tupla** é semelhante a uma lista, exceto que é **imutável**. Uma vez criada, uma tupla não pode ser modificada. Por exemplo, a tupla abaixo contém três elementos:

```python
tupla = (1, 2, 3)

```

Um **dicionário** é uma estrutura de dados que consiste em **chaves e valores**. Os valores podem ser recuperados usando as chaves. Por exemplo, o dicionário abaixo contém três elementos:

```python
dicionario = {'a': 1, 'b': 2, 'c': 3}

```

Um **conjunto** é uma coleção **não ordenada de elementos únicos**. Por exemplo, o conjunto abaixo contém três elementos:

```python
conjunto = {1, 2, 3}

```

<aside>
<img src="https://www.notion.so/icons/light-bulb_orange.svg" alt="https://www.notion.so/icons/light-bulb_orange.svg" width="40px" /> As Collections do Python permitem armazenar de forma eficiente e organizada diferentes tipos de dados. Elas são essenciais para muitas tarefas de programação, desde a manipulação de dados até a criação de algoritmos avançados.

</aside>

## Listas

Uma das principais formas de trabalhar com listas em Python é usando os métodos de lista. Os métodos de lista são funções especiais que nos permitem realizar tarefas comuns com listas, como adicionar, remover, modificar e procurar elementos.

Por exemplo, o método `append()` permite adicionar um novo elemento ao final de uma lista:

```python
minha_lista = [1, 2, 3]
minha_lista.append(4)
print(minha_lista) # [1, 2, 3, 4]

```

O método `remove()` permite remover um elemento específico da lista:

```python
minha_lista = [1, 2, 3, 4]
minha_lista.remove(3)
print(minha_lista) # [1, 2, 4]

```

O método `sort()` permite classificar os elementos de uma lista em ordem crescente ou decrescente:

```python
minha_lista = [3, 1, 4, 2]
minha_lista.sort()
print(minha_lista) # [1, 2, 3, 4]

```

Listas são úteis quando você precisa armazenar vários objetos do mesmo tipo. Aqui estão alguns exemplos de usos comuns para listas no Python:

- Armazenar uma lista de nomes: `nomes = ['João', 'Maria', 'Ana']`
- Armazenar uma lista de números: `numeros = [1, 2, 3, 4, 5]`
- Armazenar uma lista de strings: `strings = ['Olá', 'mundo', '!']`
- Armazenar uma lista de objetos: `objetos = [obj_a, obj_b, obj_c]`
- Armazenar uma lista de listas: `listas = [[1, 2], [3, 4], [5, 6]]`
- Percorrer todos os elementos de uma lista:

```python
lista = [1, 2, 3]

for elemento in lista:
    print(elemento)

```

- Modificar elementos de uma lista:

```python
lista = [1, 2, 3]

lista[0] = 4
lista[1] = 5
lista[2] = 6

print(lista) # [4, 5, 6]

```

- Adicionar elementos a uma lista:

```python
lista = [1, 2, 3]

lista.append(4)
lista.append(5)
lista.append(6)

print(lista) # [1, 2, 3, 4, 5, 6]

```

Além disso, é possível usar vários outros métodos de lista para realizar tarefas com listas, como `pop()`, `reverse()`, `count()` e `index()`. Para obter mais informações sobre esses métodos, consulte a [documentação do Python](https://docs.python.org/3/tutorial/datastructures.html).

## Tuplas

Tuplas são úteis para armazenar dados que não devem ser alterados. Por exemplo, imagine que você tem um conjunto de dados que representam as coordenadas de um lugar, como latitude e longitude. Uma tupla é uma estrutura de dados ideal para armazenar esses dados, pois uma vez criadas, as tuplas não podem ser alteradas.

Uma das principais formas de trabalhar com tuplas em Python é usando os métodos de tupla. Os métodos de tupla são funções especiais que nos permitem realizar tarefas comuns com tuplas, como acessar, contar e pesquisar elementos.

Aqui estão alguns exemplos de usos comuns para tuplas no Python:

- Armazenar uma tupla de nomes: `nomes = ('João', 'Maria', 'Ana')`
- Armazenar uma tupla de números: `numeros = (1, 2, 3, 4, 5)`
- Armazenar uma tupla de strings: `strings = ('Olá', 'mundo', '!')`
- Armazenar uma tupla de objetos: `objetos = (obj_a, obj_b, obj_c)`
- Armazenar uma tupla de tuplas: `tuplas = ((1, 2), (3, 4), (5, 6))`
- Percorrer todos os elementos de uma tupla:

```python
tupla = (1, 2, 3)

for elemento in tupla:
    print(elemento)

```

- Modificar elementos de uma tupla:

```python
tupla = (1, 2, 3)

nova_tupla = (4, 5, 6)

tupla = nova_tupla

print(tupla) # (4, 5, 6)

```

- Desempacotar uma tupla:

```python
tupla = (1, 2, 3)

a, b, c = tupla

print(a) # 1
print(b) # 2
print(c) # 3

```

Outra situação em que as tuplas são úteis é quando você precisa passar vários parâmetros para uma função. Como as tuplas são imutáveis, o valor dos parâmetros não pode ser alterado accidentalmente:

```python
# Uma função que calcula a média de três números
def media(a, b, c):
    return (a + b + c) / 3

# Uma tupla com os três números
numeros = (1, 2, 3)

# Chamando a função "media" e passando a tupla como parâmetro
resultado = media(*numeros)

print(resultado) # 2.0

```

Além disso, as tuplas são úteis para armazenar conjuntos de dados relacionados, como um nome e uma idade. Por exemplo, você pode criar uma tupla contendo um nome e uma idade e armazená-la em uma lista para acessar facilmente os dados:

```python
# Uma tupla contendo o nome e a idade de uma pessoa
pessoa = ("João", 25)

# Uma lista de tuplas contendo o nome e a idade de várias pessoas
lista_pessoas = [("João", 25), ("Maria", 20), ("Ana", 30)]

# Acessando os dados de uma tupla específica
nome = lista_pessoas[0][0]
idade = lista_pessoas[0][1]

print(f"{nome} tem {idade} anos.") # João tem 25 anos.

```

Por fim, as tuplas também são úteis para criar dicionários em que as chaves são tuplas. Isso pode ser útil se você precisar armazenar um conjunto de dados relacionados, como as coordenadas de uma cidade:

```python
cidade = {
    (10.0, 15.0): 'Rio de Janeiro',
    (20.0, 25.0): 'São Paulo',
    (30.0, 35.0): 'Belém'
}

## Agora, você pode facilmente recuperar o nome da cidade usando as coordenadas:

# Recuperando o nome da cidade usando as coordenadas
coordenadas = (10.0, 15.0)

nome_cidade = cidade[coordenadas]

print(nome_cidade) # Rio de Janeiro
```

Além disso, é possível usar vários outros métodos de tupla para realizar tarefas com tuplas, como  `index()` ,`count()` ,`len()`, `sum()` e `max()`. Para obter mais informações sobre esses métodos, consulte a [documentação do Python](https://docs.python.org/3/tutorial/datastructures.html).

## Conjuntos

Um **conjunto** é uma coleção **não ordenada de elementos únicos**. Os conjuntos são úteis para armazenar dados que não podem ser repetidos, como nomes de usuário, IDs de produtos e números de lote.

Um dos principais usos dos conjuntos é **descobrir se um elemento existe em um conjunto**. Por exemplo, imagine que você tem um conjunto de nomes de usuário e precisa descobrir se um determinado nome de usuário existe no conjunto. Você pode usar o operador `in` para verificar se o nome de usuário está no conjunto:

```python
# Um conjunto de nomes de usuário
usuarios = {'joao', 'maria', 'ana'}

# Verificando se o nome de usuário "joao" existe no conjunto
if 'joao' in usuarios:
    print('O nome de usuário "joao" existe no conjunto')
```

Além disso, os conjuntos também são úteis para realizar **operações matemáticas, como união, intersecção e diferença**. Por exemplo, imagine que você tem dois conjuntos de números e precisa encontrar os números que estão presentes em ambos os conjuntos. Você pode usar o operador `&` para realizar a intersecção entre os conjuntos:

```python
# Um conjunto de números
conjunto_a = {1, 2, 3, 4, 5}

# Outro conjunto de números
conjunto_b = {3, 4, 5, 6, 7}

# Encontrando os números que estão presentes em ambos os conjuntos
intersecao = conjunto_a & conjunto_b

print(intersecao) # {3, 4, 5}
```

Outra operação matemática comum é a união. Por exemplo, imagine que você tem dois conjuntos de números e precisa encontrar os números que estão em pelo menos um dos conjuntos. Você pode usar o operador `|` para realizar a união entre os conjuntos:

```python
# Um conjunto de números
conjunto_a = {1, 2, 3, 4, 5}

# Outro conjunto de números
conjunto_b = {3, 4, 5, 6, 7}

# Encontrando os números que estão presentes em pelo menos um dos conjuntos
uniao = conjunto_a | conjunto_b

print(uniao) # {1, 2, 3, 4, 5, 6, 7}
```

Por fim, os conjuntos também são úteis para **remover elementos duplicados de uma lista**. Por exemplo, imagine que você tem uma lista de números e precisa remover os números duplicados da lista. Você pode usar o método `set()` para converter a lista em um conjunto e, em seguida, usar o método `list()` para converter o conjunto em uma lista sem elementos duplicados:

```python
# Uma lista com números duplicados
lista = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]

# Convertendo a lista em um conjunto
conjunto = set(lista)

# Convertendo o conjunto em uma lista sem elementos duplicados
lista_sem_duplicados = list(conjunto)

print(lista_sem_duplicados)
```

Em Python, você pode usar o operador `-` para remover elementos repetidos de dois conjuntos. O operador `-` realiza a operação de subtração set, ou seja, retorna um novo conjunto com os elementos presentes no primeiro conjunto, mas não no segundo.

Por exemplo:

```python
# Um conjunto de números
conjunto_a = {1, 2, 3, 4, 5}

# Outro conjunto de números
conjunto_b = {3, 4, 5, 6, 7}

# Encontrando os números que estão presentes no conjunto_a,
# mas não estão presentes no conjunto_b
diferenca = conjunto_a - conjunto_b

print(diferenca) # {1, 2}
```

Já o operador `^` exclusivo, também conhecido como operador XOR, retorna um conjunto com os elementos presentes em um dos conjuntos, mas não em ambos Você pode usar o operador `^` para criar um conjunto exclusivo:

```python
# Um conjunto de números
conjunto_a = {1, 2, 3, 4, 5}

# Outro conjunto de números
conjunto_b = {3, 4, 5, 6, 7}

# Encontrando os números que estão presentes em pelo menos um dos conjuntos,
# mas não em ambos
conjunto_exclusivo = conjunto_a ^ conjunto_b

print(conjunto_exclusivo) # {1, 2, 6, 7}
```

### Adicionando elementos em um conjunto

Em Python, você pode usar o método `add()` para adicionar um novo elemento a um conjunto. Por exemplo, imagine que você tem um conjunto de nomes de usuário e precisa adicionar um novo nome de usuário. Você pode usar o método `add()` para adicionar o novo nome ao conjunto:

```python
# Um conjunto de nomes de usuário
usuarios = {'joao', 'maria', 'ana'}

# Adicionando um novo nome de usuário
usuarios.add('pedro')

print(usuarios) # {'joao', 'maria', 'ana', 'pedro'}
```

Além do método `add()`, você também pode usar o método `update()` para adicionar múltiplos elementos a um conjunto. Por exemplo, imagine que você tem um conjunto de números e precisa adicionar vários números ao conjunto. Você pode usar o método `update()` para adicionar os números ao conjunto:

```python
# Um conjunto de números
numeros = {1, 2, 3, 4}

# Adicionando múltiplos números ao conjunto
numeros.update([5, 6, 7, 8])

print(numeros) # {1, 2, 3, 4, 5, 6, 7, 8}
```

Além disso, você também pode usar o operador `|` para adicionar os elementos de um conjunto a outro. Por exemplo, imagine que você tem dois conjuntos de números e precisa adicionar os números do primeiro conjunto ao segundo conjunto. Você pode usar o operador `|` para adicionar os números:

```python
# Um conjunto de números
conjunto_a = {1, 2, 3, 4}

# Outro conjunto de números
conjunto_b = {3, 4, 5, 6}

# Adicionando os elementos do conjunto_a ao conjunto_b
conjunto_b |= conjunto_a

print(conjunto_b) # {1, 2, 3, 4, 5, 6}
```

## Dicionários

Um **dicionário** é uma coleção **não ordenada de pares chave-valor**. Os dicionários são úteis para armazenar conjuntos de dados que estão relacionados, como um nome e um endereço de e-mail.  A sintaxe de um dicionário em Python é muito simples. Você pode criar um dicionário usando a sintaxe de colchetes `{}` e adicionar elementos ao dicionário usando a sintaxe de atribuição `key: value`. 

Por exemplo, você pode criar um dicionário contendo o nome e o endereço de e-mail de uma pessoa e armazená-lo para acessar facilmente os dados:

```python
# Um dicionário contendo o nome e o endereço de e-mail de uma pessoa
pessoa = {'nome':'João', 'email': 'joao@example.com'}

# Imprimindo o nome da pessoa
print(pessoa['nome']) # João

# Imprimindo o endereço de e-mail da pessoa
print(pessoa['email']) # joao@example.com
```

Os dicionários também são úteis para **acessar dados usando chaves**. Por exemplo, imagine que você tem um dicionário contendo o nome e o endereço de e-mail de várias pessoas e deseja recuperar o endereço de e-mail de uma pessoa específica. Você pode usar a chave `'email'` para recuperar o endereço de e-mail da pessoa:

```python
# Um dicionário contendo o nome e o endereço de e-mail de várias pessoas
pessoas = {
    'joao': {'nome':'João', 'email': 'joao@example.com'},
    'maria': {'nome':'Maria', 'email': 'maria@example.com'},
    'ana': {'nome':'Ana', 'email': 'ana@example.com'}
}

# Imprimindo o endereço de e-mail da pessoa "ana"
print(pessoas['ana']['email']) # ana@example.com
```

Além disso, você também pode usar os métodos `keys()`, `values()` e `items()` para iterar sobre um dicionário. Por exemplo, imagine que você tem um dicionário contendo o nome e o endereço de e-mail de várias pessoas e deseja imprimir os nomes de todas as pessoas. Você pode usar o método `values()` para recuperar os nomes de todas as pessoas:

```python
# Um dicionário contendo o nome e o endereço de e-mail de várias pessoas
pessoas = {
    'joao': {'nome':'João', 'email': 'joao@example.com'},
    'maria': {'nome':'Maria', 'email': 'maria@example.com'},
    'ana': {'nome':'Ana', 'email': 'ana@example.com'}
}

# Iterando sobre o dicionário e imprimindo os nomes de todas as pessoas
for nome in pessoas.values():
    print(nome['nome'])

# João
# Maria
# Ana
```

Além disso, os dicionários também são úteis para **armazenar dados em cache**. Por exemplo, imagine que você tem um dicionário contendo os resultados de uma consulta a um banco de dados e dese

### Adicionando elementos a um dicionário

Em Python, você pode usar o método `update()` para adicionar um novo par chave-valor a um dicionário. Por exemplo, imagine que você tem um dicionário contendo o nome e o endereço de e-mail de uma pessoa e precisa adicionar um novo par chave-valor ao dicionário. Você pode usar o método `update()` para adicionar o novo par:

```python
# Um dicionário contendo o nome e o endereço de e-mail de uma pessoa
pessoa = {'nome':'João', 'email': 'joao@example.com'}

# Adicionando um novo par chave-valor ao dicionário
pessoa.update({'idade': 20})

print(pessoa) # {'nome': 'João', 'email': 'joao@example.com', 'idade': 20}
```

Além disso, você também pode usar o operador `[]` para adicionar um novo par chave-valor ao dicionário. Por exemplo, imagine que você tem um dicionário contendo o nome e o endereço de e-mail de uma pessoa e deseja adicionar um novo par chave-valor ao dicionário. Você pode usar o operador `[]` para adicionar o novo par:

```python
# Um dicionário contendo o nome e o endereço de e-mail de uma pessoa
pessoa = {'nome':'João', 'email': 'joao@example.com'}

# Adicionando um novo par chave-valor ao dicionário
pessoa['idade'] = 20

print(pessoa) # {'nome': 'João', 'email': 'joao@example.com', 'idade': 20}
```

### Removendo elementos de um dicionário

Em Python, você pode usar o método `pop()` para remover um elemento do dicionário. Por exemplo, imagine que você tem um dicionário contendo o nome e o endereço de e-mail de uma pessoa e deseja remover o nome da pessoa do dicionário. Você pode usar o método `pop()` para remover o nome:

```python
# Um dicionário contendo o nome e o endereço de e-mail de uma pessoa
pessoa = {'nome':'João', 'email': 'joao@example.com'}

# Removendo o nome da pessoa do dicionário
pessoa.pop('nome')

print(pessoa) # {'email': 'joao@example.com'}
```

Além disso, você também pode usar o método `del` para remover um elemento do dicionário. Por exemplo, imagine que você tem um dicionário contendo o nome e o endereço de e-mail de uma pessoa e deseja remover o nome da pessoa do dicionário. Você pode usar o método `del` para remover o nome:

```python
# Um dicionário contendo o nome e o endereço de e-mail de uma pessoa
pessoa = {'nome':'João', 'email': 'joao@example.com'}

# Removendo o nome da pessoa do dicionário
del pessoa['nome']

print(pessoa) # {'email': 'joao@example.com'}
```

### Verificando se um elemento está presente em um dicionário

Em Python, você pode usar o operador `in` para verificar se um elemento está presente em um dicionário. Por exemplo, imagine que você tem um dicionário contendo o nome e o endereço de e-mail de uma pessoa e deseja verificar se a chave `'nome'` está presente no dicionário. Você pode usar o operador `in` para verificar se a chave está presente no dicionário:

```python
# Um dicionário contendo o nome e o endereço de e-mail de uma pessoa
pessoa = {'nome':'João', 'email': 'joao@example.com'}

# Verificando se a chave 'nome' está presente no dicionário
if 'nome' in pessoa:
    print('A chave está presente no dicionário!')
```

### Recuperando o valor de uma chave específica em um dicionário

Você também pode usar o método `get()` para recuperar o valor de uma chave específica em um dicionário. Por exemplo, imagine que você tem um dicionário contendo o nome, o endereço de e-mail e o número de telefone de uma pessoa e precisa recuperar o número de telefone da pessoa. Você pode usar o método `get()` para recuperar o número de telefone do dicionário:

```python
pessoa = {'nome': 'João', 'email': 'joao@example.com', 'telefone': '1234567890'}

# Recuperando o número de telefone da pessoa
numero_telefone = pessoa.get('telefone')

print(numero_telefone) # 1234567890
```

### Usando o construtor `dict()`

No Python, você pode usar o construtor `dict()` para criar um dicionário vazio. O construtor `dict()` aceita um argumento obrigatório, que pode ser uma sequência, um iterável ou outro dicionário. Se o argumento for uma sequência, o construtor `dict()` criará um dicionário com os pares chave-valor da sequência. Se o argumento for um iterável, o construtor `dict()` criará um dicionário com os pares chave-valor do iterável. Se o argumento for outro dicionário, o construtor `dict()` criará um dicionário com os pares chave-valor do dicionário. Por exemplo:

```python
# Criando um dicionário a partir de uma sequência
dicionario = dict([('nome', 'João'), ('idade', 20)])

# Imprimindo o dicionário
print(dicionario) # {'nome': 'João', 'idade': 20}

# Criando um dicionário a partir de uma lista de tuplas
dicionario = dict([('nome', 'João'), ('idade', 20), ('email', 'joao@example.com')])

# Imprimindo o dicionário
print(dicionario) # {'nome': 'João', 'idade': 20, 'email': 'joao@example.com'}

# Criando um dicionário a partir de outro dicionário
dicionario_2 = {'sobrenome': 'Cardoso'}
dicionario = dict(dicionario, **dicionario_2)

# Imprimindo o dicionário
print(dicionario) # {'nome': 'João', 'idade': 20, 'email': 'joao@example.com', 'sobrenome': 'Cardoso'}
```

### Quando e porque usar o `zip()` junto ao `dict()` em Python

O `zip()` é uma função útil para combinar duas ou mais sequências em um único objeto. O objeto criado pelo `zip()` é um objeto iterável contendo tuplas, onde cada tupla contém um elemento de cada sequência.

O `dict()`, por sua vez, é um construtor de dicionário que pode ser usado para criar um dicionário a partir de uma sequência de tuplas.

Portanto, o `zip()` e o `dict()` podem ser usados em conjunto para criar um dicionário a partir de duas sequências. Por exemplo, imagine que você tem duas listas, uma contendo os nomes de usuário e outra contendo as senhas, e deseja criar um dicionário contendo os nomes de usuário e suas respectivas senhas. Você pode usar o `zip()` para combinar as duas listas e o `dict()` para criar o dicionário:

```python
# Uma lista de nomes de usuário
usuarios = ['joao', 'maria', 'ana']

# Uma lista de senhas
senhas = ['123', '456', '789']

# Criando um dicionário contendo os nomes de usuário e suas respectivas senhas
dicionario = dict(zip(usuarios, senhas))

print(dicionario) # {'joao': '123', 'maria': '456', 'ana': '789'}
```

Outro exemplo:

```python
# Uma lista de nomes de usuário
usuarios = ['joao', 'maria', 'ana']

# Criando um dicionário contendo os nomes de usuário e suas respectivas senhas
dicionario = dict(zip(usuarios, ['123', '456', '789']))

print(dicionario) # {'joao': '123', 'maria': '456', 'ana': '789'}
```

**Como percorrer linha a linha em um dicionário?**

Para percorrer linha a linha em um dicionário, você pode usar o método `items()`. Por exemplo:

```python
dic = {'chave1': 'valor1', 'chave2': 'valor2'}
for key, valor in dic.items():
    print(key, valor)

# O código acima imprimirá chave1 valor1 e chave2 valor2
```

## `defaultdict`

O `defaultdict` é um construtor de dicionário que permite que você especifique o valor padrão que será retornado quando o dicionário não contém uma chave específica. Por exemplo, imagine que você tem um dicionário contendo nomes e idades e deseja recuperar a idade de uma pessoa, mas não há nenhuma entrada no dicionário para a pessoa. O `defaultdict` permite que você especifique um valor padrão para retornar caso não haja uma entrada correspondente no dicionário. Por exemplo:

```python
from collections import defaultdict

# Um dicionário contendo nomes e idades
dic = defaultdict(lambda: -1)
dic['joao'] = 20
dic['maria'] = 25

# Recuperando a idade de uma pessoa, mas não há nenhuma entrada no dicionário para a pessoa
idade = dic['ana']

# Imprimindo a idade
print(idade) # -1
```

No exemplo acima, o `defaultdict` foi instanciado com o valor padrão `-1`. Portanto, quando você tentou recuperar a idade de `ana`, que não está presente no dicionário, o `defaultdict` retornou `-1`.

### Counter

O Counter é um contador de objetos disponível no módulo collections do Python. Ele é usado para contar a quantidade de vezes que um objeto ou elemento aparece em uma sequência. Ele retorna um objeto do tipo Counter que é um dicionário que mapeia os elementos da sequência à sua contagem. Por exemplo, imagine que você tem uma lista de elementos e deseja contar a quantidade de vezes que cada elemento aparece na lista. Você pode usar o Counter para contar a quantidade de vezes que cada elemento aparece na lista:

```python
from collections import Counter

# Uma lista de elementos
lista = ['a', 'b', 'c', 'a', 'a', 'b']

# Contando a quantidade de vezes que cada elemento aparece na lista
contador = Counter(lista)

print(contador) # Counter({'a': 3, 'b': 2, 'c': 1})
```

### Referências

[5. Data Structures](https://docs.python.org/3/tutorial/datastructures.html)

[3.11.1 Documentation](https://docs.python.org/pt-br/3/index.html)

## Jogo de Adivinhação

### Jogo de Adivinhação

Um jogo de adivinhação é um jogo divertido no qual o jogador tenta adivinhar o resultado gerado aleatoriamente. O jogador tem uma série de chances para adivinhar o resultado correto. Se o jogador falhar, o jogo termina e o jogador perde.

No Python, podemos criar um jogo de adivinhação usando a biblioteca `random`. A biblioteca `random` contém funções que geram números aleatórios. Para criar um jogo de adivinhação, precisamos usar a função `random.randint()`. Esta função gera um número aleatório entre dois números que são passados como parâmetros.

Em nosso exemplo, vamos criar um jogo de adivinhação simples. O jogador terá que adivinhar um número entre 1 e 10. Se o jogador acertar, ele ganha; caso contrário, ele perde.

Vamos começar importando a biblioteca `random`:

```python
import random

```

Em seguida, vamos gerar um número aleatório entre 1 e 10 usando a função `random.randint()`:

```python
numero_secreto = random.randint(1, 10)

```

Agora, vamos iniciar um laço `while` para dar ao jogador 10 chances de adivinhar o número:

```python
tentativas = 0

while tentativas < 10:
    tentativa = int(input("Adivinhe o número secreto (entre 1 e 10): "))
    tentativas += 1

    if tentativa == numero_secreto:
        print("Parabéns! Você acertou!")
        break
    else:
        print("Você errou! Tente novamente.")

```

Se o jogador adivinhar o número, o jogo acabará e ele ganhará; caso contrário, o jogo continuará até que o jogador exceda 10 tentativas. Se isso acontecer, o jogo acabará e o jogador perderá.

Esse é um exemplo simples de como criar um jogo de adivinhação em Python. Você pode aprimorar esse jogo adicionando um sistema de pontuação ou adicionando mais níveis de dificuldade.

## Conta Corrente

```python
class ContaCorrente:
    
    def __init__(self, codigo_conta):
        self.codigo_conta = codigo_conta
        self.saldo = 0
        
    def deposita(self, valor):
        self.saldo += valor
    
    def __str__(self):
        return "[>> Codigo {} Saldo {} <<]".format(self.codigo_conta, self.saldo)
    

conta_da_day = ContaCorrente(57)
conta_da_day.deposita(2548)

conta_do_luca = ContaCorrente(2765)
conta_do_luca.deposita(1250)

contas = [conta_da_day,conta_do_luca]

for conta in contas: #Nao entendi em que momento o variavel "conta" foi crianda
    print(conta)
```