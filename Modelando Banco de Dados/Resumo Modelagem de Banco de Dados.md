# Modelagem de Banco de Dados

[Entrevista clube do livro.docx](Modelagem%20de%20Banco%20de%20Dados%20c895a45f60a34b0b94fd861e40fe7189/Entrevista_clube_do_livro.docx)

**Por que modelar o banco de dados?**

Para evitar gastos desnecessários de espaço, dualidades e etc.

# Modelo Domínio / Modelo Conceitual

O Modelo Domínio de banco de dados é usado para representar os dados e relacionamentos entre os dados no seu negócio. Ele estrutura os dados em termos de entidades, atributos, relacionamentos e regras de negócios. Ele é usado para representar os requisitos de negócios e as relações entre as entidades. O modelo domínio também é útil para identificar os requisitos não funcionais, como a escalabilidade, a manutenibilidade e a performance.

## Ferramentas para modelagem de banco de dados

É possível aplicar as técnicas de modelagem sem o uso de uma ferramenta **CASE** (Computer-Aided Software Engineering, ou Engenharia de Software Assistida por Computador), porém esse trabalho manual seria bem extenso. Além disso, a conversão entre o esquema conceitual para o esquema lógico (redesenhando as formas, por exemplo), pode tornar o trabalho exaustivo e estressante. Usando uma ferramenta CASE conseguimos observar as alterações do modelo, conforme formos tomando as decisões (processo “causa-efeito”).

### Mas será que existe uma ferramenta CASE ideal?

Uma ferramenta CASE precisa possuir a capacidade de utilizar diversas formas geométricas para: desenvolver uma boa representação visual, o dicionário de dados, a integração entre o diagrama entidade/relacionamento e o dicionário de dados, além de possibilitar uma mínima interação com o(a) usuário(a).

Existem várias ferramentas avançadas disponíveis no mercado que podem auxiliar a modelagem de banco de dados. Algumas das mais conhecidas são:

- **[OracleDesigner ™ (Oracle ®)](https://www.oracle.com/database/technologies/developer-tools/designer.html)**: possui uma arquitetura flexível e pode ser instalada em múltiplas plataformas;
- **[PowerDesigner ™ (Sybase ®)](https://www.sapstore.com/solutions/61111/SAP-PowerDesigner)**: um dos mais utilizados no mercado;
- **[ERWin (CA ®)](https://www.erwin.com/br-pt/)**: também é muito utilizado no mercado;
- **[Freeware DBDesigner](https://dbdesigner.softonic.com.br/)**: possui uma grande quantidade de recursos;
- **[PyDesigner](https://pydesigner.readthedocs.io/en/latest/installation/pydesigner.html#pydesigner)**: está disponível para a plataforma Linux;
- **[VISIO ™ (Microsoft ®)](https://www.microsoft.com/pt-br/microsoft-365/visio/flowchart-software)**: ferramenta direcionada exclusivamente para desenho. Você pode conhecer um pouco mais de como o VISIO funciona, neste Alura+ sobre [Excel: Fluxogramas](https://cursos.alura.com.br/extra/alura-mais/excel-fluxogramas-c832).

Durante o curso utilizamos o **brModelo**, mas o que nos levou a essa escolha?

Essa ferramenta possui algumas vantagens como:

- permitir realizar alterações estruturais no modelo, conforme são tomadas novas decisões pela pessoa analista;
- trazer uma atenção especial aos atributos e todas as suas especificações;
- possibilitar uma visualização mais “limpa” do esquema ao ocultar os atributos que não tenham relevância no modelo conceitual, mas que são relevantes no modelo lógico, por exemplo;
- e possuir um dicionário de dados bem completo.

### Minimundo

O conceito de minimundo em banco de dados é um modelo abstrato do mundo real que é criado para armazenar dados relevantes para um determinado contexto ou domínio de negócio. Um minimundo é um subconjunto de dados que representa uma parte do mundo real em um ambiente de banco de dados.

Um exemplo de minimundo seria um banco de dados para uma biblioteca. Neste minimundo, os dados relevantes incluiriam informações sobre livros, autores, editoras, empréstimos e devoluções de livros, entre outras informações. O banco de dados da biblioteca **contém apenas informações relevantes para o contexto** da biblioteca e não informações irrelevantes, como as informações do clima.

Ao modelar um minimundo, o projetista do banco de dados deve levar em consideração as necessidades de negócios da organização, as regras de negócios, a complexidade do ambiente e os requisitos de segurança e privacidade, para garantir que o modelo do minimundo atenda às necessidades dos usuários do sistema.

### MER - Modelo Entidade e Relacionamento

MER (Modelo Entidade e Relacionamento) é um modelo de dados usado para representar os dados e relacionamentos entre os dados em um banco de dados. É usado para representar os requisitos de negócios e as relações entre as entidades. O modelo MER é feito por meio de um diagrama entidade-relacionamento, que usa entidades (tabelas) e relacionamentos (ligações entre entidades) para modelar os dados.

### DER - Diagrama Entidade e Relacionamento

DER (Diagrama Entidade e Relacionamento) é um diagrama que representa o modelo MER. O diagrama DER mostra os elementos de dados (entidades e seus atributos) e as relações entre eles. O diagrama DER é usado para verificar se o modelo MER está correto e se está adequado para o contexto do negócio. Ele também é usado para entender melhor como os dados estão relacionados entre si.

- **Entidade:**

Em modelagem de banco de dados, uma entidade é um objeto ou conceito no mundo real que pode ser distinguido de outros objetos ou conceitos. Essas entidades são representadas como tabelas em um banco de dados e são usadas para armazenar informações sobre o objeto ou conceito que eles representam. Existem dois tipo de entidades:

- **Entidades fortes:**

Entidades fortes são aquelas que **têm uma identidade própria e que podem existir independentemente de outras entidades no banco de dados**. Por exemplo, em um sistema de gerenciamento de biblioteca, a entidade "Livro" é uma entidade forte porque ele pode existir independentemente de outras entidades no banco de dados.

- **Entidades fracas**

Já as entidades fracas são aquelas que **não têm uma identidade própria e dependem de outras entidades para existir**. Elas são identificadas por meio de uma chave estrangeira que é referenciada por uma chave primária de outra tabela. Por exemplo, em um sistema de gerenciamento de biblioteca, a entidade "Cópia de Livro" é uma entidade fraca porque ela depende da entidade "Livro" para existir. Ela tem uma chave primária própria, mas também inclui a chave primária da entidade "Livro" como chave estrangeira.

<aside>
<img src="https://www.notion.so/icons/light-bulb_green.svg" alt="https://www.notion.so/icons/light-bulb_green.svg" width="40px" /> Em resumo, entidades fortes são independentes e têm uma identidade própria, enquanto entidades fracas são dependentes e precisam de outra entidade para existir. A identificação das entidades fortes e fracas é importante para a modelagem de banco de dados, pois ajuda a estabelecer relacionamentos entre as tabelas e garantir a integridade dos dados.

</aside>

## Classificação dos relacionamentos das entidades

Existem três tipos de relacionamentos: **relacionamentos 1:1**, **relacionamentos 1:N** e **relacionamentos N:N:**

- **Relacionamento 1:1**

Um relacionamento 1:1 (um para um) é usado quando **cada instância de uma entidade é relacionada a apenas uma instância de outra entidade**. Por exemplo, um relacionamento 1:1 pode ser usado para relacionar uma pessoa a seu endereço.

- **Relacionamento 1:N**

Um relacionamento 1:N (um para muitos) é usado quando **cada instância de uma entidade é relacionada a múltiplas instâncias de outra entidade**. Por exemplo, um relacionamento 1:N pode ser usado para relacionar um professor a vários alunos.

- **Relacionamento N:N**

Um relacionamento N:N (muitos para muitos) é usado quando **cada instância de uma entidade é relacionada a múltiplas instâncias de outra entidade** e vice-versa. Por exemplo, um relacionamento N:N pode ser usado para relacionar estudantes a disciplinas.

## Cardinalidade dos relacionamentos

A cardinalidade é a especificação da quantidade mínima e máxima de ocorrências que uma entidade pode ter em relação a outra entidade no contexto de um determinado relacionamento em um modelo de banco de dados. Ela é representada por um conjunto de números e símbolos, que indicam a quantidade mínima e máxima de ocorrências permitidas em cada entidade no relacionamento.

A seguir, estão os símbolos mais comuns usados para representar a cardinalidade mínima e máxima nos relacionamentos entre entidades:

- (0,1) ou (0..1): indica que a entidade pode ter zero ou uma ocorrência no relacionamento. Isso significa que a entidade pode estar presente ou não no relacionamento, mas se estiver presente, só pode ocorrer uma vez.
- (1,1) ou (1..1): indica que a entidade deve ter uma ocorrência no relacionamento. Isso significa que a entidade é obrigatória no relacionamento e só pode ocorrer uma vez.
- (0,N) ou (0..N): indica que a entidade pode ter zero ou mais ocorrências no relacionamento. Isso significa que a entidade pode estar presente ou não no relacionamento e, se estiver presente, pode ocorrer mais de uma vez.
- (1,N) ou (1..N): indica que a entidade deve ter uma ou mais ocorrências no relacionamento. Isso significa que a entidade é obrigatória no relacionamento e pode ocorrer mais de uma vez.

Por exemplo, em um sistema de gerenciamento de biblioteca, pode haver um relacionamento entre a entidade "Livro" e a entidade "Autor". A cardinalidade deste relacionamento pode ser (1,N), o que significa que cada livro deve ter pelo menos um autor, mas cada autor pode estar relacionado com vários livros. Ou ainda, pode ser (0,N), o que significa que um livro pode ou não ter um autor e um autor pode ter vários livros. A escolha da cardinalidade depende das necessidades do negócio e do contexto do relacionamento.

<aside>
<img src="https://www.notion.so/icons/flash_green.svg" alt="https://www.notion.so/icons/flash_green.svg" width="40px" /> Ao modelar um banco de dados, é importante levar em consideração a classificação e a cardinalidade dos relacionamentos entre as entidades, para garantir que os dados sejam armazenados corretamente e possam ser recuperados de forma eficiente.

</aside>

## SGBD

SGBD é a abreviatura de Sistema Gerenciador de Banco de Dados. É o software responsável por gerenciar o banco de dados e fornecer uma interface para permitir que os usuários interajam com o banco de dados. Ele também é responsável por garantir a integridade dos dados, a segurança dos dados, a consistência dos dados e a performance. O SGBD é usado para armazenar, recuperar, gerenciar e manipular os dados.

- Abaixo está uma lista dos softwares de SGBD mais usados:

- **Oracle**
    
    ![https://raw.githubusercontent.com/devicons/devicon/master/icons/oracle/oracle-original.svg](https://raw.githubusercontent.com/devicons/devicon/master/icons/oracle/oracle-original.svg)
    
- **MySQL**
    
    ![https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg](https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg)
    
- **Microsoft SQL Server**
    
    ![https://www.svgrepo.com/show/303229/microsoft-sql-server-logo.svg](https://www.svgrepo.com/show/303229/microsoft-sql-server-logo.svg)
    

- **SQLite**
    
    ![https://www.vectorlogo.zone/logos/sqlite/sqlite-icon.svg](https://www.vectorlogo.zone/logos/sqlite/sqlite-icon.svg)
    
- **Redis**
    
    ![https://raw.githubusercontent.com/devicons/devicon/master/icons/redis/redis-original-wordmark.svg](https://raw.githubusercontent.com/devicons/devicon/master/icons/redis/redis-original-wordmark.svg)
    
- **Cassandra**
    
    ![https://www.vectorlogo.zone/logos/apache_cassandra/apache_cassandra-icon.svg](https://www.vectorlogo.zone/logos/apache_cassandra/apache_cassandra-icon.svg)
    

- **PostgreSQL**
    
    ![https://raw.githubusercontent.com/devicons/devicon/master/icons/postgresql/postgresql-original-wordmark.svg](https://raw.githubusercontent.com/devicons/devicon/master/icons/postgresql/postgresql-original-wordmark.svg)
    
- **MongoDB**
    
    ![https://raw.githubusercontent.com/devicons/devicon/master/icons/mongodb/mongodb-original-wordmark.svg](https://raw.githubusercontent.com/devicons/devicon/master/icons/mongodb/mongodb-original-wordmark.svg)
    
- **MariaDB**
    
    ![https://www.vectorlogo.zone/logos/mariadb/mariadb-icon.svg](https://www.vectorlogo.zone/logos/mariadb/mariadb-icon.svg)