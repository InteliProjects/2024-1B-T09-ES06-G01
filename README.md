<Table>
  <tr>
    <td>
      <a href= "https://www.inteli.edu.br/"><img src="./docs/assets/images/inteli.png" alt="Inteli - Instituto de Tecnologia e Liderança" border="0"></a>
    </td>
    <td><a href= "https://www.fdc.org.br/"><img src="./docs/assets/images/fdc.png" alt="Fundação Dom Cabral" border="0"></td>
  </tr>
</table> <br>

# Coffee Break ☕

## Spark 💫

## Integrantes:

- <a href="https://www.linkedin.com/in/gabriellysilvavitor/">Gabrielly Silva Vitor</a>
- <a href="https://br.linkedin.com/in/heitorprudente">Heitor Elias Prudente</a>
- <a href="https://www.linkedin.com/in/joselitojunior">Joselito Júnior Motta de Carvalho</a>
- <a href="https://www.linkedin.com/in/luigiotavio/">Luigi Otávio Neves Macedo</a>
- <a href="https://www.linkedin.com/in/victor-gabriel-marques/">Victor Gabriel Marques</a>


## Professores:

### Orientadora 

- <a href="https://www.linkedin.com/in/vanunes/">Vanessa Nunes</a>

### Instrutores
- <a href="https://br.linkedin.com/in/jefferson-o-silva">Computação - Jefferson de Oliveira</a>
- <a href="https://br.linkedin.com/in/jose-romualdo">Computação - José Romualdo</a>
- <a href="https://br.linkedin.com/in/diogo-martins-gon%C3%A7alves-de-morais-96404732">Matemática e Física - Diogo</a>
- <a href="https://br.linkedin.com/in/rafael-jacomossi-6135b0a1">Negócios - Rafael Jacomossi</a>
- <a href="https://www.linkedin.com/in/gui-cestari/">Design - Guilherme Cestari</a> 
- <a href="https://www.linkedin.com/in/anacristinadossantos/">Liderança - Ana Cristina dos Santos</a>

## 📝 Descrição

O projeto ``"Coffee Break"`` é uma solução integrada que utiliza tecnologias modernas para fornecer uma plataforma robusta e escalável, focada na gestão e otimização de processos de negócios. A arquitetura do projeto segue o paradigma de SOA (Arquitetura Orientada a Serviços) e está implementada com desenvolvimento orientado a testes (TDD), garantindo alta qualidade e confiabilidade do código.

### Backend

O backend é desenvolvido em Flask, uma microframework leve em Python, ideal para a criação de APIs robustas e escaláveis. A estrutura do backend é organizada em diferentes módulos, cada um responsável por funcionalidades específicas, como integração de serviços externos, recomendação de conteúdos, e gestão de projetos e CEOs.

### Frontend

O frontend é desenvolvido utilizando Flutter, um framework de código aberto do Google para a criação de aplicações nativas compiladas, visando alta performance tanto em dispositivos móveis quanto em outras plataformas. A estrutura do frontend é organizada para suportar múltiplas plataformas, incluindo Android, iOS, Web, e outros sistemas operacionais.

### BI (Business Intelligence)

O módulo de BI é responsável pela inteligência de negócios, incluindo a gestão e processamento de dados, bem como a criação de modelos analíticos para suporte à decisão. Este módulo está estruturado para lidar com dados brutos e processados, além de fornecer modelos de dados e scripts para manipulação de banco de dados.

## 📁 Estrutura de pastas

```
docs/
└── assets/
    └── images/
    └── videos/
└── diagramas/
└── outros/
└── wireframe/
└── mockup/
└── index.md
src/
└── backend/
    └── bff_mobile/
    └── ceos/
    └── common/
    └── external/
    └── projetos/
    └── recomendacao/
└── bi/
    └── data/
        └── processed/
        └── raw/
    └── database/
    └── models/
    └── modelo_conteudo.py
└── frontend/
    └── coffeebreak/
        └── android/
        └── assets/
            └── fonts/
            └── icons/
            └── img/
            └── videos/
        └── ios/
        └── lib/
            └── custom/
            └── layouts/
            └── models/
            └── screens/
            └── utils/
            └── widgets/
        └── linux/
        └── macos/
        └── test/
        └── web/
        └── windows/
└── tests/
    └── bff/
    └── ceos/
    └── database/
    └── external/
    └── integration/
    └── projetos/
    └── recomendacao/
.gitignore
README.md
requirements.txt
```

Na raiz do projeto, temos o diretório ``docs/``, que armazena toda a documentação relacionada ao projeto. Dentro deste diretório, há subdiretórios como ``assets/`` que contém imagens e vídeos, ``diagramas/`` para diagramas técnicos, ``outros/`` para documentos diversos, ``wireframe/`` para esboços de telas, e ``mockup/`` para protótipos visuais. O arquivo principal de documentação é o ``index.md``.

O diretório ``src/`` contém o código-fonte do projeto e está dividido em três partes principais: backend, BI e frontend. O backend, implementado em Flask, está localizado em ``src/backend/`` e é subdividido em várias partes, como ``bff_mobile/`` que serve como Backend for Frontend para dispositivos móveis, ``ceos/`` que contém funcionalidades específicas para o projeto CEOS, ``common/`` para funcionalidades compartilhadas, ``external/`` para integrações com sistemas externos, ``projetos/`` para funcionalidades relacionadas a projetos, e ``recomendacao/`` que abrange o módulo de recomendação.

O diretório ``src/bi/`` está relacionado à inteligência de negócios (BI) e é organizado com subdiretórios como ``data/`` que possui os dados processados (``processed/``) e brutos (``raw/``), ``database/`` para configurações e scripts de banco de dados, ``models/`` para os modelos de dados e ``modelo_conteudo.py`` que é um script específico para o BI.

O frontend, desenvolvido em Flutter, está localizado em ``src/frontend/`` e é organizado pelo projeto ``coffeebreak/``, que possui subdiretórios para diferentes plataformas como ``android/``, ``ios/``, ``linux/``, ``macos/``, ``web/`` e ``windows/``. Além disso, há diretórios específicos para ``assets/`` contendo fontes, ícones, imagens e vídeos, ``lib/`` para o código Flutter com subdiretórios para componentes customizados (``custom/``), layouts (``layouts/``), modelos (``models/``), telas (``screens/``), utilitários (``utils/``) e widgets (``widgets/``). Há também um diretório ``test/`` para os testes do frontend.

O diretório ``tests/`` é dedicado aos testes e está subdividido em ``bff/``, ``ceos/``, ``database/``, ``external/``, ``integration/``, ``projetos/`` e ``recomendacao/``, refletindo a estrutura do backend.

Na raiz do projeto, encontram-se arquivos importantes como ``.gitignore`` para especificar quais arquivos ou diretórios devem ser ignorados pelo Git, ``README.md`` que geralmente contém informações básicas sobre o projeto e ``requirements.txt`` que lista as dependências do projeto.

## 💻 Configuração para desenvolvimento

Para configurar o desenvolvimento da aplicação, [instale o git](https://git-scm.com/downloads) e clone esse repositório em seu computador através do comando:

```
git clone https://github.com/Inteli-College/2024-1B-T09-ES06-G01
```

Em seguida siga as instruções presentes em nosso <a href="/documentos/outros/manual-instalacao.md">manual de instalação</a>.

## 🗃 Histórico de lançamentos

> Para visualizar o histórico de lançamentos completo deste projeto, consulte as [tags neste repositório](https://github.com/Inteli-College/2024-1B-T09-ES06-G01/tags), ou diretamente as [releases](https://github.com/Inteli-College/2024-1B-T09-ES06-G01/releases)

## 📋 Licença/License

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/Inteli-College/2024-1B-T09-ES06-G01">Coffee Break</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://www.inteli.edu.br/">INTELI</a>, <a href="https://www.linkedin.com/in/gabriellysilvavitor/">Gabrielly Silva Vitor</a>, <a href="https://br.linkedin.com/in/heitorprudente">Heitor Elias Prudente</a>, <a href="https://www.linkedin.com/in/joselitojunior">Joselito Júnior Motta de Carvalho</a>, <a href="https://www.linkedin.com/in/luigiotavio/">Luigi Otávio Neves Macedo</a>, <a href="https://www.linkedin.com/in/victor-gabriel-marques/">Victor Gabriel Marques</a>, is licensed under <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"></a></p>
