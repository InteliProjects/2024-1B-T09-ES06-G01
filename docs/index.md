<table>
  <tr>
    <td>
      <a href= "https://www.inteli.edu.br/"><img src="./assets/images/inteli.png" alt="Inteli - Instituto de Tecnologia e Liderança" border="0"></a>
    </td>
    <td><a href= "https://www.fdc.org.br/"><img src="./assets/images/fdc.png" alt="Fundação Dom Cabral" border="0"></td>
  </tr>
</table>

# Coffee Break ☕

## Spark 💫

## :student: Integrantes:

- <a href="https://www.linkedin.com/in/gabriellysilvavitor/">Gabrielly Silva Vitor</a>
- <a href="https://br.linkedin.com/in/heitorprudente">Heitor Elias Prudente</a>
- <a href="https://www.linkedin.com/in/joselitojunior">Joselito Júnior Motta de Carvalho</a>
- <a href="https://www.linkedin.com/in/luigiotavio/">Luigi Otávio Neves Macedo</a>
- <a href="https://www.linkedin.com/in/victor-gabriel-marques/">Victor Gabriel Marques</a>

## Sumário

- [1. Termos e Abreviações](#termos-abreviacoes)
- [2. Visão Geral do Projeto](#visão-geral-do-projeto)
  - [2.1 Entendimento do Parceiro](#entendimento-parceiro)
    - [2.1.1 Partes Interessadas](#partes-interessadas)
    - [2.1.2 Análise da Indústria](#analise-da-industria)
    - [2.1.3 Modelo de Negócio](#modelo-de-negocio)
    - [2.1.4 Tendências](#tendencias)
    - [2.1.5 Players de Mercado](#players-mercado)
  - [2.2 Problema](#problema)
- [3. Proposta da Solução](#proposta-de-solucao)
  - [3.1 Descritivo Geral da Solução](#descritivo-da-solucao)
  - [3.2 Proposta Tecnológica e Benefícios](#proposta-tecnologica-beneficios)
  - [3.3 Proposta de Valor (Value Proposition Canvas)](#value-canvas)
  - [3.4 Matriz de Risco](#matriz-de-risco)
  - [3.5 Estimativa de Investimento](#estimativa-investimento)
- [4. Análise dos processos](#analise-processos)
  - [4.1 Cadeia de Valor](#cadeia-valor-processos)
  - [4.2 Modelagem de processos](#modelo-bpmn)
- [5. Requisitos](#requisitos)
  - [5.1 Requisitos Funcionais](#requisitos-funcionais)
  - [5.2 Requisitos não Funcionais](#requisitos-não-funcionais)
  - [5.3 Casos de Uso](#casos-de-uso)
  - [5.4 Casos de Uso x Requisitos Funcionais](#casodeuso-reqfunc)
- [6. Projeto de Solução](#projeto-solucao)
  - [6.1 Diagrama de Classes](#diagrama-classes)
  - [6.2 Arquitetura da Solução](#diagrama-arquitetura)
  - [6.3 Diagrama de Implantação](#diagrama-implantacao)
  - [6.4 Tecnologias e Ferramentas](#tecnologias-ferramentas)
  - [6.5 Padrões de Trabalho](#padroes-trabalho)
- [7. Interface](#interface)
  - [7.1 Projeto de Interface (Wireframes)](#wireframe)
  - [7.2 Mockup](#mockup)
  - [7.3 Frontend](#frontend)
  - [7.4 Análise de Usabilidade do Frontend](#usabilidade-frontend)
- [8. Projeto de Banco de Dados](#projeto-de-banco-de-dados)
  - [8.1 Especificação da Base de Dados para Modelo de Recomendação](#basedados-recomendacao)
  - [8.2 - Modelo Conceitual](#modelo-conceitual)
  - [8.3 - Modelo Lógico](#modelo-conceitual)
- [9. Construção da Solução](#testes-de-software)
  - [9.1 Modelo de Recomendação](#modelo-recomendacao)
  - [9.2 Estrutura da solução](#estrutura-solucao)
- [10. Testes de Software](#testes-de-software)
  - [10.1 Testes de Usabilidade para Mockup](#teste-de-usabilidade)
  - [10.2 Testes de Integração](#teste-de-integracao)
  - [10.3 Testes da API Externa](#teste-automatizado)
  - [10.5 Testes de Integração do Modelo de Recomendação](#teste-de-rnf)
- [11. Procedimento de Implantação da Solução](#procedimento-implantacao)
  - [11.1 Procedimento de Implantação do Sistema](#procedimento-implantacao-sistema)
  - [11.2 Procedimento de Implantação do Banco de Dados](#procedimento-implantacao-bd)
  - [11.3 Documentação Automática do Sistema](#documentacao-automatica)
- [Referências](#referências)
- [Apêndice](#apêndice)

# 1. Termos e Abreviações

&emsp;&emsp;No desenvolvimento do aplicativo `CoffeeBreak`, destinado a otimizar a experiência e contribuir para a criação de legados por meio de projetos colaborativos dos CEOs parceiros da Fundação Dom Cabral (FDC), foram identificados diversos termos e abreviações utilizados ao longo do documento. A compreensão clara e eficaz desses termos é essencial para a implementação bem sucedida do projeto. Portanto, foi desenvolvida uma tabela com os principais termos e abreviações destacados na implementação da solução CoffeeBreak. Este esforço é fundamental para assegurar que todos os membros da equipe estejam alinhados e entendam os conceitos chave que guiam o desenvolvimento e a operação do aplicativo.

&emsp;&emsp;Com isso, se faz necessário entender todos esses termos e abreviações, sendo de extrema importância por se tratarem de fundamentos que corroboram para a compreensão total e para a melhor execução do aplicativo "Coffee Break", desenvolvido para o gerenciamento de sinergias de projetos entre os CEOs parceiros Fundação Dom Cabral. Além dos itens listados, outros termos e abreviações podem surgir ao longo do desenvolvimento. Em caso de dúvidas, é fundamental buscar o significado desses termos adicionais para garantir que todos os envolvidos estejam alinhados e possam colaborar de forma eficiente. Segue abaixo uma lista detalhada dos principais termos e abreviações utilizados na solução CoffeeBreak:

| Termo e Abreviação | Descrição |
| ------------------ | --------- |
| **CoffeeBreak** | Refere-se à solução proposta para melhorar a logística e a gestão dos intervalos de café em eventos, visando proporcionar uma experiência mais agradável e eficiente aos participantes. |
| **FDC** | Fundação Dom Cabral, a instituição parceira para a qual a Solução CoffeeBreak está sendo desenvolvida. |
| **App** | Abreviação de “Application” (Aplicativo), utilizado para descrever a plataforma digital que será criada para gerenciar as funcionalidades da Solução CoffeeBreak. |
| **UI** | User Interface (Interface do Usuário). Refere-se ao design e à disposição dos elementos visuais que compõem a aplicação, com o objetivo de proporcionar uma experiência intuitiva e agradável ao usuário. |
| **UX** | User Experience (Experiência do Usuário). Engloba todos os aspectos da interação do usuário com a aplicação, buscando tornar a navegação e utilização do app o mais eficiente e satisfatória possível. |
| **API** | Application Programming Interface (Interface de Programação de Aplicações). Um conjunto de rotinas e padrões estabelecidos por uma aplicação para que outras aplicações possam interagir com ela. |
| **DB** | Database (Banco de Dados). Sistema que será utilizado para armazenar todas as informações relevantes sobre os eventos, participantes, preferências de café, entre outros dados necessários para o funcionamento da Solução CoffeeBreak. |
| **AWS** | Amazon Web Services. Plataforma de serviços de computação em nuvem que será utilizada para hospedar a aplicação e os dados da Solução CoffeeBreak, garantindo escalabilidade e segurança. |
| **EC2** | Elastic Compute Cloud. Serviço de computação em nuvem da AWS que fornece capacidade de computação escalável na nuvem, utilizado para executar a aplicação CoffeeBreak. |
| **Frontend** | Parte da aplicação que interage diretamente com o usuário, desenvolvida com foco em usabilidade e design. No caso da Solução CoffeeBreak, o frontend será desenvolvido utilizando Flutter e Dart. |
| **Backend** | Parte da aplicação que processa a lógica de negócios, gerencia as interações com o banco de dados e garante a funcionalidade da aplicação. No caso da Solução CoffeeBreak, o backend será desenvolvido utilizando Flask. |
| **Flutter** | Framework de desenvolvimento de aplicações criado pelo Google, utilizado para criar o frontend da Solução CoffeeBreak, permitindo a criação de interfaces nativas para iOS e Android. |
| **Dart** | Linguagem de programação utilizada em conjunto com o Flutter para o desenvolvimento do frontend da Solução CoffeeBreak. |
| **MVP** | Minimum Viable Product (Produto Viável Mínimo). Versão inicial da Solução CoffeeBreak com funcionalidades essenciais para ser lançada e testada, permitindo obter feedback dos usuários para futuras melhorias.

&emsp;&emsp;Ao familiarizar-se com esses termos e abreviações, todos os envolvidos no projeto, desde a equipe de desenvolvedores até os usuários e stakeholders da FDC, poderão colaborar de maneira mais eficiente e alinhada. A clareza na comunicação é crucial para o sucesso do projeto, garantindo que todos compreendam os objetivos e os meios utilizados para alcançá-los. A Solução CoffeeBreak, voltada para os CEOs parceiros da Fundação Dom Cabral, pretende não apenas melhorar a logística dos eventos, mas também fomentar uma cultura de colaboração e inovação contínua, impulsionando os projetos de ESG a novos patamares de excelência.

# 2. Visão Geral do Projeto

&emsp;&emsp;O projeto desenvolvido em parceria com a Fundação Dom Cabral (FDC) consiste na solução desenvolvida pela grupo Spark chamada "Coffee Break", que tem como objetivo principal criar um aplicativo mobile voltado para os CEOs colaboradores da fundação, visando promover uma maior interação e engajamento entre seus projetos de ESG (Environmental, Social, and Governance). A iniciativa busca proporcionar uma plataforma integrada onde os líderes empresariais possam realizar sinergias de aprendizado, integração ou união, além de compartilhar e acompanhar o progresso das iniciativas sustentáveis, reforçando o compromisso da fundação com práticas empresariais responsáveis e sustentáveis.

<div align="center">
  <sub>Figura 1 - Coffee Break</sub>
  <img src="./assets/images/coffeebreak.png" width="100%" alt='Coffee Break'>
  <sup>Fonte: Os autores (2024)</sup>
</div>

&emsp;&emsp;Para a construção deste aplicativo, foram utilizadas tecnologias modernas e eficientes. O frontend do aplicativo é desenvolvido com Flutter utilizando a linguagem Dart, escolhida por sua capacidade de criar interfaces de usuário nativas e de alta performance. O backend é estruturado com Flask, um framework de micro serviços em Python, conhecido por sua simplicidade e flexibilidade. O banco de dados utilizado é o PostgreSQL, garantindo escalabilidade, e será hospedado em instâncias EC2 da AWS, oferecendo segurança e desempenho necessários para suportar o crescimento e a demanda do aplicativo. Mais informações sobre tecnologias e ferramentas utilizada na seção 6.4 deste documento.

&emsp;&emsp;De modo geral, este projeto visa proporcionar um ambiente digital que facilita a colaboração entre projetos empresariais de ESG e, consequentemente, a criação de legados por parte dos CEOs parceiros da Fundação Dom Cabral. Dessa forma, espera-se que por meio dessa solução seja possível proporcionar mais sinergias e aprendizados para todos os envolvidos, solucionando a problemática apresentada pela FDC. Além disso, esse projeto pode ser visto como uma solução extremente única, diferenciada e que contribue diretamente, não só para o avanço dos trabalhos da Fundação, mas também proporcionando meios para a contrução de uma sociedade brasileira mais igualitária e consciente.

## 2.1 Entendimento do Parceiro

&emsp;&emsp;No desenvolvimento do aplicativo CoffeeBreak, a parceria com a Fundação Dom Cabral (FDC) se destaca como um dos principais alicerces do projeto. A FDC é uma instituição renomada, focada em capacitação e desenvolvimento de líderes empresariais, proporcionando uma base sólida de conhecimento e recursos para o sucesso do projeto. A compreensão das necessidades e expectativas da FDC é crucial para o alinhamento das metas do projeto com os objetivos estratégicos da fundação. A colaboração com CEOs de diversas empresas, que são parceiros da FDC, acrescenta uma camada adicional de complexidade e enriquecimento ao projeto, pois incorpora visões e experiências práticas do mercado.

### 2.1.1 Partes Interessadas

&emsp;&emsp;As partes interessadas no projeto CoffeeBreak incluem uma gama diversificada de stakeholders que desempenham papéis cruciais no desenvolvimento, implementação e utilização da solução. Cada grupo traz uma perspectiva única e contribuições valiosas que são fundamentais para o sucesso do projeto. Primeiramente, os **CEOs parceiros da Fundação Dom Cabral** são os principais usuários finais do aplicativo. Estes líderes empresariais trazem suas necessidades e expectativas específicas relacionadas à gestão de projetos colaborativos e à otimização de intervalos em eventos corporativos, fornecendo insights práticos e feedback contínuo que orientam o desenvolvimento do aplicativo.

1. **CEOs Parceiros da Fundação Dom Cabral**: Estes líderes empresariais são os principais usuários finais do aplicativo. Suas expectativas e necessidades em relação à gestão de projetos colaborativos e intervalos em eventos corporativos são fundamentais para o sucesso da solução. A interação direta com esses CEOs permitirá um feedback contínuo e a adequação do aplicativo às suas preferências e necessidades específicas.

2. **Fundação Dom Cabral (FDC)**: Como parceira principal, a FDC fornece o suporte institucional e os recursos necessários para o desenvolvimento do projeto. A fundação também atua como intermediária entre os desenvolvedores e os CEOs parceiros, facilitando a comunicação e garantindo que os objetivos do projeto estejam alinhados com a missão da FDC.

3. **Inteli**: Esta organização contribui com expertise técnica e inovação, garantindo que as soluções tecnológicas utilizadas no desenvolvimento do CoffeeBreak sejam de ponta e adequadas às demandas do projeto. A Inteli desempenha um papel fundamental auxiliando os alunos, membros do Grupo Spark, na garantia da qualidade técnica e na implementação das melhores práticas de desenvolvimento de software.

4. **Grupo Spark**: o Grupo Spark agrega valor ao produzir a solução por inteiro para a Fundação Dom Cabral, que será diretamente utilizada pelos CEOs, e claro, tudo isso com o apoio do Inteli. Assim, por meio dos conhecimentos técnicos e aprendizados em equipe durante todo o processo de idealização e desenvolvimendo do aplicativo "Coffee Break", o Grupo Spark apresenta uma solução robusta e com uma qualidade impressionante!

&emsp;&emsp;A colaboração entre essas partes interessadas é essencial para o desenvolvimento de um aplicativo que atenda às expectativas de todos os envolvidos, garantindo uma solução eficiente e inovadora. Cada grupo de stakeholders traz uma perspectiva única e uma gama de competências que, quando combinadas, criam um ambiente propício para a inovação e a excelência. A interação contínua e o diálogo aberto entre os CEOs parceiros, a Fundação Dom Cabral, a Inteli e o Grupo Spark permitem a identificação rápida de desafios e a implementação de soluções criativas e eficazes. Por fim, a entrega de uma solução extremente eficiente, atraente e personalizada.

### 2.1.2 Análise da Indústria

&emsp;&emsp;Neste módulo de Engenharia de Software do Inteli, o parceiro de projetos é a renomada Fundação Dom Cabral (FDC). A Fundação Dom Cabral é uma importante instituição brasileira de ensino e pesquisa em administração e gestão. Fundada em 1976, a FDC tem sua sede em Nova Lima, Minas Gerais, e é reconhecida internacionalmente por seus programas de educação executiva, consultoria, pesquisa e desenvolvimento de executivos. O contexto FDC está intimamente ligado ao mundo dos negócios, da gestão e da administração. A instituição atua oferecendo programas de educação executiva, como MBAs, cursos de especialização, workshops e programas customizados para empresas e CEOs. Além disso, a FDC também realiza pesquisas aplicadas e consultorias para organizações públicas e privadas.

&emsp;&emsp;A FDC se destaca por sua abordagem inovadora, que combina teoria e prática, promovendo o desenvolvimento de líderes e gestores capazes de enfrentar os desafios do ambiente de negócios contemporâneo. Seus programas são conhecidos por sua excelência acadêmica, corpo docente qualificado e pela capacidade de promover transformações significativas nas organizações e na sociedade como um todo.No contexto brasileiro, a FDC desempenha um papel importante na formação de líderes empresariais e na promoção do desenvolvimento econômico e social do país, contribuindo para o avanço da gestão e da administração no Brasil e no mundo.

### 2.1.3 Modelo de Negócio

&emsp;&emsp;Um modelo de negócio é um conceito estrutural que define a lógica de funcionamento de uma organização. Ele detalha como uma empresa cria, entrega e captura valor econômico, social ou de outro tipo. O modelo de negócio abrange vários aspectos importantes para a perenidade da instituição no mercado, incluindo a proposta de valor, a infraestrutura, os clientes e as finanças. Esse modelo é fundamental para garantir que a organização mantenha um funcionamento sustentável e competitivo na sociedade, adaptando-se às mudanças da economia, atendendo às necessidades de seus stakeholders e proporcionando maior crescimento em relação ao propósito da empresa em questão.

&emsp;&emsp;O modelo de negócio da Fundação Dom Cabral é caracterizado por uma proposta de valor centrada no desenvolvimento executivo, sendo considerada uma das principais escolas de negócios do Brasil, reconhecida por sua excelência em educação executiva, desenvolvimento de lideranças e consultoria em gestão empresarial. Além disso, possui uma infraestrutura de alta qualidade, uma rede robusta de parcerias e etc. Esses elementos combinados permitem à FDC manter sua posição de liderança no mercado de educação executiva e continuar a gerar valor significativo. Segue abaixo cada elemento e sua respectiva descrição, permitindo assim maior compreensão sobre a posição de mercado da FDC:

**Proposta de Valor:**

- A proposta de valor da FDC é oferecer educação executiva de alta qualidade, com programas customizados e pesquisa aplicada que atendam às necessidades de desenvolvimento de executivos, gestores e empresários. A FDC se posiciona como uma ponte entre a teoria e a prática gerencial, promovendo a inovação, o pensamento crítico e o desenvolvimento sustentável nas organizações.

**Segmentos de Clientes:**

- A FDC atende a um amplo espectro de clientes que inclui desde pequenas e médias empresas até grandes corporações, além de executivos e profissionais que buscam aprimoramento individual. A fundação também desenvolve projetos para o setor público e organizações do terceiro setor.

**Canais:**

- A FDC utiliza uma variedade de canais para entregar sua proposta de valor, incluindo programas presenciais no campus, treinamentos in company, plataformas digitais de aprendizagem e parcerias com outras instituições educacionais e organizações para ampliar seu alcance.

**Relacionamento com Clientes:**

- O relacionamento é mantido através de um acompanhamento personalizado, onde a FDC se destaca por seu forte envolvimento na jornada de aprendizagem de cada cliente, fornecendo suporte contínuo e acesso a uma vasta rede de ex-alunos.

**Fontes de Receita:**

- As principais fontes de receita da FDC vêm dos cursos oferecidos, programas customizados para empresas, consultoria organizacional, e projetos de pesquisa aplicada. A fundação também pode receber doações e patrocínios, dada sua natureza de organização educacional sem fins lucrativos.

**Recursos Principais:**

- Os recursos que sustentam o modelo de negócio da FDC incluem um corpo docente altamente qualificado, parcerias internacionais, uma infraestrutura física de ponta para a realização de seus programas e uma sólida reputação no mercado educacional.

**Atividades-Chave:**

- A FDC se dedica a atividades como desenvolvimento de conteúdo educacional atualizado, pesquisa em gestão e negócios, networking e parcerias estratégicas, além de constante inovação pedagógica.

**Parcerias Principais:**

- As parcerias são essenciais para o modelo de negócio da FDC, incluindo colaborações com outras instituições de ensino, empresas de consultoria, organizações setoriais e tecnológicas que complementam e enriquecem sua oferta educativa.

**Estrutura de Custos:**

- A estrutura de custos envolve investimentos em desenvolvimento de programas, manutenção de instalações, salários de professores e equipe administrativa, tecnologia para suporte de plataformas de e-learning e marketing para a promoção de seus programas.

&emsp;&emsp;Combinando estes elementos, o modelo de negócio da Fundação Dom Cabral reflete seu compromisso com a excelência em educação gerencial e desenvolvimento de lideranças, focando em criar um impacto significativo nas organizações e na sociedade. Este compromisso é evidenciado pela maneira como a FDC integra seus recursos, conhecimentos e parcerias estratégicas para oferecer programas educacionais que não apenas capacitam executivos, mas também promovem uma cultura de liderança inovadora e ética. A Fundação se dedica a formar líderes que são capazes de transformar suas organizações e contribuir para um desenvolvimento sustentável e inclusivo.

### 2.1.4 Tendências

&emsp;&emsp;Na indústria da Fundação Dom Cabral, algumas tendências emergentes se destacam, refletindo as demandas e desafios do cenário empresarial atual. Uma dessas tendências, semelhante à observada no Instituto de Tecnologia e Liderança (Inteli), é a crescente ênfase na transformação digital. As organizações estão buscando adaptar suas operações e estratégias para aproveitar ao máximo as tecnologias emergentes, como inteligência artificial, análise de big data e automação de processos, para aumentar a eficiência, inovar produtos e serviços, e melhorar a tomada de decisões. Assim, proporcionam tomadas de decisões mais conscientes e qualitativas.

&emsp;&emsp;Além disso, há uma crescente valorização da sustentabilidade e da responsabilidade social corporativa, com empresas buscando integrar práticas ambientalmente conscientes e socialmente responsáveis em suas estratégias de negócios. A globalização contínua também influencia a indústria, exigindo que líderes e gestores desenvolvam habilidades de liderança interculturais e capacidade de atuar em mercados diversificados. Em resposta a essas tendências, a Fundação Dom Cabral continua aprimorando seus programas educacionais e serviços de consultoria para capacitar líderes e organizações a enfrentar esses desafios de forma eficaz e inovadora.

&emsp;&emsp;Ademais, a educação executiva e o desenvolvimento de habilidades empreendedoras estão ganhando um novo enfoque dentro da Fundação Dom Cabral. O crescente mercado de startups e a necessidade de inovação rápida impulsionam a demanda por programas que não apenas ensinem gestão tradicional, mas também fomentem a agilidade, a criatividade e a capacidade de rápida adaptação em ambientes de negócios voláteis. Isso inclui a integração de métodos ágeis de gestão de projetos e o pensamento design como ferramentas essenciais no currículo de futuros líderes, que de certa forma são fundamentos ensinados pelo Funação Dom Cabral.

&emsp;&emsp;Além do mais, outro aspecto relevante é o aumento do foco na análise de dados e na tomada de decisão baseada em evidências. Com o volume de dados disponíveis crescendo exponencialmente, há uma necessidade crítica de líderes que possam interpretar e aplicar esses dados de maneira estratégica, econômica e eficiente. A Fundação Dom Cabral está atenta a essa realidade, desenvolvendo e incorporando em seus cursos habilidades avançadas de data science e análise estatística, preparando os CLevels/gestores para utilizar esses dados como uma vantagem competitiva perante os formandos de outras instituições de liderança empresarial.

### 2.1.5 Players de Mercado

&emsp;&emsp;No mercado de educação executiva e consultoria em gestão, a Fundação Dom Cabral se destaca e enfrenta a concorrência de diversas instituições. Esses players competem por oferecer programas de alta qualidade, inovação educacional e impacto significativo para empresas e líderes, em relação aos ensinamentos de gestão empresarial mais inovadora e eficiente. A competição se dá tanto no mercado nacional quanto no internacional, exigindo que a FDC mantenha um padrão de excelência e esteja sempre atenta às tendências e demandas do setor. Segue abaixo os players de mercado mais significativos que competem diretamente com a FDC: 

<div align="center">
  <sub>Figura 2 - Coffee Break</sub>
  <img src="./assets/images/fgv-executiva.jpg" width="100%" alt='Imagem FGV'>
  <sup>Fonte: Os autores (2024)</sup>
</div>

- **Fundação Getulio Vargas (FGV)**: A FGV é uma das mais prestigiadas instituições de ensino e pesquisa do Brasil, oferecendo uma vasta gama de cursos de graduação, pós-graduação e programas de educação executiva. Suas escolas, incluindo a Escola Brasileira de Administração Pública e de Empresas (EBAPE) e a Escola de Administração de Empresas de São Paulo (EAESP), são renomadas tanto nacional quanto internacionalmente pela excelência em seus programas de administração e gestão. A FGV é conhecida por seu rigor acadêmico, forte impacto na formação de líderes empresariais e por manter uma sólida reputação de qualidade e inovação em educação executiva.

<div align="center">
  <sub>Figura 3 - Coffee Break</sub>
  <img src="./assets/images/insper.jpg" width="100%" alt='Imagem INSPER'>
  <sup>Fonte: Os autores (2024)</sup>
</div>

- **Insper**: O Insper é uma instituição de ensino superior privada com foco em negócios, economia, direito e engenharia. Oferece programas de graduação, pós-graduação e educação executiva, destacando-se pelo desenvolvimento de líderes e gestores para o mercado corporativo. A Escola de Negócios do Insper é amplamente reconhecida por sua excelência acadêmica, combinando rigor teórico com práticas aplicadas, o que facilita uma aprendizagem que prepara seus alunos para enfrentar desafios reais no ambiente empresarial. Além disso, o Insper mantém uma forte conexão com o mercado, proporcionando aos estudantes oportunidades de networking e integração direta com profissionais e empresas líderes em seus setores.

<div align="center">
  <sub>Figura 4 - Coffee Break</sub>
  <img src="./assets/images/insead.jpg" width="100%" alt='Imagem INSEAD'>
  <sup>Fonte: Os autores (2024)</sup>
</div>

- INSEAD: Apesar de ser uma instituição estrangeira, o INSEAD é um competidor relevante no mercado de educação executiva no Brasil, especialmente para programas de MBA e educação executiva de nível internacional. Com campi na Europa, Ásia, Oriente Médio e América do Norte, o INSEAD é conhecido por sua abordagem global e pela formação de líderes globais com uma visão internacional dos negócios. Embora não seja uma instituição brasileira, muitos profissionais brasileiros buscam seus programas devido à reputação internacional da escola e à rede de contatos globais que oferece.

## 2.2 Problema

&emsp;&emsp;Para melhor compreensão, de acordo com a TAPI apresentada pelo Inteli para o desenvolvimento da solução, o desafio principal consiste na falta de uma ferramenta mobile que centralize a capacidade de administrar os registros e interações de projetos e detectar potenciais sinergias de aprendizado, interação e união entre os mesmos, por parte dos CEOs parceiros da Fundação Dom Cabral. Com isso, se fez necessário construir uma solução mobile utilizadno a Arquitetura Orientada a Serviços (SOA), para facilitar a conexão entre as funcionalidades dos serviçõs do sistema.

&emsp;&emsp;Atualmente, a gestão de todos os projetos e informações dos CEOs do CEOs’Legacy é feita manualmente por um funcionário utilizando o Excel. Embora esse método possa ser eficaz no presente momento, a entrada de novos CEOs e o aumento do volume de projetos tornarão o processo cada vez mais complexo e propenso a erros. Além disso, a ausência de uma comunicação direta entre os CEOs dificulta o entendimento profundo dos projetos uns dos outros, limitando a colaboração e a identificação de oportunidades de sinergia.

&emsp;&emsp;A necessidade identificada é de uma solução que permita a gestão eficiente das interações e registros de projetos pelas empresas do CEOs’Legacy, com um enfoque particular na busca de sinergias entre os projetos. É crucial que a ferramenta seja capaz de identificar possíveis sinergias dentro dos temas estabelecidos, proporcionando aos CEOs a oportunidade de conhecer mais sobre os projetos dos seus pares, expressar interesses e estabelecer colaborações estratégicas. Dessa forma, a solução deve facilitar não apenas a administração dos projetos, mas também promover uma rede de colaboração dinâmica e eficiente entre os CEOs, potencializando o impacto dos projetos desenvolvidos.

# 3. Proposta da Solução

&emsp;&emsp;Inicialmente, este tópico apresentará uma descrição geral da solução, abrangendo a proposta tecnológica e seus benefícios, a proposta de valor, a matriz de riscos e a estimativa de investimento. A proposta tecnológica será detalhada, evidenciando as tecnologias utilizadas e como elas se relacionam para formar uma solução integrada e eficiente, incluindo uma análise dos componentes técnicos, arquiteturas de sistema e ferramentas empregadas. Além disso, os benefícios esperados serão discutidos, destacando as vantagens para a organização e os usuários finais. Assim, a solução será apresentada de forma abrangente, oferecendo uma visão completa do projeto tanto do ponto de vista técnico quanto negócios.

## 3.1 Descritivo Geral da Solução

&emsp;&emsp;A solução a ser desenvolvida, chamada de `Coffee Break`, é um aplicativo móvel que visa melhorar a gestão e a visualização das sinergias entre projetos de empresas associadas ao _CEOs’ Legacy_. Utilizando tecnologias de sistemas de recomendação e uma interface otimizada para dispositivos móveis, o aplicativo permitirá que os CEOs e gestores de projeto identifiquem oportunidades de colaboração de forma mais eficiente e eficaz. O `Coffee Break` facilitará a conexão entre projetos complementares, permitindo uma análise rápida e precisa das áreas em que as empresas podem trabalhar juntas para alcançar objetivos comuns. Dessa forma, `Coffee Break` não apenas otimiza a gestão de projetos, mas também promove um ambiente colaborativo e inovador entre as empresas associadas ao _CEOs’ Legacy_.

- **CEOs das Empresas Associadas**: Como os principais usuários do aplicativo, os CEOs poderão explorar e identificar projetos de interesse, promovendo uma maior colaboração interempresarial e potencializando o impacto e legado de suas iniciativas.

- **Equipe Técnica (Desenvolvedores e Designers)**: Encarregados de desenvolver e manter o aplicativo, garantindo que a plataforma seja robusta, segura e fácil de usar.

- **Orientadores Acadêmicos e Inteli**: Incluindo a orientadora do curso, que se beneficiará ao ver como os estudantes aplicam conhecimentos práticos para resolver problemas reais, reforçando o vínculo entre teoria e prática.

- **Fundação Dom Cabral**: Como parceira do projeto, a FDC poderá utilizar o aplicativo para promover a colaboração entre as empresas associadas, fortalecendo a rede de contatos e a troca de experiências.

&emsp;&emsp;Destarte, é possível notar que o aplicativo `Coffee Break` abrange uma quantidade significativa de partes interessadas, cada uma com suas próprias necessidades e expectativas. Para atender a essas demandas, a solução proposta foi projetada para ser flexível, escalável e fácil de usar, garantindo que todos os usuários possam se beneficiar dela de maneira eficaz. A flexibilidade do aplicativo permite personalizações conforme as necessidades específicas de cada usuário, enquanto a escalabilidade assegura que a solução possa crescer e se adaptar ao aumento da demanda e ao número de usuários. A usabilidade foi planejada para proporcionar uma experiência intuitiva, facilitando o uso contínuo do aplicativo. A seguir, serão apresentados os principais **benefícios da solução** envolvidos no projeto:

- **Para os CEOs das Empresas Associadas**: O sistema de recomendação analisará as informações dos projetos para sugerir potenciais sinergias, baseando-se em critérios como áreas de interesse, objetivos de negócio e impacto social. Isso facilitará a descoberta de novas oportunidades de colaboração. Ademais, a interface _mobile-first_ permitirá que os CEOs interajam com as informações dos projetos de maneira intuitiva, usando gestos e toques para navegar, o que é ideal para usuários em constante movimento.

- **Para a Equipe Técnica**: A solução proposta permitirá que os desenvolvedores e designers apliquem seus conhecimentos em tecnologias de ponta, como sistemas de recomendação e interfaces móveis, para criar uma plataforma inovadora e de alto impacto. Além disso, a experiência adquirida no desenvolvimento do aplicativo poderá ser utilizada em projetos futuros, enriquecendo o portfólio e a empregabilidade dos membros da equipe.

- **Para os Orientadores Acadêmicos e Inteli**: A solução `Coffee Break` servirá como um exemplo prático de como os conceitos aprendidos em sala de aula podem ser aplicados para resolver problemas reais, sobretudo no que diz respeito ao curso de Engenharia de Software do Inteli. Isso reforçará a importância da formação prática e da interação com o mercado de trabalho, preparando os estudantes para os desafios do mundo profissional.

&emsp;&emsp;Em suma, a solução proposta neste projeto, realizado em uma parceria entre o Inteli e a FDC, por meio do grupo `Spark`, tem o potencial de transformar a maneira como os CEOs e gestores de projeto interagem e colaboram, promovendo uma cultura de inovação e sinergia entre as empresas associadas ao _CEOs’ Legacy_. Através do aplicativo `Coffee Break`, as empresas poderão identificar e explorar novas oportunidades de colaboração de forma mais eficiente e eficaz, otimizando recursos e promovendo o crescimento conjunto. Além de facilitar a comunicação e o alinhamento entre os projetos, fortalece as relações profissionais e contribui para o desenvolvimento de forma colaborativa. 

## 3.2 Proposta Tecnológica e Benefícios

&emsp;&emsp;A seguir, serão apresentadas as tecnologias utilizadas para o desenvolvimento da aplicação `Coffee Break`, suas propostas e benefícios. A aplicação combina tecnologias modernas como **Flutter** e **Dart** para o frontend, garantindo uma interface responsiva. O **Flask** está sendo utilizado no backend, proporcionando uma estrutura eficiente para APIs. Para os modelos de recomendação, está sendo empregado **Python**, **Apache Spark** e a biblioteca **Pandas**, permitindo manipulação de dados eficiente. O banco de dados é o **PostgreSQL**, conhecido por sua robustez e escalabilidade. Para hospedagem, usamos **AWS**, que oferece infraestrutura segura e escalável. Essa combinação assegura uma solução completa e integrada, atendendo às necessidades do escopo do projeto.

### Frontend

&emsp;&emsp;**Flutter:** O Flutter é um framework de desenvolvimento de aplicativos móveis criado pelo Google. Ele permite que os desenvolvedores criem aplicativos mais atraentes e de alto desempenho para iOS e Android a partir de uma única base de código. O Flutter usa a linguagem de programação **Dart**, que é fácil de aprender, tem excelente suporte para programação assíncrona e é otimizada para UI.

### Backend

&emsp;&emsp;**Flask:** : O Flask é um framework leve para Python, escolhido para desenvolver a camada de backend da aplicação. Sua simplicidade e flexibilidade permitem que a equipe construa APIs robustas e escaláveis para atender às necessidades do aplicativo. O Flask facilita a implementação de rotas, autenticação de usuários, gerenciamento de solicitações HTTP e integração com outros serviços, proporcionando uma base sólida para a lógica de negócios da aplicação.

&emsp;&emsp;**Apache Spark**: Uma plataforma de processamento de dados de código aberto conhecida por seu desempenho rápido, alcançando velocidades até 100 vezes mais rápidas que o Hadoop MapReduce em memória. Ele suporta processamento em tempo real, batch, e streaming, oferecendo APIs simples para Java, Scala, Python e R. Spark é amplamente utilizado para análises de big data, aprendizado de máquina e processamento de dados distribuídos.

&emsp;&emsp;**BFFs:** É proposto o uso de dois BFFs (Backends For Frontends) em vez de um único API Gateway, separados para os dashboards em desktop (Dashboard BFF) e a aplicação no smartphone (Mobile BFF). Isso permite que cada frontend tenha seu próprio backend que lidará com os serviços, otimizado para suas necessidades específicas e facilitando a manutenção.

### Modelos de recomendação

&emsp;&emsp;A aplicação utiliza dois modelos de recomendação para fornecer sugestões personalizadas aos usuários: Filtragem Colaborativa por Usuário e Filtragem por Conteúdo.

&emsp;&emsp;**Filtragem Colaborativa por Usuário:** A Filtragem Colaborativa por Usuário é um método de recomendação que se baseia na ideia de que usuários que concordaram no passado tendem a concordar no futuro. Para cada usuário, o sistema recomenda itens que usuários semelhantes também gostaram. Este método é particularmente útil para recomendar itens que são populares entre um grupo de usuários semelhantes.

&emsp;&emsp;**Filtragem por Conteúdo:** A Filtragem por Conteúdo é um método de recomendação que utiliza informações específicas sobre itens para fazer recomendações. Este método recomenda itens parecidos entre si, com base em uma comparação de conteúdo. Por exemplo, se um usuário gostou de um item específico, o sistema recomendará itens que são semelhantes a esse item. Essa filtragem utiliza o framework **Apache Spark**.

### Banco de dados

&emsp;&emsp;**PostgreSQL:** PostgreSQL é um sistema de gerenciamento de banco de dados relacional bem estruturado e seguro. Ele oferece recursos avançados de segurança, escalabilidade e conformidade com padrões, além de ser altamente extensível. É uma escolha sólida para armazenar e gerenciar os dados da aplicação.

### Hospedagem

&emsp;&emsp;**AWS:** A Amazon Web Services (AWS) é uma plataforma de computação em nuvem altamente escalável e confiável. Ela oferece uma ampla gama de serviços, como computação, armazenamento, banco de dados, segurança e machine learning, que podem atender às necessidades de hospedagem da aplicação móvel.

#### Principais benefícios

- **Escalabilidade Automática:** A capacidade de dimensionar recursos de acordo com a demanda permite garantir uma experiência consistente aos usuários, independentemente do volume de tráfego.

- **Confiabilidade e Segurança:** A AWS oferece padrões de segurança líderes do setor, garantindo a proteção dos dados dos nossos usuários. Além disso, sua infraestrutura globalmente distribuída aumenta a confiabilidade da nossa aplicação.

- **Ampla Gama de Serviços:** Além dos recursos utilizados na aplicação, a AWS oferece uma vasta variedade de outros serviços, desde armazenamento e computação até machine learning e segurança, permitindo que personalizar a infraestrutura de acordo com as necessidades específicas da aplicação.

#### Recursos da AWS

- **Amazon EC2 (Elastic Compute Cloud):** O Amazon EC2 oferece capacidade de computação redimensionável na nuvem, flexibilidade para escolher o tipo de instância, sistema operacional, armazenamento e configurações de rede de acordo com os requisitos da sua aplicação. É neste serviço que será hospedada a aplicação.

- **Amazon RDS (Relational Database Service):** O Amazon RDS oferece um serviço de banco de dados relacional gerenciado na nuvem. nele será hospedado o banco de dados PostgreSQL. O RDS gerencia tarefas administrativas como provisionamento de hardware, backups, aplicação de patches e monitoramento, permitindo que os desenvolvedores se concentrem no desenvolvimento da aplicação sem se preocuparem com a infraestrutura de banco de dados.

## 3.3 Proposta de Valor (Value Proposition Canvas)

&emsp;&emsp;O Value Proposition Canvas (VPC) é uma ferramenta estratégica amplamente utilizada no desenvolvimento e aprimoramento de produtos e serviços, com foco na criação de valor para o cliente. Essa ferramenta permite uma visão detalhada sobre como um produto ou serviço pode atender às expectativas e resolver as necessidades dos clientes. O VPC se divide em duas seções principais: o perfil do cliente e a proposta de valor da empresa. O perfil do cliente ajuda a identificar e mapear os desejos, necessidades, problemas e tarefas dos clientes, enquanto a proposta de valor da empresa descreve como seus produtos ou serviços podem aliviar as dores e gerar ganhos para os clientes.

&emsp;&emsp;No projeto desenvolvido para a Fundação Dom Cabral (FDC), o VPC desempenha um papel crucial ao alinhar a oferta de um serviço de plataforma unificada para CEOs com as necessidades específicas desses profissionais. Através da análise detalhada proporcionada pelo VPC, é possível entender melhor os desafios enfrentados pelos CEOs, como a necessidade de maior integração e eficiência nas suas atividades diárias. A plataforma proposta tem o objetivo de oferecer uma solução que responda diretamente a essas necessidades, facilitando a gestão de projetos e a colaboração entre as empresas associadas.

<div align="center">
  <sub>Figura 5- Value Proposition Canvas</sub>
  <img src="./assets/images/vpc.png" alt="VPC" title="VPC" />
  <sup>Fonte: Os autores (2024)</sup>
</div>

Perfil do Cliente:

- Tarefas do Cliente: Os CEOs buscam escolher projetos para parcerias, entrar em contato com projetos similares e apresentar seus próprios projetos com informações necessárias. A plataforma deverá facilitar essas atividades, agindo como um facilitador de negócios.
- Ganhos: A plataforma promove conexões diretas entre CEOs, fornecendo uma interface intuitiva e organizada. A funcionalidade de recomendação de projetos é um ganho significativo, pois potencializa a identificação de oportunidades de negócios alinhadas aos interesses de cada CEO.
- Dores: Um desafio enfrentado pelos CEOs é a dificuldade em identificar sinergias entre projetos, em encontrar CLevels e de mobilizar mais interações entre os líderes, para serem agentes do progresso. A plataforma precisa abordar essas dores, possibilitando um engajamento mais efetivo entre os líderes empresariais.

Proposta de Valor:

- Produtos e Serviços: A oferta central é uma plataforma de interação entre CEOs, que permite uma concentração de projetos de diferentes categorias e promove o desenvolvimento compartilhado entre projetos e CEOs.
- Criadores de Ganhos: A proposta de valor inclui a apresentação de diversos projetos em uma plataforma unificada, facilitando o desenvolvimento compartilhado entre CEOs e permitindo contato direto e fácil conexão entre eles.
- Aliviadores de Dor: Como remédios para as dores dos clientes, a plataforma oferece um banco de dados completo e simples, um sistema de recomendação de projetos, e a indicação de projetos divididos por categorias, o que ajuda na filtragem e na tomada de decisão rápida e eficiente.

&emsp;&emsp;O VPC serve como um guia para desenvolver um serviço alinhado com as necessidades reais e expectativas dos CEOs, público-alvo da FDC. Ele ajuda a identificar como a plataforma pode ser essencial, facilitando a descoberta de novas oportunidades de negócios e promovendo a colaboração entre líderes empresariais. A ferramenta visual destaca como a proposta de valor atende às dores e ganhos dos CEOs, assegurando que a solução ofereça benefícios tangíveis e relevantes. Ao mapear claramente esses elementos, o VPC orienta o desenvolvimento de um serviço mais eficaz e centrado no cliente. Dessa forma, o VPC garante que a plataforma atenda de maneira precisa às demandas dos usuários finais.

## 3.4 Matriz de Risco

&emsp;&emsp;A matriz de risco é uma ferramenta essencial na gestão de projetos, desempenhando um papel central na avaliação e controle dos riscos. Ela proporciona uma visão abrangente dos possíveis problemas associados ao projeto, facilitando a identificação e priorização dos riscos mais críticos. Ao utilizar a matriz de risco, a equipe de projeto pode categorizar e classificar os riscos com base na sua probabilidade de ocorrência e no impacto potencial que podem causar. Com uma matriz de risco bem definida, a equipe pode desenvolver e implementar medidas preventivas e estratégias corretivas eficazes, minimizando os impactos negativos no projeto. 

&emsp;&emsp;Esta ferramenta também permite uma monitorização contínua dos riscos ao longo do ciclo de vida do projeto, garantindo que novos riscos sejam rapidamente identificados e tratados. Além disso, a matriz de risco promove uma comunicação clara e eficaz sobre os riscos entre todos os membros da equipe, assegurando que todos estejam cientes dos desafios potenciais e das ações necessárias para mitigá-los. A análise detalhada dos riscos permite à equipe planejar respostas adequadas, como planos de ajustes no cronograma do projeto. Assim, a matriz de risco não só ajuda a proteger o projeto contra possíveis ameaças, mas também melhora a resiliência e a capacidade de resposta da equipe frente a imprevistos. Devido à sua importância, abaixo estão descritos alguns dos riscos mapeados e as medidas correspondentes:

<div align="center">
	<sub>Imagem x - Matriz de risco</sub>
	<img src="../docs/assets/images/matriz-de-risco.png" />
</div>

#### Planos de Ação para Ameaças

- **Preferência por produtos concorrentes por parte dos CEOs (como LinkedIn):** É importante destacar os recursos exclusivos e as vantagens competitivas do aplicativo que garantem uma unicidade. Isso pode incluir a personalização, a facilidade de uso, a eficiência na descoberta de projetos ou fortes recomendações de projetos com modelos preditivos.
- **Equipe de desenvolvimento não conseguir cumprir todos os requisitos propostos:** É essencial estabelecer prioridades claras para os requisitos e garantir uma boa comunicação e convivência entre a equipe. Fazer bom uso da metodologia ágil Scrum.
- **Modelo preditivo com baixa acurácia:** Para melhorar a acurácia do modelo preditivo, é importante investir em boas técnicas de modelagem e em uma análise aprofundada dos dados.
- **CEOs não se familiazarem com a proposta da aplicação:** Coletar feedbacks de CEOs para ajustar a proposta de acordo com suas necessidades e preferências em futuras versões da aplicação.
- **Vieses gerados pela baixa assertividade e fidelidade dos dados:** É importante garantir a qualidade dos dados através de técnicas de limpeza e validação de dados. Uma maior diversidade dos dados coletados também pode ajudar a reduzir os vieses.
- **Baixa quantidade de dados para o treinamento do modelo preditivo:** Se a obtenção de dados para o aprendizado da máquina for pequena, para lidar com essa questão, pode-se explorar técnicas como o aumento de dados. Além disso, incentivar os CEOs a usar o aplicativo e a fornecer feedback pode ajudar a coletar mais dados.
- **CEOs terem dificuldade em encontrar projetos para sinergia:** Para facilitar a descoberta de projetos, é importante investir em um design intuitivo, funcionalidades de busca eficientes e recomendações a partir de machine learning.
- **Falhas de comunicação na equipe de desenvolvimento:** Para prevenir falhas de comunicação, é importante promover uma cultura de transparência e utilização de maneiras de comunicação eficazes, como a CNV (comunicação não violenta). Além disso, é essencial a comunicação efetiva sobre o andamento das tarefas e possíveis dificuldades durante as dailys em equipe.

#### Detalhamento das Oportunidades

- **Solução inovadora com uma proposta única no mercado:** A criação de um aplicativo que permite aos CEOs se conectarem, descobrirem projetos e fazerem sinergia entre os mesmos. Sendo assim, uma proposta única que pode preencher uma lacuna no mercado, em relação a falta de ações ESG nas empresas.
- **Requisitos extras para melhorias na experiência do usuário:** A inclusão de funcionalidades adicionais, como a aba de notícias personalizadas, com base nos temas de interesse do CEO, pode melhorar significativamente a experiência do usuário e aumentar a adoção ao aplicativo.
- **Equipe de desenvolvimento cooperativa:** Uma equipe cooperativa e com uma comunicação eficiente, pode levar a um ambiente de trabalho mais harmonioso e a um produto final de alta qualidade e excelente usabilidade.
- **Usabilidade da interface intuitiva:** Uma interface interativa, personalizada e intuitiva pode melhorar a experiência do usuário e aumentar a escolha e acesso ao aplicativo, para cada vez mais CEOs.
- **Alta participação dos CEOs na aplicação, aperfeiçoando as recomendações e o modelo preditivo:** A participação ativa dos CEOs, por meio das interações, como "Favoritar", "Salvar" e "Demonstrar Interesse" sobre os projetos, pode fornecer dados valiosos que serão usados para aprimorar o modelo preditivo e as recomendações do aplicativo.
- **Possibilidade da solução ser um software altamente utilizado por várias empresas:** Se o aplicativo for bem recebido pelos CEOs, ele tem o potencial de ser adotado por várias empresas, aumentando seu impacto e alcance.
- **Equipe de desenvolvimento engajada com o projeto:** Uma equipe engajada pode levar a um aumento na produtividade e a um produto final de alta qualidade.
- **Produto autossuficiente capaz de gerenciar tudo:** O desenvolvimento de um produto autossuficiente, que pode gerenciar todos os aspectos da conexão, descoberta e sinergia de projetos, pode ser um grande diferencial para o aplicativo.

## 3.5 Estimativa de Investimento

&emsp;&emsp;A priori, para o desenvolvimento de um aplicativo móvel que facilita a gestão de sinergias entre projetos de CEOs, o `Coffee Break`, é crucial realizar um planejamento financeiro detalhado. Este planejamento inclui uma análise precisa dos custos associados à equipe de desenvolvimento e infraestrutura necessária. Utilizando dados de fontes como [Glassdoor](https://www.glassdoor.com.br/index.htm) e [Payscale](https://www.payscale.com/), foi necessário que a equipe ajustasse os salários médios para refletir o mercado de trabalho em Tecnologia no Brasil, considerando as especificidades do projeto e a realidade econômica local.

### Detalhamento dos Custos de Pessoal

&emsp;&emsp;Destarte, a equipe proposta para o desenvolvimento do aplicativo consiste em quatro posições, todas ocupadas meio período para otimizar recursos e adequar-se ao escopo do projeto:

1. **Designer** (meio período)
   Salário médio mensal: R$ 4.000,00
   Custo Anual: (R$ 4.000,00 / 2) x 12 = R$ 24.000,00
2. **Desenvolvedor Mobile Fullstack** (meio período)
   Salário médio mensal: R$ 8.000,00
   Custo Anual: (R$ 8.000,00 / 2) x 12 = R$ 48.000,00
3. **Cientista de Dados Jr.** (meio período)
   Salário médio mensal: R$ 4.000,00
   Custo Anual: (R$ 4.000,00 / 2) x 12 = R$ 24.000,00
4. **Tech Lead Jr.** (meio período)
   Salário médio mensal: R$ 10.000,00
   Custo Anual: (R$ 10.000,00 / 2) x 12 = R$ 60.000,00

&emsp;&emsp;**Total de Custos de Pessoal sem Markup**: R$ 156.000,00

&emsp;&emsp;**Total de Custos de Pessoal com Markup de 20%**: R$ 187.200,00

### Custos de Infraestrutura

&emsp;&emsp;A infraestrutura necessária para o projeto inclui software, hardware e serviços em nuvem:

1. **Software e colaboração**: Estimado em R$ 5.000,00 anuais
2. **Serviços em nuvem**: Considerando o [plano gratuito da AWS EC2](https://aws.amazon.com/pt/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=*all&awsf.Free%20Tier%20Categories=*all), é possível assumir que os custos adicionais de nuvem são mínimos, estimados em R$ 3.000,00 para o ano para cobrir qualquer uso que exceda o plano gratuito.

&emsp;&emsp;**Total de Custos de Infraestrutura sem Markup**: R$ 8.000,00

&emsp;&emsp;**Total de Custos de Infraestrutura com Markup**: R$ 8.800,00

### Análise Trivariada de Custos

&emsp;&emsp;A análise trivariada ajuda a entender o impacto potencial de variações nos custos, proporcionando uma visão desde o cenário mais otimista ao mais pessimista. Consideramos três cenários:

- **Cenário Otimista:**

  - Redução de 10% nos salários e manutenção dos custos de infraestrutura.
  - Custos de Pessoal: R$ 168.480,00
  - Custos de Infraestrutura: R$ 7.920,00
  - **Total**: R$ 176.400,00

- **Cenário Mais Provável:**

  - Manutenção dos custos conforme planejado.
  - Custos de Pessoal: R$ 187.200,00
  - Custos de Infraestrutura: R$ 8.800,00
  - **Total**: R$ 196.000,00

- **Cenário Pessimista:**
  - Aumento de 10% nos salários e um aumento nos custos de serviços em nuvem para cobrir excedentes.
  - Custos de Pessoal: R$ 205.920,00
  - Custos de Infraestrutura: R$ 10.560,00
  - Total: R$ 216.480,00

&emsp;&emsp;O planejamento financeiro detalhado para o desenvolvimento do `Coffee Break` demonstra que os custos variam de **R$ 176.400,00** no cenário mais otimista a **R$ 216.480,00** no cenário mais pessimista. Esta análise trivariada permite aos stakeholders do projeto prepararem-se para variações no mercado e garante que o projeto seja realizado dentro de um orçamento controlado. A escolha cuidadosa de recursos e a decisão de empregar profissionais em meio período são estratégias fundamentais para manter o projeto econômico sem sacrificar a qualidade ou a capacidade de escalabilidade futura.

# 4. Análise dos processos

&emsp;&emsp;A análise de processos de negócio é essencial para organizações que buscam eficiência operacional e sucesso estratégico. Ela permite identificar oportunidades de melhoria, otimizar fluxos de trabalho e alinhar atividades ao propósito organizacional, resultando em melhor desempenho e alcance de metas [referencia_workfellow]. Nesta seção, detalhamos a cadeia de valor e a modelagem de processos BPMN, fornecendo ferramentas para entender e aprimorar o processo de 'Gestão de Sinergias' no CEOs’ Legacy, operado pela Fundação Dom Cabral. Isso envolve uma análise minuciosa dos componentes do processo, identificação de pontos críticos e implementação de melhorias que facilitam a colaboração e a sinergia entre as empresas participantes.

## 4.1 Cadeia de Valor

&emsp;&emsp;A cadeia de valor é um modelo conceitual que descreve as atividades sequenciais realizadas por uma organização para criar valor para seus clientes e demais partes interessadas. Essas atividades são divididas em processos de apoio e processos principais, ambos essenciais para alcançar os objetivos estratégicos da organização. Os processos de apoio proporcionam os recursos e infraestruturas necessários, enquanto os processos principais diretamente produzem e entregam os produtos ou serviços que atendem às necessidades dos clientes.

### Processos de Apoio

&emsp;&emsp;Processos de apoio são essenciais para a sustentação das operações organizacionais. Eles incluem:

- **Gerenciamento de Recursos Humanos:** Foco na captação e desenvolvimento de talentos.
- **Desenvolvimento Tecnológico:** Inovação e manutenção de plataformas digitais.
- **Coordenação Administrativa e Financeira:** Gerenciamento de recursos e investimentos.
- **Suporte Jurídico e Compliance:** Assegura a conformidade legal das atividades.

### Processos Principais

&emsp;&emsp;Os processos principais estão diretamente relacionados à entrega de valor e incluem:

- **Identificação de Oportunidades:** Análise de mercado para alinhamento com o propósito organizacional.
- **Evolução de Projetos:** Incentivo ao desenvolvimento dos projetos apresentados.
- **Gestão de CEOs:** Acompanhamento e desenvolvimento pessoal.
- **Gestão de Sinergias:** Facilitação de colaborações estratégicas.

&emsp;&emsp;Esses processos culminam na **Contribuição Comunitária**, que representa o impacto final da organização na comunidade, abrangendo a disseminação de conhecimento e a partilha de insights e melhores práticas.

<div align="center">
    <sub>Figura 6 - Cadeia de Valor do CEO's Legacy</sub>
    <img src="./assets/images/cadeia-de-valor.jpg" alt="Cadeia de Valor" border="0">
    <sup>Fonte: Os autores (2024)</sup>
</div>

&emsp;&emsp;Assim, a cadeia de valor é fundamental para oferecer uma perspectiva clara sobre as contribuições de cada processo na missão da organização. Ela permite uma visão integrada das atividades, destacando como cada etapa agrega valor e apoia os objetivos estratégicos. Com essa visão, a organização pode identificar áreas de melhoria, otimizar recursos e assegurar que todos os processos estejam alinhados com sua missão e metas. Além disso, a cadeia de valor facilita a comunicação e o entendimento entre diferentes departamentos, promovendo uma colaboração mais eficaz. Isso resulta em uma maior coesão organizacional e no fortalecimento da capacidade da empresa de alcançar resultados sustentáveis e de longo prazo.


## 4.2 Modelagem de Processos

&emsp;&emsp;Modelar processos usando BPMN oferece uma representação visual e estruturada dos processos organizacionais. Destarte, foi selecionado o processo de 'Gestão de Sinergias' do CEOs Legacy para demonstrar essa técnica e sua aplicabilidade prática [referencia_integrify]. O diagrama BPMN apresentado na Figura X captura a complexidade e as nuances do processo de 'Gestão de Sinergias'. Ele inicia com a criação do projeto, passando pela identificação de macrotemas e visualização de projetos recomendados, até a avaliação da apresentação de interesse. Cada etapa é crucial e interconectada, refletindo a decisão de seguir adiante com a sinergia ou não, dependendo do interesse e tipo de sinergia identificada – aprendizado, integração ou unificação.

&emsp;&emsp;As diversas rotas de decisão e ações subsequentes delineadas no diagrama destacam o envio de solicitação de sinergia, avaliação da solicitação, e o estabelecimento e acompanhamento da sinergia, ilustrando a atenção da organização em fomentar interações valiosas e estratégicas entre os CEOs. Este mapeamento é essencial para garantir a gestão efetiva das sinergias, que é central para a missão do CEOs Legacy de promover projetos transformadores e desenvolvimento de lideranças. Segue abaixo o diagrama BPMN para Gestão de Sinergias.

<div align="center">
    <sub>Figura 7 - Diagrama BPMN para Gestão de Sinergias</sub>
    <img src="./assets/images/bpmn.png" alt="Diagrama BPMN" border="0">
    <sup>Fonte: Os autores (2024)</sup>
</div>

&emsp;&emsp;A modelagem BPMN serve como um guia fundamental para a execução eficiente dos processos. As notações padronizadas do BPMN permitem uma análise detalhada e transparente dos passos operacionais, garantindo que todas as etapas do processo sejam compreendidas de forma clara e precisa. Isso não apenas ajuda a identificar e resolver possíveis problemas rapidamente, mas também assegura que a organização possa atingir seus objetivos de maneira eficaz e eficiente. Resumidamente, a modelagem BPMN promove a consistência e a padronização nas operações, permitindo que todos os membros da equipe estejam alinhados e informados sobre os procedimentos e expectativas, contribuindo para a melhoria contínua e o sucesso estratégico da organização.

# 5. Requisitos

&emsp;&emsp;De início, conforme descrito por Ian Sommerville (2016), **requisitos são descrições de serviços que o sistema deve fornecer e das restrições sob as quais ele deve operar**. Os requisitos funcionais descrevem as funcionalidades ou serviços que o sistema deve fornecer. Os requisitos não funcionais são restrições sobre os serviços ou funções oferecidos pelo sistema. Sendo assim, faz-se necessário a descrição dos requisitos funcionais e não funcionais da aplicação a ser desenvolvida neste projeto.

## 5.1 Requisitos Funcionais

&emsp;&emsp;Requisitos funcionais são especificações que descrevem as funções e operações que um sistema, software ou produto deve realizar. Eles definem o comportamento do sistema e as interações que ele deve ter com seus usuários, outros sistemas ou com o ambiente em que está inserido. Esses requisitos descrevem o que o sistema deve fazer em termos de entrada, processamento e saída de dados.

&emsp;&emsp;Os requisitos funcionais são essenciais para guiar o desenvolvimento de um sistema e são frequentemente documentados durante a fase de análise de requisitos de um projeto de desenvolvimento de software. Eles são contrastados com os requisitos não funcionais, que se concentram em atributos de qualidade do sistema, como desempenho, segurança e usabilidade.

&emsp;&emsp;A seguir, são listados os principais requisitos funcionais da plataforma `Coffee break`:

### **Usuários**

### RF-001

**Cadastro de CEOs via Admin**

A aplicação deve suportar que os usuários com permissão administrativa possam cadastrar novos CEOs na plataforma.

#### Critérios de Aceitação

1. O usuário deve estar em um perfil de administrador.
2. O CEO não deve ter um cadastro já existente na plataforma.
3. A aplicação deve possuir um formulário de cadastro exclusivo para CEOs.

#### Descrição dos Testes

<div align="center">
   <sub>Quadro 1 - Descrição dos casos de teste do RF-001</sub>

| Nome                       | Pré-condição                                               | Procedimentos                                                                                                                                                                        | Resultado Esperado                            | Pós-condição                                                                |
| -------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------- | --------------------------------------------------------------------------- |
| Cadastro CEO bem sucedido. | O usuário deve estar logado com o perfil de administrador. | O usuário deve estar logado com o perfil de administrador; clicar o botão de cadastro de CEOs; preencher as informções; o sistema avaliar a existência daquele perfil na plataforma. | O perfil do CEO deve ser criado na plataforma | O CEO responsável por aquele perfil deve ser capaz de acessar a plataforma. |

<sup>Fonte: Os autores (2024)</sup>

</div>

### RF-002

**Edição do perfil do CEO**

A aplicação deve permitir que um usuário com perfil de administrador edite um perfil de CEO.

#### Critérios de Aceitação

1. O usuário deve estar em um perfil de administrador.
2. O CEO deve existir na plataforma.
3. A opção de edição deve estar habilitada na plataforma.

#### Descrição dos Testes

<div align="center">
   <sub>Quadro 2 - Descrição dos casos de teste do RF-002</sub>

| Nome                        | Pré-condição                                                                                           | Procedimentos                                                                                                                  | Resultado Esperado                                                                  | Pós-condição                                                |
| --------------------------- | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| Edição de um perfil de CEO. | O usuário deve estar logado com o perfil de administrador; o perfil do CEO deve existir na plataforma. | O usuário deve estar logado com o perfil de administrador; clicar no botão de editar perfil de um CEO existente na plataforma. | O usuário de perfil administrativo deve conseguir editar o perfil do CEO existente. | As edições feitas no perfil do CEO devem permanecer salvas. |

<sup>Fonte: Os autores (2024)</sup>

</div>

### RF-003

**Login no aplicativo**

A aplicação deve permitir que o usuário acesse a plataforma utilizando suas credenciais correspondentes ao seu perfil.

#### Critérios de Aceitação

1. O usuário deve possuir um perfil válido na plataforma.
2. As credenciais fornecidas pelo usuário devem ser autenticadas com sucesso.
3. O acesso deve ser concedido apenas se as credenciais e o perfil do usuário estiverem corretos.

#### Descrição dos Testes

<div align="center">
   <sub>Quadro 3 - Descrição dos casos de teste do RF-003</sub>

| Nome                 | Pré-condição                                                                 | Procedimentos                                                                                                      | Resultado Esperado                                                                   | Pós-condição                                                                  |
| -------------------- | ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------- |
| Acesso à Plataforma. | O usuário deve ter credenciais válidas e um perfil registrado na plataforma. | 1. Abrir o aplicativo. 2. Inserir as credenciais (nome de usuário e senha). 3. Selecionar o perfil correspondente. | O usuário é autenticado com sucesso e acessa a plataforma com seu respectivo perfil. | O usuário tem acesso às funcionalidades disponíveis de acordo com seu perfil. |

<sup>Fonte: Os autores (2024)</sup>

</div>

### RF-004

**Inativação/Ativação de Usuários via Admin**

A aplicação deve permitir que um usuário com perfil de administrador inative ou ative contas de usuário na plataforma.

#### Critérios de Aceitação

1. O usuário deve possuir um perfil de administrador.
2. A conta de usuário a ser inativada ou ativada deve existir na plataforma.
3. Deve haver uma opção disponível para inativação/ativação de contas de usuário.

#### Descrição dos Testes

<div align="center">
   <sub>Quadro 4 - Descrição dos casos de teste do RF-004</sub>

| Nome                           | Pré-condição                                                                                                                    | Procedimentos                                                                                                                                                  | Resultado Esperado                                                                         | Pós-condição                                                |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | ----------------------------------------------------------- |
| Inativação de Conta de Usuário | O usuário deve estar logado com um perfil de administrador e a conta de usuário a ser inativada deve estar ativa na plataforma. | 1. Logar na aplicação com um perfil de administrador. 2. Localizar a conta de usuário a ser inativada. 3. Selecionar a opção para inativar a conta do usuário. | A conta de usuário é inativada com sucesso e o usuário não pode mais acessar a plataforma. | A conta do usuário está marcada como inativa na plataforma. |
| Ativação de Conta de Usuário   | O usuário deve estar logado com um perfil de administrador e a conta de usuário a ser ativada deve estar inativa na plataforma. | 1. Logar na aplicação com um perfil de administrador. 2. Localizar a conta de usuário a ser ativada. 3. Selecionar a opção para ativar a conta do usuário.     | A conta de usuário é ativada com sucesso e o usuário pode acessar a plataforma novamente.  | A conta do usuário está marcada como ativa na plataforma.   |

<sup>Fonte: Os autores (2024)</sup>

</div>

### RF-005

**Visualização de Perfis de Forma Global**

A aplicação deve permitir que um usuário com perfil de administrador visualize todos os perfis de usuário de forma global na plataforma.

#### Critérios de Aceitação

1. O usuário deve possuir um perfil.
2. Todos os perfis de usuário devem ser acessíveis para visualização.
3. Deve haver uma opção disponível para acessar a visualização dos perfis de usuário.

#### Descrição dos Testes

<div align="center">
   <sub>Quadro 5 - Descrição dos casos de teste do RF-005</sub>

| Nome                          | Pré-condição                                                | Procedimentos                                                                                                           | Resultado Esperado                                                                  | Pós-condição                                                      |
| ----------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| Visualização Global de Perfis | O usuário deve estar logado com um perfil de administrador. | 1. Logar na aplicação com um perfil de administrador. 2. Selecionar a opção para visualizar todos os perfis de usuário. | O usuário pode visualizar todos os perfis de usuário de forma global na plataforma. | O usuário tem acesso à visualização global dos perfis de usuário. |

<sup>Fonte: Os autores (2024)</sup>

</div>

### **Projeto**

### RF-006

**Cadastro de Projetos**

A aplicação deve permitir que um usuário com perfil de administrador ou gerente cadastre novos projetos na plataforma.

#### Critérios de Aceitação

1. O usuário deve possuir um perfil de CEO.
2. Deve haver campos disponíveis para inserir informações relevantes do projeto, como título, descrição, data de início, data de término, entre outros.
3. Após o cadastro, o projeto deve ficar disponível para visualização e edição por usuários autorizados.

#### Descrição dos Testes

<div align="center">
   <sub>Quadro 6 - Descrição dos casos de teste do RF-006</sub>

| Nome                     | Pré-condição                                                           | Procedimentos                                                                                                                                                                             | Resultado Esperado                                | Pós-condição                                                                   |
| ------------------------ | ---------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------------------------------------ |
| Cadastro de Novo Projeto | O usuário deve estar logado com um perfil de administrador ou gerente. | 1. Logar na aplicação com um perfil de administrador ou gerente. 2. Selecionar a opção para cadastrar um novo projeto. 3. Preencher os campos obrigatórios com as informações do projeto. | O projeto é cadastrado com sucesso na plataforma. | O projeto fica disponível para visualização e edição por usuários autorizados. |

|
<sup>Fonte: Os autores (2024)</sup>

</div>

### RF-007

**Edição de Projeto**

A aplicação deve permitir que um usuário com perfil de administrador ou gerente edite informações de um projeto existente na plataforma.

#### Critérios de Aceitação

1. O usuário deve possuir um perfil de CEO.
2. Deve haver uma opção disponível para edição de projetos.
3. As informações do projeto, como título, descrição, datas de início e término, entre outras, devem ser editáveis.
4. As alterações feitas devem ser salvas corretamente na plataforma.

#### Descrição dos Testes

<div align="center">
   <sub>Quadro 7 - Descrição dos casos de teste do RF-007</sub>

| Nome                        | Pré-condição                                                                                                                | Procedimentos                                                                                                                                                           | Resultado Esperado                                                     | Pós-condição                                              |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | --------------------------------------------------------- |
| Edição de Projeto Existente | O usuário deve estar logado com um perfil de administrador ou gerente e o projeto a ser editado deve existir na plataforma. | 1. Logar na aplicação com um perfil de administrador ou gerente. 2. Selecionar o projeto que deseja editar. 3. Realizar as alterações necessárias nos campos editáveis. | As alterações feitas no projeto são salvas corretamente na plataforma. | O projeto é atualizado com as novas informações editadas. |

|
<sup>Fonte: Os autores (2024)</sup>

</div>

### RF-008

**Inativação/Ativação de projetos**

A aplicação deve permitir que um usuário com perfil de administrador ou CEO inative ou ative projetos na plataforma.

#### Critérios de Aceitação

1. O usuário deve possuir um perfil de administrador ou gerente.
2. Deve haver uma opção disponível para inativação/ativação de projetos.
3. Os projetos podem ser marcados como ativos ou inativos.
4. Projetos inativos não devem ser acessíveis ou editáveis por usuários.

#### Descrição dos Testes

<div align="center">
   <sub>Quadro 8 - Descrição dos casos de teste do RF-008</sub>

| Nome                  | Pré-condição                                                                                                                      | Procedimentos                                                                                                                                              | Resultado Esperado                                                                                 | Pós-condição                                       |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| Inativação de Projeto | O usuário deve estar logado com um perfil de administrador ou gerente e o projeto a ser inativado deve estar ativo na plataforma. | 1. Logar na aplicação com um perfil de administrador ou gerente. 2. Selecionar o projeto que deseja inativar. 3. Escolher a opção para inativar o projeto. | O projeto é marcado como inativo na plataforma e não está mais acessível ou editável por usuários. | O projeto está marcado como inativo na plataforma. |

|
|Ativação de Projeto | O usuário deve estar logado com um perfil de administrador ou gerente e o projeto a ser ativado deve estar inativo na plataforma. | 1. Logar na aplicação com um perfil de administrador ou gerente. 2. Selecionar o projeto que deseja ativar. 3. Escolher a opção para ativar o projeto. | O projeto é marcado como ativo na plataforma e está acessível e editável novamente por usuários. |O projeto está marcado como ativo na plataforma.

|
<sup>Fonte: Os autores (2024)</sup>

</div>

### RF-009

**Possibilidade de Curtir um Projeto**

A aplicação deve permitir que um usuário com perfil de CEO possa "curtir" um projeto na plataforma.

#### Critérios de Aceitação

1. O usuário deve possuir um perfil de CEO.
2. Deve haver uma opção disponível para "curtir" um projeto.
3. Cada usuário só pode "curtir" um projeto uma vez.
4. A ação de "curtir" deve ser registrada e visível para outros usuários.

#### Descrição dos Testes

<div align="center">
   <sub>Quadro 9 - Descrição dos casos de teste do RF-009</sub>

| Nome              | Pré-condição                                      | Procedimentos                                                                                                                       | Resultado Esperado                                               | Pós-condição                                                                     |
| ----------------- | ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| Curtir um Projeto | O usuário deve estar logado com um perfil de CEO. | 1. Logar na aplicação com um perfil de CEO. 2. Selecionar o projeto que deseja curtir. 3. Escolher a opção para "curtir" o projeto. | O usuário "curte" o projeto e a ação é registrada na plataforma. | A ação de "curtir" é registrada para o projeto e é visível para outros usuários. |

|
<sup>Fonte: Os autores (2024)</sup>

</div>

### RF-010

**Possibilidade de Demonstrar Interesse em um Projeto (Detalhamento do Projeto)**

A aplicação deve permitir que os usuários demonstrem interesse em um projeto específico apenas quando estiverem visualizando os detalhes desse projeto na plataforma.

#### Critérios de Aceitação

1. A funcionalidade de demonstrar interesse em um projeto estará disponível apenas na visualização detalhada do projeto.
2. Cada usuário poderá demonstrar interesse em um projeto apenas uma vez.
3. A ação de demonstrar interesse será registrada e visível para outros usuários.

#### Descrição dos Testes

<div align="center">
   <sub>Quadro 10 - Descrição dos casos de teste do RF-010</sub>

| Nome                                    | Pré-condição                                                               | Procedimentos                                                                                            | Resultado Esperado                                                            | Pós-condição                                                                                 |
| --------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| Demonstração de Interesse em um Projeto | O usuário deve estar visualizando os detalhes de um projeto na plataforma. | 1. Abrir a página de detalhes de um projeto. 2. Selecionar a opção para demonstrar interesse no projeto. | O usuário demonstra interesse no projeto e a ação é registrada na plataforma. | A ação de demonstrar interesse é registrada para o projeto e é visível para outros usuários. |

|
<sup>Fonte: Os autores (2024)</sup>

</div>

### RF-011

**Possibilidade de salvar um projeto como favorito**

A aplicação deve permitir que os usuários salvem projetos como favoritos para fácil acesso posterior.

#### Critérios de Aceitação

1. Deve haver uma opção disponível para salvar um projeto como favorito.
2. Cada usuário pode salvar múltiplos projetos como favoritos.
3. Os projetos salvos como favoritos devem estar facilmente acessíveis na interface do usuário.
4. Os projetos salvos como favoritos devem permanecer como favoritos mesmo após o usuário sair da sessão.

#### Descrição dos Testes

<div align="center">
   <sub>Quadro 11 - Descrição dos casos de teste do RF-011</sub>

| Nome                         | Pré-condição                                                               | Procedimentos                                                                                           | Resultado Esperado                                                                       | Pós-condição                                                                                              |
| ---------------------------- | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| Salvar Projeto como Favorito | O usuário deve estar visualizando os detalhes de um projeto na plataforma. | 1. Abrir a página de detalhes de um projeto. 2. Selecionar a opção para salvar o projeto como favorito. | OO projeto é salvo como favorito para o usuário e está disponível na lista de favoritos. | O projeto está marcado como favorito para o usuário e pode ser facilmente acessado na lista de favoritos. |

<sup>Fonte: Os autores (2024)</sup>

</div>

### RF-012

**Envio de notificação ao criador do projeto sobre a demonstração de interesse**

A aplicação deve enviar uma notificação ao criador do projeto sempre que um usuário demonstrar interesse em seu projeto.

#### Critérios de Aceitação

1. Quando um usuário demonstrar interesse em um projeto, o criador do projeto deve ser notificado.
2. A notificação deve conter informações relevantes, como o nome do usuário interessado e detalhes do projeto.
3. O criador do projeto deve receber a notificação em tempo real ou em um intervalo de tempo curto.

#### Descrição dos Testes

<div align="center">
   <sub>Quadro 12 - Descrição dos casos de teste do RF-012</sub>

| Nome                                       | Pré-condição                                                | Procedimentos                                                                    | Resultado Esperado                                                                                              | Pós-condição                                                                        |
| ------------------------------------------ | ----------------------------------------------------------- | -------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| Envio de Notificação ao Criador do Projeto | Um usuário demonstra interesse em um projeto na plataforma. | O usuário demonstra interesse em um projeto selecionando a opção correspondente. | O criador do projeto recebe uma notificação sobre a demonstração de interesse, contendo informações relevantes. | O criador do projeto é notificado sobre a demonstração de interesse em seu projeto. |

<sup>Fonte: Os autores (2024)</sup>

</div>

### RF-013

**Listagem de Notificações sobre Demonstração de Interesse**

A aplicação deve fornecer uma lista de notificações para os criadores de projeto, onde podem visualizar as demonstrações de interesse recebidas em seus projetos.

#### Critérios de Aceitação

1. Os criadores de projeto devem ter acesso a uma lista de notificações sobre demonstração de interesse recebidas em seus projetos.
2. Cada notificação deve conter informações relevantes, como o nome do usuário interessado e detalhes do projeto.
3. As notificações devem ser apresentadas de forma clara e organizada para fácil visualização.

#### Descrição dos Testes

<div align="center">
   <sub>Quadro 13 - Descrição dos casos de teste do RF-013</sub>

| Nome                                                     | Pré-condição                                                      | Procedimentos                                                                                                                        | Resultado Esperado                                                                                                               | Pós-condição                                                                             |
| -------------------------------------------------------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| Listagem de Notificações sobre Demonstração de Interesse | O criador do projeto acessa a área de notificações na plataforma. | 1. Acessar a área de notificações. 2. Visualizar a lista de notificações sobre demonstração de interesse recebidas em seus projetos. | O criador do projeto pode visualizar de forma clara e organizada todas as demonstrações de interesse recebidas em seus projetos. | O criador do projeto tem acesso à lista de notificações sobre demonstração de interesse. |

<sup>Fonte: Os autores (2024)</sup>

</div>

### RF-014

**Aceitar/Recusar Demonstração de Interesse**

A aplicação deve permitir que os criadores de projeto aceitem ou recusem as demonstrações de interesse recebidas em seus projetos.

#### Critérios de Aceitação

1. Os criadores de projeto devem ter a opção de aceitar ou recusar demonstrações de interesse recebidas em seus projetos.
2. Para cada demonstração de interesse recebida, deve haver uma opção clara para aceitar ou recusar.
3. Após a decisão, o usuário interessado deve ser notificado sobre o resultado.

#### Descrição dos Testes

<div align="center">
   <sub>Quadro 14 - Descrição dos casos de teste do RF-014</sub>

| Nome                              | Pré-condição                                                                                                  | Procedimentos                                                                                                       | Resultado Esperado                                                                                              | Pós-condição                                                                          |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| Aceitar Demonstração de Interesse | O criador do projeto acessa a lista de notificações sobre demonstração de interesse recebidas em seu projeto. | 1. Visualizar a lista de notificações. 2. Selecionar a opção para aceitar uma demonstração de interesse específica. | O criador do projeto aceita a demonstração de interesse e o usuário interessado é notificado sobre o resultado. | O usuário interessado é notificado de que sua demonstração de interesse foi aceita.   |
| Recusar Demonstração de Interesse | O criador do projeto acessa a lista de notificações sobre demonstração de interesse recebidas em seu projeto. | 1. Visualizar a lista de notificações. 2. Selecionar a opção para recusar uma demonstração de interesse específica. | O criador do projeto recusa a demonstração de interesse e o usuário interessado é notificado sobre o resultado. | O usuário interessado é notificado de que sua demonstração de interesse foi recusada. |

<sup>Fonte: Os autores (2024)</sup>

</div>

### RF-015

**Listagem dos Projetos Autorais**

A aplicação deve fornecer uma lista de projetos autorais para os usuários, onde eles possam visualizar todos os projetos que criaram na plataforma.

#### Critérios de Aceitação

1. Os usuários devem ter acesso a uma lista de projetos autorais que criaram na plataforma.
2. Cada projeto listado deve conter informações relevantes, como título, descrição, data de criação, entre outros.
3. Os projetos devem ser apresentados de forma clara e organizada para fácil visualização.

#### Descrição dos Testes

<div align="center">
   <sub>Quadro 15 - Descrição dos casos de teste do RF-015</sub>

| Nome                           | Pré-condição                              | Procedimentos                                                                                                | Resultado Esperado                                                                               | Pós-condição                                                          |
| ------------------------------ | ----------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------- |
| Listagem dos Projetos Autorais | O usuário acessa sua conta na plataforma. | 1. Acessar a área de projetos autorais na plataforma. 2. Visualizar a lista de projetos que o usuário criou. | O usuário pode visualizar de forma clara e organizada todos os projetos que criou na plataforma. | O usuário tem acesso à lista de seus projetos autorais na plataforma. |

<sup>Fonte: Os autores (2024)</sup>

</div>

### RF-016

**Listagem dos projetos recomendados**

A aplicação deve fornecer uma lista de projetos recomendados para os usuários, baseada em seus interesses e interações na plataforma.

#### Critérios de Aceitação

1. Os usuários devem ter acesso a uma lista de projetos recomendados na plataforma.
2. A lista de projetos recomendados deve ser personalizada para cada usuário, levando em consideração seus interesses e interações anteriores na plataforma.
3. Os projetos recomendados devem ser apresentados de forma clara e organizada para fácil visualização.

#### Descrição dos Testes

<div align="center">
   <sub>Quadro 16 - Descrição dos casos de teste do RF-016</sub>

| Nome                               | Pré-condição                              | Procedimentos                                                                                                                                                 | Resultado Esperado                                                                                           | Pós-condição                                                                                                         |
| ---------------------------------- | ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------- |
| Listagem dos Projetos Recomendados | O usuário acessa sua conta na plataforma. | 1. Acessar a área de projetos recomendados na plataforma. 2. Visualizar a lista de projetos recomendados com base em seus interesses e interações anteriores. | O usuário pode visualizar de forma clara e organizada todos os projetos recomendados para ele na plataforma. | O usuário tem acesso à lista de projetos recomendados personalizada para seus interesses e interações na plataforma. |

<sup>Fonte: Os autores (2024)</sup>

</div>

### RF-017

**Listagem de todos os projetos com filtros (macrotema, subtema, palavras-chave, etc)**

A aplicação deve permitir que os usuários visualizem todos os projetos disponíveis na plataforma com a opção de aplicar filtros, como macrotema, subtema, palavras-chave, etc.

#### Critérios de Aceitação

1. Os usuários devem ter acesso a uma lista de todos os projetos disponíveis na plataforma.
2. Deve haver opções de filtro disponíveis, como macrotema, subtema, palavras-chave, entre outros.
3. Os filtros aplicados devem retornar resultados relevantes e atualizados de acordo com as seleções do usuário.
4. Os projetos devem ser apresentados de forma clara e organizada para fácil visualização.

#### Descrição dos Testes

<div align="center">
   <sub>Quadro 17 - Descrição dos casos de teste do RF-017</sub>

| Nome                             | Pré-condição                                                     | Procedimentos                                                                                                                                               | Resultado Esperado                                                                                                                    | Pós-condição                                                                                      |
| -------------------------------- | ---------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| Listagem de Projetos com Filtros | O usuário acessa a página de listagem de projetos na plataforma. | 1. Aplicar os filtros desejados, como macrotema, subtema, palavras-chave, etc. 2. Visualizar os resultados dos projetos de acordo com os filtros aplicados. | O usuário pode visualizar de forma clara e organizada todos os projetos disponíveis na plataforma de acordo com os filtros aplicados. | O usuário tem acesso à lista de projetos filtrados de acordo com suas preferências na plataforma. |

<sup>Fonte: Os autores (2024)</sup>

</div>

### RF-018

**Listagem de Projetos Curtidos**

A aplicação deve fornecer uma lista dos projetos que o usuário curtiu na plataforma.

#### Critérios de Aceitação

1. s usuários devem ter acesso a uma lista dos projetos que eles curtiram na plataforma.
2. A lista deve apresentar os projetos de forma clara e organizada para fácil visualização.
3. Os projetos curtidos devem ser atualizados automaticamente à medida que o usuário curte ou descurte projetos.

#### Descrição dos Testes

<div align="center">
   <sub>Quadro 18 - Descrição dos casos de teste do RF-018</sub>

| Nome                          | Pré-condição                              | Procedimentos                                                                                                 | Resultado Esperado                                                                                | Pós-condição                                                          |
| ----------------------------- | ----------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| Listagem de Projetos Curtidos | O usuário acessa sua conta na plataforma. | 1. Acessar a área de projetos curtidos na plataforma. 2. Visualizar a lista de projetos que o usuário curtiu. | O usuário pode visualizar de forma clara e organizada todos os projetos que curtiu na plataforma. | O usuário tem acesso à lista de seus projetos curtidos na plataforma. |

<sup>Fonte: Os autores (2024)</sup>

</div>

### RF-019

**Listagem de projetos com demonstração de interesse**

A aplicação deve fornecer uma lista dos projetos em que o usuário demonstrou interesse na plataforma.

#### Critérios de Aceitação

1. Os usuários devem ter acesso a uma lista dos projetos em que demonstraram interesse na plataforma.
2. A lista deve apresentar os projetos de forma clara e organizada para fácil visualização.
3. Os projetos com demonstração de interesse devem ser atualizados automaticamente à medida que o usuário demonstra ou remove interesse em projetos.

#### Descrição dos Testes

<div align="center">
   <sub>Quadro 19 - Descrição dos casos de teste do RF-019</sub>

| Nome                                               | Pré-condição                              | Procedimentos                                                                                                                                       | Resultado Esperado                                                                                                 | Pós-condição                                                                        |
| -------------------------------------------------- | ----------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------- |
| Listagem de Projetos com Demonstração de Interesse | O usuário acessa sua conta na plataforma. | 1. Acessar a área de projetos com demonstração de interesse na plataforma. 2. Visualizar a lista de projetos em que o usuário demonstrou interesse. | O usuário pode visualizar de forma clara e organizada todos os projetos em que demonstrou interesse na plataforma. | O usuário tem acesso à lista de projetos em que demonstrou interesse na plataforma. |

<sup>Fonte: Os autores (2024)</sup>

</div>

### RF-020

**Listagem de projetos salvos**

A aplicação deve fornecer uma lista dos projetos que o usuário salvou como favoritos na plataforma.

#### Critérios de Aceitação

1. Os usuários devem ter acesso a uma lista dos projetos que salvaram como favoritos na plataforma.
2. A lista deve apresentar os projetos de forma clara e organizada para fácil visualização.
3. Os projetos salvos como favoritos devem ser atualizados automaticamente à medida que o usuário salva ou remove projetos como favoritos.

#### Descrição dos Testes

<div align="center">
   <sub>Quadro 20 - Descrição dos casos de teste do RF-020</sub>

| Nome                        | Pré-condição                              | Procedimentos                                                                                                                             | Resultado Esperado                                                                                               | Pós-condição                                                                       |
| --------------------------- | ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Listagem de Projetos Salvos | O usuário acessa sua conta na plataforma. | 1. Acessar a área de projetos salvos como favoritos na plataforma. 2. Visualizar a lista de projetos que o usuário salvou como favoritos. | O usuário pode visualizar de forma clara e organizada todos os projetos que salvou como favoritos na plataforma. | O usuário tem acesso à lista de seus projetos salvos como favoritos na plataforma. |

<sup>Fonte: Os autores (2024)</sup>

</div>

### RF-021

**Listagem de projetos sinérgicos**

A aplicação deve fornecer uma lista de projetos sinérgicos para os usuários, ou seja, projetos que possuem alguma relação ou afinidade com os projetos visualizados pelo usuário.

#### Critérios de Aceitação

1. Os usuários devem ter acesso a uma lista de projetos sinérgicos na plataforma.
2. A lista de projetos sinérgicos deve ser baseada nos projetos visualizados pelo usuário e suas características.
3. Os projetos sinérgicos devem ser apresentados de forma clara e organizada para fácil visualização.

#### Descrição dos Testes

<div align="center">
   <sub>Quadro 21 - Descrição dos casos de teste do RF-021</sub>

| Nome                            | Pré-condição                                  | Procedimentos                                                                                                                                                             | Resultado Esperado                                                                                                      | Pós-condição                                                       |
| ------------------------------- | --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| Listagem de Projetos Sinérgicos | O usuário visualiza um projeto na plataforma. | 1. Acessar a área de projetos sinérgicos na plataforma. 2. Visualizar a lista de projetos que possuem alguma relação ou afinidade com o projeto visualizado pelo usuário. | O usuário pode visualizar de forma clara e organizada todos os projetos sinérgicos relacionados ao projeto visualizado. | O usuário tem acesso à lista de projetos sinérgicos na plataforma. |

<sup>Fonte: Os autores (2024)</sup>

</div>

### RF-022

**Possibilidade de Ocultar a Demonstração de Interesse para Pessoas Não Envolvidas**

A aplicação deve permitir que os usuários ocultem a demonstração de interesse em seus projetos para pessoas que não estão diretamente envolvidas ou relacionadas ao projeto.

#### Critérios de Aceitação

1. Os usuários devem ter a opção de ocultar a demonstração de interesse em seus projetos.
2. Quando a opção de ocultar a demonstração de interesse é ativada, apenas as pessoas envolvidas ou relacionadas ao projeto podem visualizar a demonstração de interesse.
3. A demonstração de interesse deve ser visível apenas para pessoas autorizadas, como os criadores do projeto e usuários envolvidos.

#### Descrição dos Testes

<div align="center">
   <sub>Quadro 22 - Descrição dos casos de teste do RF-022</sub>

| Nome                                                          | Pré-condição                                                   | Procedimentos                                                                                                                   | Resultado Esperado                                                                                                   | Pós-condição                                                                                                               |
| ------------------------------------------------------------- | -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| Ocultar Demonstração de Interesse para Pessoas Não Envolvidas | O usuário acessa as configurações de um projeto na plataforma. | 1. Acessar as configurações do projeto. 2. Ativar a opção para ocultar a demonstração de interesse para pessoas não envolvidas. | A demonstração de interesse é ocultada para pessoas que não estão diretamente envolvidas ou relacionadas ao projeto. | A demonstração de interesse é visível apenas para pessoas autorizadas, como os criadores do projeto e usuários envolvidos. |

<sup>Fonte: Os autores (2024)</sup>

</div>

### RF-023

**Listagem dos CEOs Envolvidos no Projeto**

A aplicação deve fornecer uma lista dos CEOs envolvidos em um projeto específico na plataforma.

#### Critérios de Aceitação

1. Os usuários devem ter acesso a uma lista dos CEOs envolvidos em um projeto.
2. A lista deve apresentar os CEOs de forma clara e organizada para fácil visualização.
3. Para cada CEO listado, devem ser fornecidas informações relevantes, como nome, cargo, empresa, entre outros.

#### Descrição dos Testes

<div align="center">
   <sub>Quadro 23 - Descrição dos casos de teste do RF-023</sub>

| Nome                                    | Pré-condição                                              | Procedimentos                                                                                      | Resultado Esperado                                                                         | Pós-condição                                                              |
| --------------------------------------- | --------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------- |
| Listagem dos CEOs Envolvidos no Projeto | O usuário acessa os detalhes de um projeto na plataforma. | 1. Acessar os detalhes do projeto específico. 2. Visualizar a lista de CEOs envolvidos no projeto. | O usuário pode visualizar de forma clara e organizada todos os CEOs envolvidos no projeto. | O usuário tem acesso à lista de CEOs envolvidos no projeto na plataforma. |

<sup>Fonte: Os autores (2024)</sup>

</div>

### RF-024

**Visualização de projetos de um determinado CEO**

A aplicação deve permitir que os usuários visualizem os projetos associados a um determinado CEO na plataforma.

#### Critérios de Aceitação

1. Os usuários devem ter acesso a uma lista dos projetos associados a um determinado CEO.
2. A lista deve apresentar os projetos de forma clara e organizada para fácil visualização.
3. Para cada projeto listado, devem ser fornecidas informações relevantes, como título, descrição, datas, entre outros.

#### Descrição dos Testes

<div align="center">
   <sub>Quadro 24 - Descrição dos casos de teste do RF-024</sub>

| Nome                                           | Pré-condição                                          | Procedimentos                                                                                  | Resultado Esperado                                                                                       | Pós-condição                                                              |
| ---------------------------------------------- | ----------------------------------------------------- | ---------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| Visualização de Projetos de um Determinado CEO | O usuário acessa os detalhes de um CEO na plataforma. | 1. Acessar os detalhes do CEO específico. 2. Visualizar a lista de projetos associados ao CEO. | O usuário pode visualizar de forma clara e organizada todos os projetos associados ao CEO na plataforma. | O usuário tem acesso à lista de projetos associados ao CEO na plataforma. |

<sup>Fonte: Os autores (2024)</sup>

</div>

### **Notícias**

### RF-025

**Listagem de notícias relacionadas aos interesses do usuário**

A aplicação deve fornecer uma lista de notícias relacionadas aos interesses do usuário na plataforma.

#### Critérios de Aceitação

1. Os usuários devem ter acesso a uma lista de notícias relacionadas aos interesses indicados em seus perfis.
2. A lista de notícias deve ser personalizada para cada usuário, levando em consideração seus interesses e interações anteriores na plataforma.
3. As notícias devem ser apresentadas de forma clara e organizada para fácil visualização.

#### Descrição dos Testes

<div align="center">
   <sub>Quadro 25 - Descrição dos casos de teste do RF-025</sub>

| Nome                                                        | Pré-condição                                        | Procedimentos                                                                                                          | Resultado Esperado                                                                                                      | Pós-condição                                                                             |
| ----------------------------------------------------------- | --------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| Listagem de Notícias Relacionadas aos Interesses do Usuário | O usuário acessa a seção de notícias na plataforma. | 1. Acessar a seção de notícias. 2. Visualizar a lista de notícias relacionadas aos interesses indicados em seu perfil. | O usuário pode visualizar de forma clara e organizada todas as notícias relacionadas aos seus interesses na plataforma. | O usuário tem acesso à lista de notícias relacionadas aos seus interesses na plataforma. |

<sup>Fonte: Os autores (2024)</sup>

</div>

### RF-026

**Redirecionamento ao site da notícia**

A aplicação deve permitir que os usuários sejam redirecionados ao site da notícia ao clicarem em uma notícia listada na plataforma.

#### Critérios de Aceitação

1. Os usuários devem ter a opção de clicar em uma notícia listada na plataforma para serem redirecionados ao site da notícia.
2. O redirecionamento deve ocorrer de forma rápida e eficiente.
3. A notícia deve ser aberta no navegador padrão do usuário.

#### Descrição dos Testes

<div align="center">
   <sub>Quadro 26 - Descrição dos casos de teste do RF-026</sub>

| Nome                                | Pré-condição                                        | Procedimentos                                   | Resultado Esperado                                                | Pós-condição                                                                           |
| ----------------------------------- | --------------------------------------------------- | ----------------------------------------------- | ----------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| Redirecionamento ao Site da Notícia | O usuário acessa a lista de notícias na plataforma. | 1. Clicar em uma notícia listada na plataforma. | O usuário é redirecionado ao site da notícia no navegador padrão. | O usuário é redirecionado ao site da notícia após clicar em uma notícia na plataforma. |

<sup>Fonte: Os autores (2024)</sup>

</div>

**Temas**

### RF-027

**Listagem dos macrotemas**

A aplicação deve fornecer uma lista dos macrotemas disponíveis na plataforma.

#### Critérios de Aceitação

1. Os usuários devem ter acesso a uma lista dos macrotemas disponíveis na plataforma.
2. A lista de macrotemas deve ser apresentada de forma clara e organizada para fácil visualização.
3. Cada macrotema listado deve conter informações relevantes, como título e descrição.

#### Descrição dos Testes

<div align="center">
   <sub>Quadro 27 - Descrição dos casos de teste do RF-027</sub>

| Nome                    | Pré-condição                                          | Procedimentos                                                                      | Resultado Esperado                                                                                   | Pós-condição                                              |
| ----------------------- | ----------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| Listagem dos Macrotemas | O usuário acessa a seção de macrotemas na plataforma. | 1. Acessar a seção de macrotemas. 2. Visualizar a lista de macrotemas disponíveis. | O usuário pode visualizar de forma clara e organizada todos os macrotemas disponíveis na plataforma. | O usuário tem acesso à lista de macrotemas na plataforma. |

<sup>Fonte: Os autores (2024)</sup>

</div>

### RF-028

**Listagem dos Subtemas**

A aplicação deve fornecer uma lista dos subtemas disponíveis na plataforma, organizados por macrotema.

#### Critérios de Aceitação

1. Os usuários devem ter acesso a uma lista dos subtemas disponíveis na plataforma.
2. A lista de subtemas deve ser organizada por macrotema para uma fácil navegação.
3. Cada subtema listado deve conter informações relevantes, como título e descrição.

#### Descrição dos Testes

<div align="center">
   <sub>Quadro 28 - Descrição dos casos de teste do RF-028</sub>

| Nome                  | Pré-condição                                        | Procedimentos                                                                                            | Resultado Esperado                                                                                                            | Pós-condição                                                                      |
| --------------------- | --------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| Listagem dos Subtemas | O usuário acessa a seção de subtemas na plataforma. | 1. Acessar a seção de subtemas. 2. Visualizar a lista de subtemas disponíveis organizados por macrotema. | O usuário pode visualizar de forma clara e organizada todos os subtemas disponíveis na plataforma, organizados por macrotema. | O usuário tem acesso à lista de subtemas organizados por macrotema na plataforma. |

<sup>Fonte: Os autores (2024)</sup>

</div>

### RF-029

**Listagem dos Projetos por Subtema**

A aplicação deve permitir que os usuários visualizem os projetos disponíveis na plataforma organizados por subtema.

#### Critérios de Aceitação

1. Os usuários devem ter acesso a uma lista dos projetos disponíveis na plataforma organizados por subtema.
2. A lista de projetos deve ser apresentada de forma clara e organizada para fácil visualização.
3. Cada projeto listado deve conter informações relevantes, como título, descrição, datas, entre outros.

#### Descrição dos Testes

<div align="center">
   <sub>Quadro 29 - Descrição dos casos de teste do RF-029</sub>

| Nome                              | Pré-condição                                        | Procedimentos                                                                                                             | Resultado Esperado                                                                                                         | Pós-condição                                                                    |
| --------------------------------- | --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| Listagem dos Projetos por Subtema | O usuário acessa a seção de projetos na plataforma. | 1. Selecionar um subtema específico na plataforma. 2. Visualizar a lista de projetos disponíveis organizados por subtema. | O usuário pode visualizar de forma clara e organizada todos os projetos disponíveis na plataforma organizados por subtema. | O usuário tem acesso à lista de projetos organizados por subtema na plataforma. |

<sup>Fonte: Os autores (2024)</sup>

</div>

**Arquivar projeto autoral**

A aplicação deve permitir que os usuários arquivem projetos autorais na plataforma.

#### Critérios de Aceitação

1. Os usuários devem ter a opção de arquivar projetos autorais.
2. Quando um projeto é arquivado, ele não é removido permanentemente da plataforma, mas sim movido para uma área de arquivos ou pastas separadas.
3. Os projetos arquivados devem ser facilmente acessíveis para os usuários, caso desejem restaurá-los ou visualizá-los novamente.

#### Descrição dos Testes

<div align="center">
   <sub>Quadro 30 - Descrição dos casos de teste do RF-030</sub>

| Nome                     | Pré-condição                                                   | Procedimentos                                                                                              | Resultado Esperado                                                   | Pós-condição                                                                                  |
| ------------------------ | -------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| Arquivar Projeto Autoral | O usuário acessa suas configurações de projetos na plataforma. | 1. Acessar as configurações do projeto que deseja arquivar. 2. Selecionar a opção para arquivar o projeto. | O projeto é arquivado e movido para uma área separada na plataforma. | O projeto é arquivado e pode ser facilmente acessado na área de arquivos ou pastas separadas. |

<sup>Fonte: Os autores (2024)</sup>

</div>

## 5.2 Requisitos não Funcionais

&emsp;&emsp;Com base nos requisitos funcionais mencionados anteriormente e considerando a estrutura proposta por Ian Sommerville, juntamente com a **ISO/IEC 25010:2011** para qualidade do produto de software, será apresentado a seguir os requisitos não funcionais. Esses requisitos foram categorizados e vinculados a requisitos funcionais específicos, utilizando o seguinte agrupamento dos requisitos não funcionais: desempenho, segurança, usabilidade, confiabilidade, manutenibilidade e portabilidade. Essa abordagem assegura uma visão abrangente e detalhada das características necessárias para atender às expectativas de qualidade e eficiência do software.

<div align="center">
  <sub>Figura X - Tipos de Requisitos Não Funcionais</sub>
  <img src="./assets/images/diagrama-requisitos-nao-funcionais.png" alt="Tipos de Requisitos Não Funcionais" width="100%">
  <sup>Fonte: Sommerville, 2016</sup>
</div>

&emsp;&emsp;Sob essa perspectiva, é notório que há três principais tipos de requisitos não funcionais, sendo eles:

- **Requisitos de produto**: Responsáveis por especificar ou restringir o comportamento do software, considerando eficiência, confiança, proteção e usabilidade.
- **Requisitos organizacionais**: São impostos pela organização do cliente, neste projeto são impostos pela FDC, ou pela organização do desenvolvedor, neste caso, o Inteli. Podem estar relacionados ao ambiente de desenvolvimento, ao modo como o sistema será usado e ao modo como será desenvolvido.
- **Requisitos externos**: Todos os requisitos que surgem de fontes externas ao sistema. Podem ser, éticos, legais, reguladores, etc.

### Requisitos de Produto

1. **Eficiência**

   - **Desempenho do Aplicativo**: O aplicativo deve responder a interações do usuário dentro de 2 segundos em 95% dos casos, testável via monitoramento de tempo de resposta em funções críticas, como o login e a listagem dos projetos recomendados.
   - **ISO/IEC 25010**: Eficiência de Desempenho - Tempo de Resposta

2. **Confiabilidade**

   - **Disponibilidade do Serviço**: O sistema deve ter uma disponibilidade de 99.9% mensalmente, testável através do monitoramento de uptime.
   - **ISO/IEC 25010**: Confiabilidade - Disponibilidade

3. **Proteção**

   - **Segurança de Dados**: Todos os dados sensíveis, como informações de login dos CEOs, devem ser criptografados em trânsito e em repouso, alinhado com a política de segurança da organização.
   - **ISO/IEC 25010**: Segurança - Confidencialidade

4. **Usabilidade**

   - **Facilidade de Uso**: O aplicativo deve ter uma taxa de conclusão de tarefas por novos usuários de pelo menos 90% sem assistência, medido por testes de usabilidade.
   - **ISO/IEC 25010**: Usabilidade - Facilidade de uso

### Requisitos Organizacionais

5. **Requisitos Ambientais**

   - **Compatibilidade com Navegadores/Dispositivos**: O sistema deve ser compatível com as duas últimas versões dos principais navegadores e sistemas operacionais móveis.
   - **ISO/IEC 25010**: Compatibilidade - Interoperabilidade

6. **Requisitos Operacionais**

   - **Conformidade com o Processo de Desenvolvimento**: O desenvolvimento do software deve seguir as práticas ágeis definidas pela organização, incluindo sprints de duas semanas e revisões regulares.
   - **ISO/IEC 25010**: Manutenibilidade - Modificabilidade

7. **Requisitos de Desenvolvimento**
   - **Testes Automatizados**: O sistema deve ter uma cobertura de testes automatizados de pelo menos 75%, garantindo a verificação contínua da funcionalidade e qualidade do produto.
   - **ISO/IEC 25010**: Manutenibilidade - Testabilidade

### Requisitos Externos

8. **Requisitos Reguladores**

   - **Conformidade com a LGPD**: O sistema deve aderir às regulamentações da LGPD em relação ao manuseio de dados pessoais de usuários do Brasil.
   - **ISO/IEC 25010**: Legalidade

9. **Requisitos Éticos**

   - **Respeito à Privacidade do Usuário**: O sistema deve projetar e implementar funcionalidades respeitando a privacidade dos usuários, como ocultar demonstrações de interesse para pessoas não envolvidas.
   - **ISO/IEC 25010**: Privacidade

10. **Requisitos Legais**
    - **Direitos Autorais**: O sistema deve garantir que todo o conteúdo, como notícias e descrições de projetos, respeite os direitos autorais aplicáveis.
    - **ISO/IEC 25010**: Legalidade - Conformidade com Direitos Autorais

&emsp;&emsp;Os requisitos não funcionais acima descritos são essenciais para garantir a qualidade do produto de software e atender às expectativas dos usuários e das partes interessadas. A conformidade com esses requisitos é fundamental para o sucesso do projeto `Coffee Break` e para a satisfação dos usuários finais. Além de assegurar que o software funcione corretamente sob diferentes condições, esses requisitos contribuem para a segurança, usabilidade, confiabilidade e manutenibilidade do sistema. Cumprir esses critérios não apenas melhora a experiência do usuário, mas também fortalece a confiança e a reputação da plataforma no mercado.

## 5.3 Casos de Uso

&emsp;&emsp;De acordo com Priscila Souza<sup>[\[3\]](#referências)</sup>, os casos de uso são representações abstratas da interação entre um sistema e seus usuários, descrevendo como o sistema responde a determinadas ações dos usuários. O diagrama de caso de uso surge para representar graficamente ilustrações das interações entre os atores (usuários ou sistemas externos) e o sistema em questão, identificando os principais cenários de uso do sistema. De acordo com os requisitos funcionais, foram desenvolvidos os seguintes diagramas de casos de uso:

#### 1. Manipulação de contas

<div align="center">
  <sub>Figura 8 - Diagrama de Caso de Uso: "Manipulação de contas"</sub>
  <img src="./assets/images/caso-de-uso-1.jpeg" width="100%" alt='Diagrama de Caso de Uso: "Manipulação de contas"'>
  <sup>Fonte: Os autores (2024)</sup>
</div>

**História de usuário:** "Como administrador da CEOs' Legacy, quero gerenciar as contas dos CEOs dentro da plataforma para que eu consiga controlar o acesso dos usuários."

#### 2. Editar perfil

<div align="center">
  <sub>Figura 9 - Diagrama de Caso de Uso: "Editar perfil"</sub>
  <img src="./assets/images/caso-de-uso-2.jpeg" width="100%" alt='Diagrama de Caso de Uso: "Editar perfil"'>
  <sup>Fonte: Os autores (2024)</sup>
</div>

**História de usuário:** "Como usuário, quero editar o meu perfil para que eu consiga manter os meus dados pessoais e da minha empresa atualizados."

#### 3. Visualizar perfil

<div align="center">
  <sub>Figura 10 - Diagrama de Caso de Uso: "Visualizar perfil"</sub>
  <img src="./assets/images/caso-de-uso-3.jpeg" width="100%" alt='Diagrama de Caso de Uso: "Visualizar perfil"'>
  <sup>Fonte: Os autores (2024)</sup>
</div>

**História de usuário:** "Como usuário, quero pesquisar e visualizar o perfil de CEOs para que eu consiga ver suas informações e projetos."

#### 4. Login

<div align="center">
  <sub>Figura 11 - Diagrama de Caso de Uso: "Login"</sub>
  <img src="./assets/images/caso-de-uso-4.jpeg" width="100%" alt='Diagrama de Caso de Uso: "Login"'>
  <sup>Fonte: Os autores (2024)</sup>
</div>

**História de usuário:** "Como usuário, quero ser autenticado na plataforma para que eu consiga utilizá-la."

#### 5. Manipulação de projetos

<div align="center">
  <sub>Figura 12 - Diagrama de Caso de Uso: "Manipulação de projetos"</sub>
  <img src="./assets/images/caso-de-uso-5.jpeg" width="100%" alt='Diagrama de Caso de Uso: "Manipulação de projetos"'>
  <sup>Fonte: Os autores (2024)</sup>
</div>

**Histórias de usuário:**

- "Como usuário, quero gerenciar os meus projetos para que eu tenha um total controle sobre eles e suas informações."
- "Como usuário, quero arquivar os meus projetos para que eles não apareçam mais no meu perfil."

#### 6. Interação com projetos

<div align="center">
  <sub>Figura 13 - Diagrama de Caso de Uso: "Interação com projetos"</sub>
  <img src="./assets/images/caso-de-uso-6.jpeg" width="100%" alt='Diagrama de Caso de Uso: "Interação com projetos"'>
  <sup>Fonte: Os autores (2024)</sup>
</div>

**Histórias de usuário:**

- "Como usuário, quero curtir projetos alheios para que eu consiga interagir melhor com outros CEOs."
- "Como usuário, quero salvar projetos para que eu consiga acessá-los em um outro momento."
- "Como usuário, quero solicitar interesse em projetos alheios para que consiga fazer sinergia com eles."
- "Como usuário, quero aceitar ou rejeitar solicitações de sinergia ao meu projeto para que eu consiga escolher quem irá participar."

#### 7. Visualização de projetos

<div align="center">
  <sub>Figura 14 - Diagrama de Caso de Uso: "Visualização de projetos"</sub>
  <img src="./assets/images/caso-de-uso-7.jpeg" width="100%" alt='Diagrama de Caso de Uso: "Visualização de projetos"'>
  <sup>Fonte: Os autores (2024)</sup>
</div>

**História de usuário:** "Como usuário, quero visualizar projetos de maneiras diferentes e personalizadas para que eu consiga encontrar exatamente os projetos que desejo fazer sinergia."

#### 8. Filtragem de projetos por tema

<div align="center">
  <sub>Figura 15 - Diagrama de Caso de Uso: "Filtragem de projetos por tema"</sub>
  <img src="./assets/images/caso-de-uso-8.jpeg" width="100%" alt='Diagrama de Caso de Uso: "Filtragem de projetos por tema"'>
  <sup>Fonte: Os autores (2024)</sup>
</div>

**História de usuário:** "Como usuário, quero filtrar projetos por temas para que eu consiga encontrar projetos com mais facilidade e rapidez."

#### 9. Notícias

<div align="center">
  <sub>Figura 16 - Diagrama de Caso de Uso: "Notícias"</sub>
  <img src="./assets/images/caso-de-uso-9.jpeg" width="100%" alt='Diagrama de Caso de Uso: "Notícias"'>
  <sup>Fonte: Os autores (2024)</sup>
</div>

**História de usuário:** "Como usuário, quero visualizar notícias relacionadas aos meus interesses para que eu possa ficar mais por dentro de um determinado assunto.”

## 5.4 Casos de Uso x Requisitos Funcionais

&emsp;&emsp;No desenvolvimento de software, a definição clara e precisa dos requisitos é fundamental para o sucesso de qualquer projeto. Dois conceitos essenciais para capturar essas necessidades são os casos de uso e os requisitos funcionais. Os casos de uso fornecem uma descrição narrativa das interações entre os usuários (atores) e o sistema, destacando como o sistema deve comportar-se em diferentes cenários de uso. Eles ajudam a entender os objetivos dos usuários e a forma como o sistema deve apoiá-los para alcançar esses objetivos.  Por outro lado, os requisitos funcionais são declarações específicas que detalham o que o sistema deve fazer. Eles traduzem os casos de uso em funcionalidades concretas que o sistema deve possuir para cumprir os objetivos descritos. 

&emsp;&emsp;Cada requisito funcional deve ser claro, verificável e completo, garantindo que todas as funcionalidades necessárias sejam implementadas de acordo com as expectativas dos usuários e das partes interessadas. Para o projeto `Coffee Break`, alinhar casos de uso com requisitos funcionais é fundamental para assegurar que todas as necessidades dos usuários sejam atendidas de maneira eficaz. Esse alinhamento permite que o desenvolvimento do software siga um caminho claro e organizado, facilitando a comunicação entre desenvolvedores, designers e usuários finais. Através dessa abordagem estruturada, podemos garantir que o projeto não só atenda às expectativas iniciais, mas também seja adaptável e escalável para futuras melhorias e expansões.

| Caso de uso                       | Requisitos Funcionais                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1. Manipulação de contas          | - RF-001: Cadastro de CEOs via Admin<br>- RF-004: Inativação/Ativação de usuários via Admin<br>                                                                                                                                                                                                                                                                                                                                                                   |
| 2. Editar perfil                  | - RF-002: Edição do perfil do CEO<br>                                                                                                                                                                                                                                                                                                                                                                                                                             |
| 3. Visualizar perfil              | - RF-005: Visualização de perfis de forma global                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 4. Login                          | - RF-003: Login no aplicativo                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| 5. Manipulação de projetos        | - RF-006: Cadastro de Projetos<br>- RF-007 Edição de Projeto<br>- RF-022: Possibilidade de ocultar a demonstração de interesse para pessoas não envolvidas<br>- RF-008: Inativação/Ativação de projetos<br>- RF-030: Arquivar projeto autoral                                                                                                                                                                                                                     |
| 6. Interação com projetos         | - RF-009: Possibilidade de curtir um projeto<br>- RF-010: Possibilidade de demonstrar interesse em um projeto<br>- RF-011: Possibilidade de salvar um projeto como favorito<br>- RF-014: Aceitar / Recusar demonstração de interesse<br>- RF-013: Listagem de notificações sobre demonstração de interesse<br>- RF-012: Envio de notificação ao criador do projeto sobre a demonstração de interesse                                                              |
| 7. Visualização de projetos       | - RF-015: Listagem dos projetos autorais<br>- RF-016: Listagem dos projetos recomendados<br>- RF-017: Listagem de todos os projetos com filtros<br>- RF-018: Listagem de projetos curtidos<br>- RF-019: Listagem de projetos com demonstração de interesse<br>- RF-020: Listagem de projetos salvos<br>- RF-021: Listagem de projetos sinérgicos<br>- RF-023: Listagem dos CEOs envolvidos no projeto<br>- RF-024: Visualização de projetos de um determinado CEO |
| 8. Filtragem de projetos por tema | - RF-027: Listagem dos macrotemas<br>- RF-028: Listagem dos subtemas<br>- RF-029: Listagem dos projetos por subtema                                                                                                                                                                                                                                                                                                                                               |
| 9. Notícias                       | - RF-025: Listagem de notícias relacionadas aos interesses do usuário<br>- RF-026: Redirecionamento ao site da notícia                                                                                                                                                                                                                                                                                                                                            |

# 6. Projeto de Solução

&emsp;&emsp;No contexto do desenvolvimento de software, é fundamental estruturar um projeto de solução. Foram definidos as arquiteruda da solução juntamente com os diagramas de classe, que desempenham um papel importante no planejamento e na construção de soluções robustas e eficientes. Esses diagramas, parte integrante da UML (Unified Modeling Language), fornecem uma representação visual das classes, seus atributos, métodos e as relações entre elas dentro de um sistema. Ao capturar a estrutura estática do sistema, os diagramas de classe ajudam a esclarecer e organizar os componentes fundamentais do projeto, facilitando a comunicação entre desenvolvedores e outras partes interessadas.

&emsp;&emsp;Para o projeto `Coffee Break`, o planejamento cuidadoso é essencial para assegurar que todos os requisitos, tanto funcionais quanto não funcionais, sejam atendidos de maneira eficaz. A criação de diagramas de classe detalhados permitirá uma visão clara da arquitetura do software, identificando as principais entidades e suas interações. Esse planejamento inicial é vital para garantir que a solução desenvolvida seja escalável, mantenível e alinhada com os objetivos estratégicos do projeto. Além disso, o uso de diagramas de classe e a construção da arquitetura contribuem para a identificação precoce de possíveis problemas e inconsistências, permitindo ajustes antes da implementação da solução.

## 6.1 Diagrama de Classes

&emsp;&emsp;Um diagrama de classes, especialmente o diagrama de classes de domínio, é uma representação visual de um modelo de domínio de negócios. Ele descreve as entidades envolvidas em um sistema e os relacionamentos entre essas entidades. O diagrama de classes de domínio é uma ferramenta útil para modelar sistemas de informação complexos e é frequentemente usado em conjunto com diagramas de sequência e diagramas de atividades para modelar a lógica de negócios de um sistema. O diagrama de classes de domínio é uma parte importante do processo de desenvolvimento de software e é frequentemente usado para comunicar ideias entre desenvolvedores, designers e partes interessadas.

&emsp;&emsp;Dessa forma, para este projeto, o diagrama de classes foi elaborado com base nas entidades e relacionamentos previstas para o `Coffee Break`, a fim de representar visualmente o modelo de domínio de negócios. O diagrama de classes foi elaborado utilizando a ferramenta [_Lucidchart_](https://www.lucidchart.com/pages/pt/landing), que é uma ferramenta de diagramação online que permite a criação de diversos diagramas de forma colaborativa e intuitiva. A seguir, é apresentado o diagrama de classes elaborado para o projeto `Coffee Break`.

<div align="center">
  <sub>Figura 17 - Diagrama de Classes do Projeto Coffee Break</sub>
  <img src="./assets/images/diagrama-de-classes-de-dominio.png" width="100%" alt="Diagrama de Classes do Projeto Coffee Break">
  <sup>Fonte: Os autores (2024)</sup>
</div>

&emsp;&emsp;Conforme demonstrado na figura acima, o diagrama de classes do projeto `Coffee Break` foi elaborado com base nas entidades e relacionamentos previstos para o sistema. Dessa forma, as classes identificadas, bem como seus atributos, métodos e relacionamentos, foram representadas no diagrama em questão. A seguir, é apresentada uma descrição detalhada de cada classe identificada no diagrama de classes do projeto `Coffee Break`.

1. `Usuário`

- **Atributos**: Identificador único, nome, email, cargo, senha, tipo de usuário (como CEO ou Administrador da FDC), link do LinkedIn, email de contato, nome da empresa, foto da empresa, foto de perfil, celular, link do site da empresa e biografia.
- **Métodos**:
  - Receber notificações relacionadas à atividade do usuário no sistema.
  - Adicionar um novo projeto à lista de projetos que o usuário gerencia.
  - Remover um projeto específico da lista do usuário.

2. `Grupo`

- **Atributos**: Identificador único, nome e descrição do grupo.
- **Métodos**:
  - Incluir um usuário no grupo.
  - Remover um usuário do grupo.

3. `Projeto`

- **Atributos**: Identificador único, nome, descrição detalhada, data de criação e identificador do usuário que é o CEO do projeto.
- **Métodos**:
  - Atualizar as informações do projeto com novos dados.
  - Adicionar um interesse de um usuário no projeto.
  - Remover o interesse de um usuário no projeto.
  - Registrar que um usuário curtiu o projeto.
  - Registrar que um usuário retirou a curtida do projeto.
  - Marcar um projeto como favorito para fácil acesso posterior do usuário.
  - Remover um projeto da lista de favoritos do usuário.

4. `Subtema`

- **Atributos**: Identificador único, nome e descrição do subtema.
- **Métodos**:
  - Associar um projeto a este subtema.
  - Desassociar um projeto deste subtema.

5. `Macrotema`

- **Atributos**: Identificador único, nome e descrição do macrotema.
- **Métodos**:
  - Adicionar um subtema ao macrotema.
  - Remover um subtema do macrotema.

6. `Interação (Classe Base)`

- **Atributos**: Identificador único, identificador do usuário que realizou a interação, identificador do projeto alvo e data da interação.
- **Métodos**:
  - Registrar uma interação geral no sistema.
  - Remover uma interação geral do sistema.

7. `Favorito (Derivado de Interação)`

- **Métodos**:
  - Registrar um projeto como favorito por um usuário.
  - Remover um projeto da lista de favoritos de um usuário.

8. `Like (Derivado de Interação)`

- **Métodos**:
  - Registrar que um usuário curtiu um projeto.
  - Remover a curtida de um usuário em um projeto.

9. `Interesse (Derivado de Interação)`

- **Métodos**:
  - Registrar o interesse de um usuário em um projeto.
  - Remover o interesse de um usuário em um projeto.

10. `Notificação`

- **Atributos**: Identificador único, identificador do usuário que deve receber a notificação, conteúdo da mensagem, data da notificação e status para indicar se foi lida.
- **Métodos**:
  - Enviar uma notificação a um usuário.
  - Marcar a notificação como lida pelo usuário.

&emsp;&emsp;Essas classes representam a estrutura do sistema de gerenciamento do projeto `Coffee Break`, refletindo como os usuários interagem com os projetos e entre si através de ações como curtidas, favoritos e expressão de interesse. A estrutura detalhada das classes define as relações e interações essenciais para o funcionamento do sistema, permitindo uma gestão eficiente e intuitiva dos projetos. Além disso, as notificações desempenham um papel fundamental ao manter os usuários informados sobre atualizações e mudanças importantes, garantindo que estejam sempre cientes das novidades e possam reagir de forma oportuna. Essa abordagem estruturada e interativa é fundamental para promover um ambiente colaborativo e dinâmico dentro da plataforma.

## 6.2 Arquitetura da Solução

&emsp;&emsp;A arquitetura SOA (Service-Oriented Architecture), ou Arquitetura Orientada a Serviços, é um paradigma de design de software que enfatiza a criação e o uso de serviços autônomos e reutilizáveis, que podem interagir entre si através de interfaces padronizadas e tecnologicamente agnósticas. Esta abordagem permite a construção de sistemas complexos por meio da composição de serviços independentes, que encapsulam distintas lógicas de negócio e podem ser distribuídos em diferentes ambientes de rede.

&emsp;&emsp;Os serviços em uma arquitetura SOA são projetados para serem modulares, permitindo que sejam facilmente modificados, substituídos, reutilizados ou realocados sem impactar o restante do sistema. Para melhor estruturação e início de entendimento da estrutura do projeto, foi desenvolvido um diagrama de solução UML, que contém detalhes sobre as integrações entre componentes, descrições sobre as tecnologias utilizadas e fluxo de dados. Segue abaixo o diagrama da arquitetura SOA do projeto para a Fundação Dom Cabral:

<div align="center">
<sub>Figura 18 - Diagrama da Arquitetura SOA</sub>
<img src="/docs/assets/images/diagrama-arquitetura.png" alt="Diagrama da Arquitetura SOA" title="Diagrama da Arquitetura SOA" />
<sup>Fonte: Os autores (2024)</sup>
</div>

1. `Clientes (Mobile e Desktop):` Representam os pontos de acesso dos usuários, através de aplicativos móveis e, como uma possível implementação, as interfaces de desktop. São as interfaces pelas quais os usuários interagem com o sistema, utilizando seus serviços e funcionalidades gerais.

2. `Mobile BFF e Dashboard BFF (Backend for Frontend):` São camadas de serviço que agem como intermediárias entre os clientes (Mobile e Desktop) e os serviços back-end. O BFF é otimizado para a melhor experiência do usuário em cada dispositivo ou plataforma específica.

3. `APIs Externas (Google API, DiceBear API, News API):` Estas APIs fornecem funcionalidades adicionais e dados externos, integrando-se ao sistema através dos BFFs. A Google API pode ser utilizada para autenticação e serviços relacionados ao Google, a DiceBear API para geração de avatares personalizados, e a News API para incorporação de notícias relevantes e atualizadas, enriquecendo a experiência do usuário com conteúdo dinâmico e personalizado.

4. `Serviços (Usuários, Recomendações, Projetos):` Estes são microserviços independentes, cada um lidando com uma parte específica da lógica de negócio. O serviço 'Usuários' gerencia o acesso e informações do usuário, 'Recomendações' fornece sugestões personalizadas e 'Projetos' lida com a gestão de projetos dentro do sistema.

5. `Banco de Dados:` É o sistema de armazenamento centralizado onde todos os dados do aplicativo são mantidos. Ele é acessado através do middleware para garantir a segurança e integridade dos dados informados e coletados pelo app.

&emsp;&emsp;A inclusão de APIs externas adiciona uma camada de flexibilidade e capacidade de resposta, permitindo que o sistema não só gerencie dados internos mas também integre e utilize dados externos de forma eficiente e segura, aumentando a funcionalidade e valor para o usuário final.

### Fluxo de Dados

&emsp;&emsp;O fluxo de dados refere-se ao caminho que os dados percorrem em um sistema de informação, desde o ponto de entrada até o processamento, armazenamento e eventual saída ou uso. No caso deste projeto, consiste nas integrações entre os componentes da solução, fazendo com que o funcionamento da mesma seja bem estruturado e eficiente. Com isso, os componentes presentes na arquitetura SOA seguem as referentes interações:

- O cliente (Mobile ou Desktop) faz uma solicitação ao BFF correspondente (Mobile BFF ou Dashboard BFF).
- O BFF processa a solicitação, podendo realizar uma lógica de negócios básica, e então encaminha a solicitação para o serviço apropriado (Usuários, Recomendações ou Projetos).
- O serviço processa a solicitação e, se necessário, interage com o Middleware de Acesso a Banco para recuperar ou persistir dados no Banco de Dados PostgreSQL.
- O serviço envia a resposta de volta ao BFF.
- O BFF então envia a resposta de volta ao cliente, completando o ciclo de solicitação-resposta.

&emsp;&emsp;Cada solicitação dentro da arquitetura segue um fluxo meticulosamente definido, assegurando que os dados sejam processados e gerenciados de maneira eficiente e segura. Este processo tira proveito dos princípios fundamentais de desacoplamento e modularidade inerentes à arquitetura SOA. Esses princípios permitem que cada componente do sistema opere independentemente, enquanto ainda contribui para o funcionamento holístico do sistema, facilitando a escalabilidade e a manutenção.

&emsp;&emsp;Além disso, é fundamental destacar que as informações apresentadas acima são vitais para a estruturação eficaz do projeto. A implementação de uma arquitetura orientada a serviços não apenas melhora a interoperabilidade entre diferentes serviços e aplicações, mas também potencializa a flexibilidade com que a organização pode responder às mudanças do mercado ou a novas demandas empresariais. Portanto, adotar a arquitetura SOA pode significar uma vantagem competitiva significativa, permitindo uma integração mais ágil e robusta de novas funcionalidades e serviços ao longo do tempo.

## 6.3 Diagrama de Implantação

&emsp;&emsp;Um diagrama de implantação é uma representação gráfica usada em modelagem de software para especificar a configuração física dos artefatos, baseando nas unidades de software quanto nas unidades de hardware. Ele mostra como o software é distribuído literalmente em diferentes máquinas ou componentes de hardware e descreve as dependências físicas entre eles. Esses diagramas são úteis para visualizar, definir e documentar sistemas distribuídos, bem como para detalhar a infraestrutura necessária para o funcionamento do sistema.

<div align="center">
  <sub>Figura 19 - Diagrama de Implantação</sub>
  <img src="./assets/images/diagrama-de-implantacao.jpg" width="100%" alt="Diagrama de Implantação">
  <sup>Fonte: Os autores (2024)</sup>
</div>

&emsp;&emsp;O diagrama de implantação mostra a estrutura de um sistema distribuído usando a infraestrutura da Amazon Web Services (AWS). O sistema é dividido em dois grupos principais de nós hospedados no Amazon Elastic Compute Cloud (EC2). O primeiro grupo de nós EC2 contém três serviços: User Service, Project Service e Recommendation Service. Esses serviços se comunicam usando o protocolo TCP/IP com um nó do Relational Database Service (RDS) que hospeda um artefato PostgreSQL, indicando uma conexão de banco de dados.

&emsp;&emsp;Além dos serviços principais, este sistema também incorpora várias APIs externas como DiceBear API para geração de avatares, Google API para integrações variadas e News API para a aquisição de notícias atualizadas, todas comunicando-se através de HTTPS. Essas APIs estão estrategicamente posicionadas para oferecer funcionalidades complementares aos serviços principais, melhorando a experiência do usuário final e enriquecendo o aplicativo com dados externos relevantes. Como atualização, a Database também foi adicionada ao nó principal, foi está diretamente relacionada com o banco de dados.

&emsp;&emsp;O segundo grupo de nós EC2 contém um serviço chamado Mobile BFF (Backend For Frontend), que se comunica via HTTPS. Esta unidade está ligada a um dispositivo móvel, também comunicando-se via HTTPS, que executa uma aplicação. Isso indica uma arquitetura que separa as responsabilidades do backend, focando em servir um frontend em dispositivos móveis de maneira otimizada. Cada serviço no diagrama é referente a uma função específica, facilitando a escalabilidade e manutenção do sistema. Além disso, a comunicação segura via HTTPS entre o backend e os dispositivos móveis enfatiza a importância da segurança nas transações de dados.

&emsp;&emsp;O diagrama de implantação é essencial para o desenvolvimento do projeto, pois oferece uma visão clara da distribuição física dos componentes de software e de como eles interagem entre si em um ambiente de produção. Ele facilita a compreensão das dependências tecnológicas e da infraestrutura necessária, o que ajuda a prevenir problemas de integração e otimiza o uso dos recursos de hardware. Além disso, promove uma melhor colaboração entre a equipe de desenvolvimento, garantindo que todos estejam alinhados com a estrutura e os requisitos técnicos do sistema.

## 6.4 Tecnologias e Ferramentas

&emsp;&emsp;No desenvolvimento da solução do aplicativo mobile `Coffee Break` para a Fundação Dom Cabral, foram utilizadas uma combinação de tecnologias e ferramentas de ponta para garantir uma aplicação sólida, escalável e eficiente, afim de contribuir para a melhor experiência dos usuários, que serão CEOs. O projeto foi estruturado com a filosofia "Mobile First", priorizando a experiência do usuário em dispositivos móveis, e depois adaptado para plataformas desktop. Abaixo estão detalhadas as tecnologias e ferramentas que desempenharam papéis fundamentais no sucesso deste projeto, tanto para Mobile quanto para Desktop:

### Linguagem de Desenvolvimento Backend:
----------------------------------------------------

#### Python

&emsp;&emsp;O projeto é desenvolvido utilizando Python como linguagem principal do backend devido à sua versatilidade e eficiência na manipulação e análise de dados. Algumas das razões para escolher Python incluem:

- **Simplicidade e Legibilidade:** Python é conhecido por sua sintaxe limpa e legível, o que facilita o desenvolvimento e a manutenção do código.

- **Ampla Comunidade e Suporte:** Python possui uma grande comunidade de desenvolvedores ativos, o que significa acesso a uma extensa biblioteca de recursos e suporte contínuo.

- **Ecossistema de Bibliotecas:** O projeto se beneficia das numerosas bibliotecas Python disponíveis, incluindo frameworks web como Flask ou Django, ferramentas para análise de dados como Pandas e NumPy, além de suporte para tarefas de aprendizado de máquina com Scikit-learn.

- **Multiplataforma:** Python é executado em diferentes sistemas operacionais, o que facilita a portabilidade do projeto.

[Documentação oficial do Python](https://docs.python.org/3/)

### Framework de Desenvolvimento Backend:
----------------------------------------------------

#### Flask

&emsp;&emsp;Flask é um framework leve de desenvolvimento web em Python. Ele é projetado para ser simples e fácil de usar, permitindo que os desenvolvedores construam aplicações web rapidamente e com menos boilerplate do que em outros frameworks mais robustos. As principais funcionalidades e benefícios do Flask incluem:

- **Roteamento Simples:** Flask facilita a definição de rotas para URLs específicos e a associação dessas rotas a funções Python.

- **Templates:** Suporta o uso de templates para renderizar páginas web dinamicamente com dados fornecidos pelas funções Python.

- **Extensibilidade:** Flask possui uma ampla variedade de extensões disponíveis para adicionar funcionalidades extras, como autenticação e ORM (Object-Relational Mapping).

- **Biblioteca WSGI:** Construído sobre o Werkzeug e utiliza o Jinja2 para seus templates, oferecendo uma infraestrutura sólida para o desenvolvimento de aplicações web.

[Documentação oficial do Flask](https://flask.palletsprojects.com/en/2.0.x/)

### Linguagem de Desenvolvimento Frontend:
----------------------------------------------------

&emsp;&emsp;Para o desenvolvimento do frontend, utilizamos a linguagem de programação Dart em conjunto com o kit de desenvolvimento Flutter, alinhado aos conceitos do Mobile-first.

## Mobile

#### Dart

&emsp;&emsp;Dart é uma linguagem de programação moderna e orientada a objetos, desenvolvida pela Google. Algumas características do Dart incluem tipagem estática opcional e compilações just-in-time (JIT) para desenvolvimento rápido e ahead-of-time (AOT) para produção eficiente de código.

[Documentação oficial do Dart](https://dart.dev/guides)

### Framework de Desenvolvimento Frontend:
----------------------------------------------------

#### Flutter

&emsp;&emsp;Flutter é um framework de desenvolvimento de interfaces de usuário (UI) criado pela Google, que permite a criação de aplicativos nativos para dispositivos móveis, web e desktop a partir de um único código-base. É conhecido por sua abordagem de desenvolvimento ágil, design flexível e alto desempenho.

[Documentação oficial do Flutter](https://flutter.dev/docs)

## Desktop 

#### HTML
&emsp;&emsp;A estrutura base da aplicação foi construída usando HTML, que organiza o conteúdo e garante a acessibilidade e estruturação semântica da página.

[Documentação HTML](https://developer.mozilla.org/pt-BR/docs/Web/HTML)

#### CSS
&emsp;&emsp;Para o estilo visual da aplicação, o CSS foi utilizado para proporcionar uma aparência atrativa e garantir que a interface seja responsiva e adaptável a diferentes tamanhos de tela de desktop.

[Documentação CSS](https://developer.mozilla.org/pt-BR/docs/Web/CSS)

#### Vue.js 
&emsp;&emsp;Este framework progressivo foi escolhido para construir a interface do usuário de forma dinâmica, permitindo uma interatividade fluida e reativa aos inputs dos usuários, o que é essencial para as funcionalidades interativas da Coffee Break.

[Documentação Vye.Js](https://br.vuejs.org/v2/guide/index.html)

#### Nuxt.js
&emsp;&emsp;Baseado em Vue.js, o Nuxt.js é utilizado para otimizar a aplicação através do Server-Side Rendering (SSR), o que melhora significativamente o tempo de carregamento da página e a SEO, oferecendo uma melhor experiência ao usuário final e um desempenho aprimorado em navegadores de desktop.

[Documentação Nuxt.js](https://nuxt.com/docs/getting-started/introduction)

### Linguagem e Ferramentas para o Desenvolvimento de Banco de Dados:
----------------------------------------------------

#### SQL

&emsp;&emsp;SQL (Structured Query Language) é uma linguagem de programação utilizada para gerenciar e manipular bancos de dados relacionais. Oferece uma maneira padronizada de realizar tarefas como consultar dados, inserir registros, atualizar informações e criar estruturas de banco de dados.

### Principais Usos do SQL

- **Consulta de Dados:** SQL permite a recuperação de informações específicas de um banco de dados por meio de consultas, como o comando SELECT.

- **Manipulação de Dados:** Com SQL, é possível adicionar novos registros (INSERT), modificar dados existentes (UPDATE) e remover registros (DELETE).

- **Gerenciamento de Esquema:** SQL possibilita a criação, modificação e eliminação de estruturas de tabelas e seus relacionamentos por meio dos comandos CREATE, ALTER e DROP.

- **Controle de Acesso:** SQL oferece recursos para controlar o acesso aos dados no banco de dados, incluindo comandos como GRANT e REVOKE.

#### PostgreSQL

&emsp;&emsp;PostgreSQL é um sistema de gerenciamento de banco de dados relacional (RDBMS) open-source, conhecido por sua robustez, conformidade com padrões SQL e suporte a recursos avançados. É amplamente utilizado em aplicações web devido à sua confiabilidade e capacidade de escalabilidade.

### Principais Características do PostgreSQL

- **Banco de Dados Relacional:** Organiza os dados em tabelas que permitem relacionamentos entre elas.

- **Open Source:** PostgreSQL é distribuído sob uma licença de código aberto, permitindo seu uso, modificação e distribuição livremente.

- **Conformidade com Padrões:** Adere estritamente aos padrões SQL, garantindo alta compatibilidade com as linguagens de consulta SQL.

- **Recursos Avançados:** Inclui suporte para chaves estrangeiras, triggers, stored procedures, views e extensões.

- **Escalabilidade e Desempenho:** Conhecido por sua capacidade de gerenciar grandes volumes de dados e cargas de trabalho intensivas. Suporta replicação e clusterização para alta disponibilidade e escalabilidade.

- **Tipos de Dados Personalizados:** Permite a definição de tipos de dados customizados, atendendo a requisitos específicos.

- **Extensibilidade:** Possibilita a extensão de suas capacidades por meio de extensões e bibliotecas adicionais, facilitando a integração com outras tecnologias e oferecendo funcionalidades especializadas.

- **Suporte a Geolocalização e Dados Espaciais:** Oferece extensões para suporte a dados geográficos e espaciais, adequado para sistemas de informação geográfica (GIS).

[Documentação oficial do PostgreSQL](https://www.postgresql.org/docs/)

### Uso em Aplicações Web

&emsp;&emsp;O PostgreSQL é amplamente utilizado em aplicações web devido à sua confiabilidade e capacidade de escalabilidade. Ele é compatível com várias linguagens de programação através de drivers e bibliotecas, facilitando a integração com diversas plataformas de desenvolvimento.

## 6.5 Padrões de Trabalho

&emsp;&emsp;Os padrões de trabalho descritos a seguir visam estabelecer um conjunto de práticas comuns para o desenvolvimento do software, garantindo consistência, qualidade e eficiência em todo o projeto. Esses padrões incluem diretrizes para o código, commits, e a organização das branches, facilitando a colaboração entre desenvolvedores e mantendo o código organizado e fácil de manter. Além disso, eles promovem uma melhor integração e fluxo contínuo no pipeline de desenvolvimento, assegurando que as atualizações e as melhorias sejam implementadas de maneira suave e eficaz.

### Padrões de Código

#### Backend

- **Linguagem e Frameworks**: O desenvolvimento do backend é realizado em Python, com o framework Flask. Python foi escolhido por sua facilidade de uso, rica biblioteca de ferramentas para manipulação de dados, e por ser ideal para integração com sistemas de recomendação que utilizam bibliotecas como Pandas. Flask é escolhido por sua simplicidade e flexibilidade, facilitando um desenvolvimento rápido e eficiente.

- **Estrutura de Diretórios**:

  - `/src`: Diretório principal para o código fonte.
    - `/backend`: Contém os arquivos de backend.
      - `/bff_mobile`: Backend for frontend, específico para operações mobile.
      - `/ceos`: Módulo para funcionalidades relacionadas a CEOs.
      - `/common`: Módulo para funções comuns e utilitários.
      - `/projetos`: Módulo para gerenciamento de projetos.
      - `/recomendacao`: Módulo para o sistema de recomendação.
    - `/bi`: Módulo para funcionalidades de Business Intelligence.
    - `/tests`: Diretório para testes.

- **Padrão de Nomenclatura**:
  - **Variáveis e Funções**: Utilizamos snake_case para nomes de variáveis e funções, seguindo a convenção padrão do Python (ex: `usuario_id`, `get_ceo`).
  - **Classes e Objetos**: Nomes de classes iniciam com letra maiúscula e seguem o PascalCase (ex: `CeoService`).
  - **Arquivos**: Os nomes de arquivos refletem seu conteúdo e seguem o snake_case (ex: `ceo_service.py`).

### Padrões de Commit

- **Nomenclatura de Commits**:

  - Os commits devem começar com um tipo que descreve a natureza da mudança, seguido pela label da task relacionada ao commit, um dois-pontos e um espaço, e então uma breve descrição da mudança:
    - Exemplo: `feat(BACK): adiciona função para buscar CEOs`, `fix(login): corrige falha de autenticação`.
  - Tipos comuns incluem:
    - `feat`: Introduz um novo recurso.
    - `fix`: Corrige um bug.
    - `docs`: Documentação apenas, como atualizações no README.
    - `style`: Mudanças que não afetam o significado do código (espaços, formatação, etc.).
    - `refactor`: Refatoração de código existente que não corrige um bug nem adiciona um recurso.
    - `test`: Adicionando testes ausentes ou corrigindo testes existentes.

- **Organização de Branches**:

  - **main**: A branch principal onde reside o código estável e é usado para releases.
  - **develop**: Branch para desenvolvimento ativo, onde todas as features são integradas antes de serem promovidas para master.
  - **feature**: Prefixo usado para branches criadas para o desenvolvimento de funcionalidades específicas (ex: `feature/nova-autenticacao`).
  - **fix**: Usado para branches que focam na correção de bugs (ex: `fix/correcao-login`).
  - **bugfix**: Usada para correções de bugs pouco urgentes / críticos.
  - **docs**: Usada para documentação.

- **Processo de Desenvolvimento**:
  - Desenvolvimento de funcionalidades ocorre em branches separadas (`feature/`), criadas a partir de `develop`.
  - Após finalizar o desenvolvimento, a branch deve passar por uma revisão de código antes de ser mesclada em `develop`.
  - Quando a versão está pronta para ser lançada, `develop` é mesclada na `main` e uma nova tag de versão é criada.

#### Frontend

- **Linguagem e Frameworks**: O desenvolvimento do frontend é realizado em Dart, com o framework Flutter. Flutter foi escolhido pela sua facilidade de desenvolver aplicativos mobiles com interações dinâmicas e estilizadas. Além disso, a sua escritura se torna universal, sendo aceita em dispositivos IOS e Android.

- **Estrutura de Diretórios**:

  - `/src`: Diretório principal para o código fonte.
    - `/frontend`: Contém os arquivos de frontend.
      - `/.dart_tool`: Contém ferramentas e pacotes específicos necessários para o backend das operações mobile.
      - `/android`: Implementa funcionalidades específicas para CEOs dentro da plataforma Android.
      - `/assets`: Contém recursos comuns e utilitários que podem ser utilizados em todo o projeto.
      - `/build`: Gerencia processos de build e configuração do projeto.
      - `/ios`: Implementa o sistema de recomendação para a plataforma iOS.
      - `/lib`: Inclui funcionalidades específicas para CEOs que são comuns a diversas plataformas.
      - `/linux`: Fornece funções comuns e utilitários específicos para a plataforma Linux.
      - `/macos`: Gerencia processos e funcionalidades específicos para a plataforma macOS.
      - `/test`: Contém testes e implementações do sistema de recomendação.
      - `/web`: Implementa funcionalidades específicas para CEOs dentro da plataforma web.
      - `/windows`: Fornece funções comuns e utilitários específicos para a plataforma Windows.z'

- **Padrão de Nomenclatura**:
  - **Arquivos**: Utilizamos snake_case para nomes de arquivos, seguindo a convenção padrão do Dart (ex: `header_test.dart`, `text_field.dart`).
  - **Classes e Objetos**: Nomes de classes iniciam com letra maiúscula e seguem o PascalCase (ex: `CeoService`).
  - **Váriaveis e funções**: Os nomes das varíaveis e funções seguem o CamelCase (ex: `exemploVariavel`).

&emsp;&emsp;Esses padrões garantem que o desenvolvimento seja bem estruturado e organizado, facilitando tanto a manutenção quanto a colaboração entre múltiplos desenvolvedores.

# 7. Interface

&emsp;&emsp;Esta seção descreve o processo de concepção e desenvolvimento das interfaces de usuário para o projeto CoffeeBreak, uma iniciativa destinada à Fundação Dom Cabral (FDC). A interface de usuário (UI) é um elemento fundamental para proporcionar uma experiência agradável e eficaz aos usuários finais, simplificando o acesso e a interação com as funcionalidades do sistema. O design adotado enfatiza a clareza, a eficiência e a estética, visando criar uma solução que não apenas satisfaça as necessidades funcionais, mas que também seja visualmente atrativa e intuitiva. Os wireframes e mockups desempenham um papel vital nesse processo, fornecendo uma visualização preliminar da estrutura da interface antes da programação. Eles são utilizados para testar a usabilidade e para realizar ajustes conforme necessário. 

## 7.1 Projeto de Interface (Wireframes)

&emsp;&emsp;Um wireframe é uma representação visual básica e esquemática que serve como um plano preliminar para interfaces em desenvolvimento de software, websites e aplicativos móveis. Frequentemente comparado ao esboço arquitetônico de uma construção, ele é utilizado para estruturar a página ou tela, destacando os elementos-chave e a funcionalidade essencial sem se preocupar com os detalhes de design gráfico, como cores ou texturas. Este método facilita a visualização da distribuição espacial dos componentes da interface, permitindo ajustes estruturais antes do avanço para etapas mais detalhadas de design.

&emsp;&emsp;Para o desenvolvimento da solução destinada à Fundação Dom Cabral, será criado um wireframe de baixa fidelidade. Essa ferramenta será crucial para orientar e visualizar a concepção estrutural do projeto, especialmente para a versão mobile, enfocando nas funcionalidades essenciais que devem ser implementadas. O wireframe funcionará como um mapa preliminar, delineando a disposição dos elementos na interface e facilitando a interação do usuário com o sistema. Além disso, ele ajudará a equipe de desenvolvimento a identificar e resolver possíveis desafios de usabilidade e navegação no início do processo de design.

<div align="center">
  <sub>Figura 20 - Wireframes</sub>
  <img src="./assets/images/wireframe.png" width="100%" alt="Wireframe">
  <sup>Fonte: Os autores (2024)</sup>
</div>

&emsp;&emsp;Para o fluxo do CEO no app, o primeiro acesso é feito por meio do `Login`, sendo inserido o email e senha pessoais. Após a realização do login, a próxima tela visualizada é a `Home`, onde encontra-se a aba `Explorar`, com uma área para filtragem por `Temas`, os projetos `Recém adicionados` pelo usuário e uma timeline de projetos, `Com base no que você curtiu`. Em `Notícias`, aparecem as recomendadas e relacionadas aos temas dos projetos. Além disso, existe a `Header`, onde permite que o usuário navegue entre `Home`, `Pesquisa` e `Perfil`. Ao clicar em `Perfil`, o CEO é redirecionado para informações do próprio perfil, com nome, descrição, links das redes sociais, nome da empresa, aparecendo também a área de `Meus Projetos`, indicando os projetos criados pelo usuário e os projetos `Salvos` pelo mesmo.

<div align="center">
  <sub>Figura 21 - Wireframes</sub>
  <img src="./assets/images/wireframe2.png" width="100%" alt="Wireframe">
  <sup>Fonte: Os autores (2024)</sup>
</div>

&emsp;&emsp;Voltando para a `Home`, na área de `Recém adicionados`, aparecem uma lista de projetos criados recentemente pelo CEO. Na área de `Pesquisa`, ao buscar por algum tema em específico, aparecem projetos relacionados a ele. Na parte superior direita, existe o ícone de `Notificações`, onde se concentra todas as interações entre projetos, CEOs, como por exemplo as sinergias. Com isso, as `Solicitações de Sinergias` são apresentadas e, ao clicar em alguma, aparece a opção de aceitar ou recusar parceria. O wireframe mais detalhado do projeto em desenvolvimento, contendo todas as interações, funcionalidades e informações complementares, pode ser visualizado por meio da plataforma Figma, que consiste em um editor gráfico de vetor e prototipagem de projetos de design. Para acessá-lo, basta clicar [neste link](<https://www.figma.com/file/Xx3xcFOitGUQClVQiAqSPw/Style-Guidelines-(Community)?type=design&node-id=24%3A32&mode=design&t=hwmL1A6pJ6A7voWK-1>).

### 7.1.1. Guia de Estilos

&emsp;&emsp;Um guia de estilos é um documento ou conjunto de diretrizes que especifica as regras de design para a criação e manutenção da identidade visual, com o objetivo de manter a consistência de uma marca, produto ou publicação. Ele inclui orientações detalhadas sobre a utilização de logotipos, esquemas de cores, tipografias, layout, imagens e outros elementos visuais.Para desenvolver e definir o guia de estilos do projeto CoffeeBreak, foi utilizada a plataforma Figma. O Figma é um editor gráfico vetorial e uma ferramenta de prototipagem para projetos de design, o que facilitou significativamente a padronização visual da solução em desenvolvimento para a FDC. Alguns dos elementos estabelecidos no guia são apresentados nas imagens a seguir, começando pela capa:

<div align="center">
  <sub>Figura 22 - Capa</sub>
  <img src="./assets/images/capa.jpg" width="100%" alt="Capa">
  <sup>Fonte: Os autores (2024)</sup>
</div>

<div align="center">
  <sub>Figura 23 - Body</sub>
  <img src="./assets/images/body.png" width="100%" alt="Body">
  <sup>Fonte: Os autores (2024)</sup>
</div>

&emsp;&emsp;Para a tipografia do projeto, foi escolhida a fonte Satoshi, conhecida por seu estilo sóbrio e visualmente agradável, ideal para projetos com uma abordagem mais executiva e com uma estética minimalista. Além disso, essa fonte harmoniza-se perfeitamente com as cores e elementos selecionados para o guia de estilos. Essas características foram fundamentais para a escolha da tipografia Satoshi.

<div align="center">
  <sub>Figura 24 - Colors</sub>
  <img src="./assets/images/colors.png" width="100%" alt="Color">
  <sup>Fonte: Os autores (2024)</sup>
</div>

<div align="center">
  <sub>Figura 25 - Gridsystem</sub>
  <img src="./assets/images/gridsystem.png" width="100%" alt="Color">
  <sup>Fonte: Os autores (2024)</sup>
</div>

&emsp;&emsp;Baseando-se na identidade visual da ferramenta CEOs Legacy, da Fundação Dom Cabral, foi desenvolvido um padrão de cores que harmoniza com a proposta do grupo Spark. As cores selecionadas apresentam tons mais escuros, que se alinham perfeitamente à estética minimalista desejada, resultando em um apelo visual extremamente agradável. Para concluir, destaca-se os formatos em que a solução CoffeeBreak pode ser aplicada. Com base nos conceitos de "Progressive Enhancement" e "Mobile First", inicialmente a solução será desenvolvida para dispositivos móveis, ela também é compatível com tablets, e está sendo planejada para suportar uma versão desktop responsiva em futuras implementações. Todos esses elementos estão detalhados no [Guia de Estilos](<https://www.figma.com/file/Xx3xcFOitGUQClVQiAqSPw/Style-Guidelines-(Community)?type=design&node-id=24%3A32&mode=design&t=hwmL1A6pJ6A7voWK-1>) do projeto, disponível no Figma.

## 7.2 Mockup

&emsp;&emsp;Mockup é uma representação visual de alta fidelidade de um produto ou projeto, usado principalmente para demonstrar, testar ou promover um design antes de sua implementação final. Diferente de um esboço ou wireframe, que são mais focados em estrutura e layout, um mockup é mais detalhado e oferece uma visão mais próxima do produto final. Ele incorpora elementos de design, como cores, tipografias, imagens e outros detalhes visuais, permitindo que os stakeholders visualizem como o produto ou projeto vai parecer e funcionar no mundo real.

&emsp;&emsp;Ademais, com base no Wireframe de baixa fidelidade desenvolvido anteriormente, para estruturar visualmente e validar as funcionalidades necessárias para a solução, foi elaborado um Mockup completo, com a estilização padrão escolhida pelo grupo de acordo com o Guia de Estilos do projeto, que contém tipografia, paleta de cores e outros elementos essenciais para a implementação do sistema. Esse material foi extrememtente útil para a construção de alto nível do Mockup, permitindo assim apresentar uma proposta visual que visa se aproximar da solução final.

&emsp;&emsp;De acordo com a abordagem "Mobile First", para o desenvolvimento da solução para a FDC, o tamanho de tela voltado para sistema móvel, como smartphones e tablests, foi priorizado em relação a implementação, com o objetivo de facilitar o desenvolvimento e suprir a necessidade de proporcionar uma experiência de usuário eficiente e agradável em telas menores. Entretanto, após a otimação para essas plataformas, caso seja interessante, o design pode ser facilmente adaptado e expandido para acomodar telas maiores, como desktops.

<div align="center">
  <sub>Figura 26 - Mockup </sub>
  <img src="./assets/images/mockup-1.png" width="100%" alt="Mockup">
  <sup>Fonte: Os autores (2024)</sup>
</div>

&emsp;&emsp;Como apresentado nesta imagem acima, as funcionalidades elaboradas consistem em nas telas de `Login`, onde encontra-se labels para que o usuário insira seu acesso no aplicativo. Após a efetuação do login, destaca-se a tela de `Home` com aba de `Explorar`, com os projetos separados por temas e com base no interesse do usuário. Além disso, é possível acessar a aba de `Notícias` relacionadas aos assuntos dos projetos, a parte de `Peril` onde encontra-se imagem e descrição pessoais do CEOs, bem como a tela de projetos `Curtidos` e `Salvos` pelo mesmo.

<div align="center">
  <sub>Figura 27 - Mockup </sub>
  <img src="./assets/images/mockup-2.png" width="100%" alt="Mockup">
  <sup>Fonte: Os autores (2024)</sup>
</div>

&emsp;&emsp;Por sua vez, nessa imagem encontra-se selecionado um projeto e seu `Detalhamento`, seguido por uma indicação de possibilidade de `Sinergia`, sendo necessário sinalizar qual tipo seria dentre aprendizado, interação e unificação. Após essa tela, é apresentado uma caixa de texto para ser respondido o motivo pelo qual o CEO gostaria de fazer parceria com o projeto de outro CEO. Logo após o preenchimento dessa resposta, aparece um breve resumo para ser revisado e enviado como `Solicitação de Sinergia`. Em caso de confirmação, aparece uma tela indicando que a solicitação foi enviada.

<div align="center">
  <sub>Figura 28 - Mockup </sub>
  <img src="./assets/images/mockup-3.png" width="100%" alt="Mockup">
  <sup>Fonte: Os autores (2024)</sup>
</div>

&emsp;&emsp;Contudo, a imagem apresenta de início a tela de `Meus Projetos`, onde encontra-se todos os projetos criados e em sinergia pelo usuário. Ao clicar em `Adicionar Projeto`, o usuário é redirecionado para selecionar o `Macrotema`referente ao projeto em desenvolvimento e após isso, o `Subtema` do mesmo. Com essa etapa finalizada, o próximo passo consiste em definir um `Título` e `Descrição` para a proposta, assim será possível apresentá-la para outros usuários do aplicativo. Com todas as informações preenchidas, basta selecionar `Confirmar` e uma tela aparecerá indicando a criação do projeto.

&emsp;&emsp;Ademais, o [Mockup completo](<https://www.figma.com/design/Xx3xcFOitGUQClVQiAqSPw/Style-Guidelines-(Community)?node-id=878%3A503&t=Nmta9IyNTREwwCyi-1>) foi desenvolvido no Figma e aprimorado com um sistema avançado de navegabilidade, que permite testar as funcionalidades do sistema, com base numa simulação de fluxo do usuário em relação ao uso real do aplicativo mobile. Essa ferramenta, mesmo que apenas em um protótipo do Figma, permite que a equipe desenvolvedora possa analisar a navegabilidade do aplicativo, melhorando assim o entendimento para a estruturação do código e de como seria a experiência do usuário, validando assim a fluidez das ações sobre as funcionalidades apresentas.

&emsp;&emsp;Como pode ser visto, por meio do Wireframe, Guia de Estilo e funcionalidades necessárias para implementação, pôde ser possível estruturar um design de Mockup bem elaborado, eficiente e atraente para melhor experiência do usuário, contemplando os requisitos funcionais e não funcionais mapeados pela equipe na sessão 5 deste documento, com base nos apontamentos feitos pela Fundação Dom Cabral. Além disso, todas as ações presentes no sistema móvel foram baseadas de acordo com os casos de usos descritos na sessão 5.3, também elaborados pelos autores.

### Atualização Mockup Web

&emsp;&emsp;Agora, com o projeto solidamente estruturado sob a filosofia "Mobile First" e aprimorado meticulosamente, foi decido por essa abordagem inicialmente devido à crescente predominância do uso de dispositivos móveis entre os usuários finais. Isso garantiu que a solução fosse acessível e otimizada onde a maioria dos usuários realmente interage com a aplicação, priorizando a usabilidade e a performance em pequenas telas. Com essa base estabelecida, foi possível adaptar a aplicação para a tela de desktop, integrando todas as estratégias utilizadas anteriormente no desenvolvimento do mockup para dispositivos móveis. 

&emsp;&emsp;Essa adição para as telas maiores ocorreu apenas na fase final do projeto, permitindo que a equipe se concentrasse em entregar uma experiência móvel excepcional antes de escalar a solução para um ambiente de desktop. Como demonstrado na imagem abaixo, o sistema de login está harmoniosamente alinhado ao do aplicativo móvel, apresentando-se de maneira atraente, interativa e interessante, especialmente para os CEOs parceiros da FDC. A consistência visual e funcional entre as plataformas garante uma experiência fluida e integrada para todos os usuários.

<div align="center">
  <sub>Figura 29 - Mockup WEB </sub>
  <img src="./assets/images/login-web.png" width="100%" alt="Login WEB">
  <sup>Fonte: Os autores (2024)</sup>
</div>

&emsp;&emsp;Como pode ser observado, o dashboard da solução `Coffee Break` está extremamente fiel à versão do aplicativo móvel. Graças ao esforço colaborativo da equipe, foi possível apresentar esta solução à gestão da FDC de maneira útil e cativante para as telas de desktop. A imagem abaixo exibe o mockup da página `Home`, que mantém consistência visual em ambos os tamanhos de tela desenvolvidos. Adotamos uma abordagem minimalista com o objetivo de tornar a solução mais intuitiva e interativa, facilitando uma experiência de usuário superior. Esta estratégia incluiu o uso de elementos visuais simplificados e uma paleta de cores suave para promover um ambiente de trabalho mais agradável.

<div align="center">
  <sub>Figura 30 - Mockup WEB </sub>
  <img src="./assets/images/home-web.png" width="100%" alt="Login WEB">
  <sup>Fonte: Os autores (2024)</sup>
</div>

&emsp;&emsp;Com a base sólida criada pela adoção do "Mobile First", a adaptação para desktop não só manteve a coesão estética e funcional, mas também expandiu a usabilidade com a tela de "Macrotemas". Esta tela foi meticulosamente desenvolvida para destacar cada macrotema apresentado pela FDC, como "Bem-Estar, Saúde e Felicidade", entre outros. Cada tema é acompanhado de uma descrição detalhada dos projetos colaborativos entre os CEOs parceiros da Fundação Dom Cabral. Esses projetos de ESG incentivam que cada vez mais legados de CLevels sejam construídos e compartilhados na sociedade brasileira.

<div align="center">
  <sub>Figura 31 - Mockup WEB </sub>
  <img src="./assets/images/macrotema-web.png" width="100%" alt="Login WEB">
  <sup>Fonte: Os autores (2024)</sup>
</div>

&emsp;&emsp;Adicionalmente, por meio do link do mockup, disponibilizado ainda nessa seção do documento, que é acessível aos leitores, é possível explorar todas as telas desenvolvidas. Este recurso inclui um guia de estilos completo, que detalha o motivo do uso das cores padrões, tipografias, ícones e outros elementos visuais, garantindo que a identidade visual seja consistente em todas as plataformas e dispositivos. A integração desses elementos não só melhora a estética e a funcionalidade da aplicação, mas também reforça o objetivo da marca e da missão da FDC, proporcionando uma experiência rica e envolvente para todos os usuários.

## 7.3 Frontend

&emsp;&emsp;Frontend refere-se à parte de uma aplicação web ou móvel com a qual os usuários interagem diretamente. Ele abrange tudo o que é visível em um site ou aplicativo, como layouts de página, animações, interações do usuário e estilização. O desenvolvimento frontend é fundamental porque determina a acessibilidade, usabilidade e a experiência geral do usuário. Utilizar tecnologias modernas e práticas de design adequadas no frontend garante que a aplicação não só pareça atraente, mas também funcione de maneira eficiente e intuitiva em diferentes tamanhos de dispositivos e plataformas.

&emsp;&emsp;A criação de wireframes e mockups é uma etapa fundamental no processo de design. Um wireframe é um esboço simples que define a estrutura básica e os componentes de uma página, enquanto um mockup é uma representação mais detalhada e visualmente próxima do produto final, geralmente colorida e com elementos gráficos definitivos. Essas ferramentas são essenciais porque permitem visualizar e ajustar o design antes do desenvolvimento efetivo, economizando tempo e recursos. Além disso, ser fiel ao mockup durante o desenvolvimento assegura que o produto final esteja alinhado com as expectativas iniciais do projeto e dos stakeholders, mantendo a consistência visual e funcional conforme planejado.

&emsp;&emsp;No desenvolvimento do aplicativo CoffeeBreak para a Fundação Dom Cabral, inicialmente foi criado um wireframe de baixa fidelidade que serviu como um guia essencial para a elaboração do mockup. Esse [mockup](https://www.figma.com/design/Xx3xcFOitGUQClVQiAqSPw/Style-Guidelines?node-id=528-373&t=6Wo11DlcJm1ElMoQ-1), por sua vez, tem se mostrado fundamental no desenvolvimento do frontend, especialmente após os testes de usabilidade, que não apenas validaram as funcionalidades do sistema, mas também reforçaram a importância de seguir o design proposto para garantir uma experiência de usuário consistente e intuitiva, fiel ao escopo do projeto. Além disso, foi utilizado Mobile first, uma abordagem de design e desenvolvimento que prioriza a otimização de websites e aplicativos para dispositivos móveis antes de adaptá-los para desktops ou outros dispositivos.

&emsp;&emsp;Na seção 6.4 deste documento, estão listadas todas as tecnologias e ferramentas utilizadas no projeto. No entanto, para facilitar o entendimento, vale destacar que o grupo optou pelo uso do framework Flutter em conjunto com a linguagem Dart para o desenvolvimento do frontend. Essa decisão foi tomada por consenso entre os membros da equipe, visando o aprendizado e aproveitando a flexibilidade e eficiência reconhecidas dessas ferramentas, que são amplamente elogiadas por sua adaptabilidade e desempenho superior em projetos de desenvolvimento de interfaces de usuário.

<div align="center">
  <sub>Figura 32 - Comparação Mockup e Front </sub>
  <img src="./assets/images/frontend.png" width="100%" alt="Comparação Mockup e Front">
  <sup>Fonte: Os autores (2024)</sup>
</div>

&emsp;&emsp;Na imagem acima, pode-ser observar a evolução das primeiras telas do frontend do aplicativo CoffeeBreak, baseadas no mockup inicial. A primeira imagem mostra a tela de login atualmente desenvolvida, enquanto a segunda exibe o mockup original dessa mesma tela; o mesmo se aplica à tela de perfil do usuário. É notável a grande semelhança entre as telas desenvolvidas e seus respectivos mockups, o que destaca na prática a importância de um mockup bem elaborado e validado. Essa fidelidade ao design original assegura que o desenvolvimento esteja alinhado com a proposta apresentada ao nosso parceiro, a Fundação Dom Cabral, garantindo consistência e satisfação.

<div align="center">
  <sub>Figura 33 - Comparação Mockup e Front </sub>
  <img src="./assets/images/frontend-2.png" width="100%" alt="Comparação Mockup e Front">
  <sup>Fonte: Os autores (2024)</sup>
</div>

&emsp;&emsp;Na imagem acima, é evidente que o desenvolvimento do frontend continua fiel ao mockup original. Na primeira imagem, podemos ver como a tela de "Meus Projetos" está atualmente desenvolvida, enquanto a segunda mostra o mockup original dessa mesma tela; a mesma comparação se aplica à tela de "Projetos Curtidos" pelo usuário. Para facilitar a integração e o funcionamento completo do frontend, essas e outras telas estão sendo desenvolvidas modularmente em componentes. Essa abordagem não apenas otimiza o processo de desenvolvimento, mas também minimiza possíveis conflitos técnicos, assegurando uma implementação suave e eficiente.

<div align="center">
  <sub>Figura 34 - Atualização Front </sub>
  <img src="./assets/images/mudanca-front.png" width="100%" alt="Mudança Front">
  <sup>Fonte: Os autores (2024)</sup>
</div>

&emsp;&emsp;Na imagem acima, é possível observar algumas melhorias que foram inseridas no Mockup para serem implementadas para o frontend, com base nos resultados e avaliações dos testes de usabilidade. Essas melhorias são em relação a TabBar, para os ícones serem mais destacados e para os "Projetos indicados" serem "Projetos indicados para você". Além disso, foi alterado também a posição de "Adicionar Projetos". Outras melhorias estão sendo desenvolvidas, afim de apresentar uma solução atraente, intuitiva, com uma experiência de usuário ideial e interessante para o publico alvo da solução, que são CEOs parceiros da Fundação Dom Cabral.

<div align="center">
  <sub>Figura 35 - Frontend WEB </sub>
  <img src="./assets/images/frontend-web3.jpg" width="100%" alt="Comparação Mockup e Front">
  <sup>Fonte: Os autores (2024)</sup>
</div>

&emsp;&emsp;Para finalizar, foram desenvolvidas também, telas para tamanho desktop, que possibilitam o acesso via administração da Fundação Dom Cabral. Essa estrutura apresentada permite que a equipe de Gestão da FDC possa ter acesso aos perfis dos CEOs usuários do aplicativo, controle maior em relação aos projetos criados e sinergias entre eles, sendo uma visão mais complexa e bem detalhada, por meio de gráficos apresentados na área de dashboard. Devivo a abordagem de "Mobile First" foi possível concluir o desenvolvimento do aplicativo Coffee Break e trazê-lo também como plataforma web, um diferencial muito bem aproveitado e desenvolvido pela Grupo Spark.

<div align="center">
  <sub>Figura 36 - Frontend WEB </sub>
  <img src="./assets/images/frontend-web2.jpg" width="100%" alt="Comparação Mockup e Front">
  <sup>Fonte: Os autores (2024)</sup>
</div>

&emsp;&emsp;Ao longo deste projeto, foram enfrentadas algumas dificuldades, especialmente porque a maioria dos membros da equipe estavam lidando pela primeira vez com o framework Flutter e a linguagem Dart. No entanto, esse desafio tem sido estimulante e enriquecedor. Gradualmente, todos os integrantes estão aprimorando suas habilidades de programação e ampliando seus conhecimentos sobre essas ferramentas. Ver a aplicação ganhando vida,se aproximando do Wireframe e Mockup inicialmente desenvolvidos, especialmente após observar os resultados positivos dos testes de usabilidade, tem sido uma experiência verdadeiramente impressionante e motivadora.

## 7.4 Análise de Usabilidade do Frontend

&emsp;&emsp;A análise de usabilidade é uma etapa crucial no desenvolvimento de interfaces que priorizam a experiência do usuário. Nesta seção, serão exploradas a aplicação das heurísticas de usabilidade, a consideração da zona do polegar para dispositivos móveis e a acessibilidade geral da aplicação. Avaliaremos como o sistema foi desenhado para ser intuitivo, eficaz e acessível, garantindo que os usuários possam interagir com a plataforma de forma confortável e eficiente.

### 7.4.1 Utilização do Design System

&emsp;&emsp;Um design system é um conjunto de padrões, componentes e diretrizes de design que serve para garantir a consistência e a eficiência na criação de produtos digitais como websites, aplicativos e interfaces de usuário. Ele inclui elementos visuais (como tipografia, cores e ícones), componentes de interface de usuário (como botões, caixas de entrada e menus) e regras de usabilidade. Um design system é fundamental para que equipes de desenvolvimento e design trabalhem de maneira mais sincronizada, minimizando redundâncias e acelerando o processo de design e desenvolvimento ao fornecer um vocabulário comum e recursos reutilizáveis.

&emsp;&emsp;A importância de um design system se estende para além da mera padronização visual; ele desempenha um papel crucial na escalabilidade e na manutenção de projetos de software. Por exemplo, ao adotar um design system, uma empresa pode garantir que suas interfaces sejam acessíveis e proporcionem uma experiência de usuário consistente, independente do ponto de contato ou plataforma. Além disso, ele ajuda na colaboração entre equipes, pois permite que novos membros se integrem mais rapidamente aos projetos, e facilita a atualização ou a iteração de produtos existentes, uma vez que as mudanças podem ser implementadas de forma global e eficiente.

&emsp;&emsp;Criar um design system próprio é um investimento estratégico que pode trazer benefícios significativos para uma organização, como consolidar a identidade visual da marca, aumentar a eficiência operacional e melhorar a coesão entre os diferentes produtos e serviços oferecidos pela empresa. O processo começa com a compreensão das necessidades específicas do usuário e do contexto de negócios, seguido pela padronização de elementos de design e componentes de interface. Este sistema deve ser bem documentado, flexível e facilmente acessível para garantir sua adoção pelas equipes de desenvolvimento e design.

&emsp;&emsp;Para o desenvolvimento do aplicativo mobile `Coffee Break` foi criado do zero um Design System, intitulado como `Spark`, contendo todas as informações necessárias para manter uma estilização padrão, com paleta de cores, tipografia e outros critérios pensados cuidadosamente. O objetivo dessa criação é apresentar um resultado mais atraente e interativo diretamente para o perfil do público alvo do projeto, que são grandes CEOs parceiros da FDC. Criar o próprio Design System foi uma decisão da equipe, com o intuito de trazer um aplicativo próximo ao que foi idealizado por todos do grupo, permitindo assim identificar e construir uma estrutura personalizada, atendendo todos os requisitos do escopo, mas com uma identidade visual que promove uma ótima experiência ao usuário.

<div align="center">
  <sub>Figura 37 - Design System </sub>
  <img src="./assets/images/capa.jpg" width="100%" alt="Capa Design System">
  <sup>Fonte: Os autores (2024)</sup>
</div>

&emsp;&emsp;Entretanto, para o desenvolvimento do Design System Spark foi necessário analisar outros Design Systems já existentes no mercado e aproveitar pilares e detalhes de componentização. Como citado na seção X deste documento, algumas identidades visuais de aplicativos foram utilizados como inspirações para a estruturação do Wireframe e Mockup do Coffee Break, dentre ele estão o Design System da Uber [Base](https://base.uber.com/6d2425e9f/p/294ab4-base-design-system), o Design System do [Instagram](https://about.instagram.com/brand) e o Design System do [Spotify](https://spotify.design/article/reimagining-design-systems-at-spotify). Cada inspiração citada foi essencial para construir funcionalidades do sistema com base na identidade visual desejada pela equipe.

<div align="center">
  <sub>Figura 338 - Design System Spotify </sub>
  <img src="./assets/images/spotify.jpg" width="100%" alt="Design System Spotify">
  <sup>Fonte: Os autores (2024)</sup>
</div>

&emsp;&emsp;A imagem acima representa a tela de busca do aplicativo do `Spotify`. Essa tela e esses componentes de playlists foram de extrema importância para o desenvolvimento da solução `Coffee Break`, pois serviu de inspiração para a parte de `Macrotemas` e `Subtemas` do aplicativo. Além disso, a identidade visual do Spotify trasmite modernidade, transmitindo uma experiência artística imersiva, com cores extramente atraentes e divertidas. Essa estratégia de formatos e cores também foi aplicado na solução Coffee Break, com o intuito de aproximar mais o usuário ao app, incentivando cada vez mais o uso do sistema, de forma interativa e mais casual.

<div align="center">
  <sub>Figura 39 - Design System Uber </sub>
  <img src="./assets/images/uber.png" width="100%" alt="Design System Uber">
  <sup>Fonte: Os autores (2024)</sup>
</div>

&emsp;&emsp;Já a plataforma da `Uber` serviu de inspiração por ser um aplicativo cotidiano, ou seja, bastante utilizado diariamente pelos seus usuários. Isso indica que as abordagens presentes no app são voltadas para a intuitividade e interação direta com o passageiro, criando assim uma conexão emocional com os usuários. Além disso, o aplicativo da Uber possui uma identidade visual mais destacada para o minimalismo, com tons neutros, como preto e branco, que significa eliminar elementos desnecessários e apenas manter o que é indispensável para o funcionamento do sistema. Todas essas estratégias foram identificadas e consideradas relevantes para aplicar no sistema do `Coffee Break`.

<div align="center">
  <sub>Figura 40 - Design System Instagram </sub>
  <img src="./assets/images/instagram.jpg" width="100%" alt="Design System Instagram">
  <sup>Fonte: Os autores (2024)</sup>
</div>

&emsp;&emsp;Como última inspiração e dessa vez sendo uma rede social, o `Instagram` também foi utilizado para a construção do aplicativo `Coffee Break`. Essa rede social foi selecionada para ajudar na construção do sistema, pois trata-se de uma rede muito utilizada mundialmente, que transmite conteúdos para seus usuários, inclusive criados por eles, de forma fácil, intuitiva e interativa. O Instagram também possui um sistema de recomendação muito interessante, essencial para o entendimento e implementação na solução em desenvolvimento. Com suas funcionalidades voltadas para conversas e trocas de conteúdos, essa plataforma se mostrou muito útil para guiar todo o grupo na implementação da estrutura do `Coffee Break`.

&emsp;&emsp;Ademais, para complementar a criação do Design System, foi necessário criar um Guia de Estilos personalizado para o projeto. Com isso, o resultado apresentado nas imagens abaixo é uma paleta de cores com tons atraentes, que transmitem uma sensação minimalista e executiva, sendo dispostos aos temas "Claro" e "Escuro" do dispositivo celular. Além disso, apresenta-se também a tipografia padrão utilizada, que consiste em um formato mais executivo e moderno. Para mais detalhes, na seção 7.1.1 deste documento, encontra-se a descrição completa sobre o Guia de Estilos desenvolvido para esse Design System, com essas e outras imagens relacionadas à identidade visual do aplicativo `Coffee Break`.

<div align="center">
  <sub>Figura 41 - Paleta de Cores </sub>
  <img src="./assets/images/color.png" width="100%" alt="Paleta de Cores">
  <sup>Fonte: Os autores (2024)</sup>
</div>

<div align="center">
  <sub>Figura 42 - Tipografia </sub>
  <img src="./assets/images/body.png" width="100%" alt="Tipografia">
  <sup>Fonte: Os autores (2024)</sup>
</div>

&emsp;&emsp;Agora, na imagem abaixo, é possível visualizar o resultado atualizado do desenvolvimento do frontend do `Coffee Break`, com base nas inspirações utilizadas e implementadas no Wireframe e Mockup desenvolvidos. Pode-se identificar muitas similaridades com todas essas plataformas citadas anteriormente, contemplando estratégias e abordagens de UI/UX reconhecidas e valorizadas pela equipe, afim de apresentar uma solução extremamente atraente, interessante para o usuário, que fosse intuitiva, de fácil uso, e muito interativa, instigando o uso frequente do aplicativo. A aplicação foi desenvolvida em dois temas, sendo eles claro e escuro, permitindo assim maior personalização para o usuário.

<div align="center">
  <sub>Figura 43 - Frontend Modo Claro </sub>
  <img src="./assets/images/frontend-claro.png" width="100%" alt="Frontend Modo Claro">
  <sup>Fonte: Os autores (2024)</sup>
</div>

<div align="center">
  <sub>Figura 44 - Frontend Modo Claro </sub>
  <img src="./assets/images/frontend-escuro.png" width="100%" alt="Frontend Modo Claro">
  <sup>Fonte: Os autores (2024)</sup>
</div>

&emsp;&emsp;Portanto, vale ressaltar que para o desenvolvimento de uma sistema, utilizar um existente ou criar um Design System é fundamental para definir direcionamentos visuais padrões para o frontend, orientados para as funcionalidades, proporcionando assim uma ótima experiência de usuário. O aplicativo `Coffee Break` está sendo desenvolvido com base em estratégias e abordagens que visam seguir o escopo do projeto, mas também trazer como diferencial uma solução bastante cativante e intuitiva, facilitando e incentivando o uso para todos os CEOS parceiros da Fundação Dom Cabral, que serão os usuários fidedignos do sistema!

### 7.4.2 Heurísticas de Nielsen

&emsp;&emsp;As Heurísticas de Nielsen, desenvolvidas pelo renomado especialista em usabilidade Jakob Nielsen, representam um conjunto de dez diretrizes projetadas para melhorar a qualidade da interação do usuário com interfaces. Estas heurísticas são amplamente reconhecidas como um framework eficaz para diagnosticar problemas de usabilidade e garantir que os sistemas sejam intuitivos e acessíveis. A adesão a esses princípios é crucial para evitar problemas comuns no design de interface, como complexidade desnecessária, inconsistência, feedback inadequado e dificuldade de recuperação de erros. No projeto CoffeeBreak, várias dessas heurísticas foram priorizadas para assegurar uma experiência de usuário otimizada. A implementação focou em simplificar a interface, manter a consistência e fornecer feedback imediato e claro, facilitando a navegação e interação com o sistema. As heurísticas específicas abordadas incluem:

#### Visibilidade do status do sistema

&emsp;&emsp;Foi garantido que o sistema sempre mantém os usuários informados sobre o que está acontecendo, através de feedback adequado dentro de um tempo razoável. Por exemplo, em todas as telas que são alcançadas através do clique de um botão, há o nome dessa tela e a seta para voltar, indicando que há uma saída. Além disso, após ações como criação de projeto ou solicitação de sinergia, telas de confirmação são exibidas para indicar sucesso.

<div align="center">
  <sub>Figura 45 - Status </sub>
  <img src="./assets/images/status-sistema.png" width="100%" alt="Status">
  <sup>Fonte: Os autores (2024)</sup>
</div>

#### Compatibilidade entre o sistema e o mundo real

&emsp;&emsp;Os ícones e símbolos usados são baseados em convenções universais ou são facilmente compreensíveis, garantindo que os usuários não precisem aprender novos significados. Ícones como sinos para notificações e lápis para editar são utilizados para alinhar a interface com as expectativas e experiências do usuário no mundo real. Ademais, os ícones e toda a construção da barra de navegação foram inspirados nas barras de navegação do Instagram e Spotify, justamente para diminuir o tempo de raciocínio e aprendizado, por se tratarem de redes sociais amplamente utilizadas e conhecidas.

<div align="center">
  <sub>Figura 46 - Compatibilidade </sub>
  <img src="./assets/images/icones.png" width="100%" alt="Compatibilidade">
  <sup>Fonte: Os autores (2024)</sup>
</div>

#### Controle e liberdade do usuário

&emsp;&emsp;Os usuários têm a flexibilidade de desfazer e refazer ações sem dificuldade. Isso inclui a edição de informações pessoais e de projetos, proporcionando uma experiência de usuário sem frustrações e com total controle sobre suas interações. Essa função de edição pode ser facilmente acessada, através do clique no ícone de lápis.

<div align="center">
  <sub>Figura 47 - Edição </sub>
  <img src="./assets/images/editar.png" width="100%" alt="Edição">
  <sup>Fonte: Os autores (2024)</sup>
</div>

#### Consistência e padrões

&emsp;&emsp;O design mantém uma uniformidade estética e funcional em todas as telas. Utilizou-se um sistema de design consolidado que padroniza componentes como botões, tipografias e cores, assegurando uma experiência coesa em todo o aplicativo.

<div align="center">
  <sub>Figura 48 - Consistência </sub>
  <img src="./assets/images/consistencia.png" width="100%" alt="Consistência">
  <sup>Fonte: Os autores (2024)</sup>
</div>

#### Prevenção de erros

&emsp;&emsp;Algumas estratégias foram implementadas para prevenir erros antes que eles ocorram, com a utilização de confirmações antes de ações críticas e revisões finais antes de submissões importantes, como o envio de uma solicitação de sinergia e criação de um novo projeto. Erros e enganos na execução de ações importantes podem ser muito comuns, por isso telas de confirmação exercem um papel fundamental no que diz respeito a prevenção de erros.

<div align="center">
  <sub>Figura 49 - Prevenção </sub>
  <img src="./assets/images/prevencao.PNG" width="100%" alt="Prevenção">
  <sup>Fonte: Os autores (2024)</sup>
</div>

#### Reconhecimento em vez de memorização

&emsp;&emsp;Os elementos de interface são projetados para serem memoráveis, não requerendo que os usuários se lembrem de informações de uma tela para outra. Isso é particularmente evidente na diferenciação visual dos macrotemas, que utilizam cores e ícones específicos. Dessa forma, a diferenciação dos cards de projeto em todo o aplicativo se torna algo muito mais intuitivo a medida que o usuário se estabelece na pltaforma.

<div align="center">
  <sub>Figura 50- Reconhecimento </sub>
  <img src="./assets/images/reconhecimento.png" width="100%" alt="Reconhecimento">
  <sup>Fonte: Os autores (2024)</sup>
</div>

&emsp;&emsp;A aplicação das Heurísticas de Nielsen no desenvolvimento do CoffeeBreak visa proporcionar uma experiência de usuário que não apenas atende, mas excede as expectativas padrão de usabilidade. Ao adotar esses princípios, o projeto assegura uma interface amigável, eficiente e acessível, reduzindo a curva de aprendizado e aumentando a satisfação do usuário. As estratégias implementadas em garantem uma solução que não apenas funciona bem, mas também é agradável e intuitiva de usar.

### 7.4.3 Zona do Polegar

&emsp;&emsp;A "zona do polegar", ou "thumb zone", é um conceito crucial no design de interfaces móveis que se refere às áreas da tela de um dispositivo que são facilmente alcançáveis pelo polegar do usuário enquanto seguram o dispositivo com uma só mão. Este conceito é fundamental, pois a ergonomia de um aplicativo pode significativamente impactar a usabilidade e a experiência do usuário. Projetar uma interface que se enquadra predominantemente dentro desta zona pode garantir que o aplicativo seja mais confortável de usar, reduzindo o esforço físico e aumentando a eficiência da interação.

#### Importância

&emsp;&emsp;A importância de considerar a zona do polegar no design de aplicativos móveis reside na crescente prevalência do uso de smartphones em diversas atividades diárias. Uma interface que exige que o usuário estique demais o polegar ou use as duas mãos para operar pode levar a uma experiência frustrante ou desconfortável. Portanto, o design que se adapta à ergonomia natural das mãos dos usuários não só melhora a acessibilidade e a experiência do usuário, mas também pode prevenir fadiga e desconforto durante usos prolongados.

&emsp;&emsp;Basicamente, a Zona do Polegar conta com três regiões específicas:

- **Verde:** área fácil de alcançar com o polegar
- **Amarela:** área intermediária
- **Vermelha:** área difícil de alcançar

<div align="center">
  <sub>Figura 51 - Zona do Polegar </sub>
  <img src="./assets/images/zona-do-polegar.png" width="100%" alt="Zona do Polegar">
  <sup>Fonte: E-Commerce Brasil</sup>
</div>

#### Implementação da Zona do Polegar

&emsp;&emsp;A disposição dos elementos de interface foi meticulosamente planejada para se alinhar com a Zona do Polegar. Isto foi realizado através de um design estratégico que coloca todos os elementos interativos chave dentro do alcance fácil do polegar. A barra de navegação, que inclui os ícones mais frequentemente utilizados como Home, Pesquisa, e Perfil, está localizada na parte inferior da tela, permitindo fácil acesso sem necessidade de reajustar a pegada do dispositivo.

<div align="center">
  <sub>Figura 52 - Zona do Polegar Coffeebreak </sub>
  <img src="./assets/images/zona-app.png" width="100%" alt="Zona do Polegar">
  <sup>Fonte: Os autores (2024)</sup>
</div>

&emsp;&emsp;Além disso, funções críticas como 'like', 'save', e 'edit' em projetos são colocadas de maneira que os usuários possam alcançá-las confortavelmente com o polegar. Isso assegura que a interação com o aplicativo seja fluida e intuitiva, contribuindo para uma experiência de usuário mais agradável e eficiente.

&emsp;&emsp;A atenção à Zona do Polegar durante o design do CoffeeBreak demonstra um compromisso em criar uma interface que não só atende às necessidades funcionais dos usuários, mas também respeita as limitações físicas e promove uma experiência de usuário ótima. A implementação cuidadosa desta prática de design é um testemunho do foco da equipe no usuário final, garantindo que o aplicativo seja acessível, fácil de usar e esteticamente agradável. Ao centrar-se na usabilidade e conforto, o app estabelece-se como um exemplo de como o design considerado pode melhorar significativamente a interação do usuário com a tecnologia móvel.

### 7.4.4 Acessibilidade

&emsp;&emsp;A acessibilidade em dispositivos móveis é fundamental para garantir que todas as pessoas, independentemente de suas habilidades físicas, visuais ou cognitivas, possam usar aplicativos eficientemente. Além de incluir usuários com deficiências, a acessibilidade abrange suportar variados níveis de letramento digital, facilitando o uso do aplicativo em diferentes contextos e por usuários com diversas necessidades. A implementação de práticas de acessibilidade não se destina apenas a pessoas com deficiência, mas visa a inclusão de todos, independentemente das habilidades individuais. Isso inclui o suporte para diferentes níveis de habilidade digital e outras necessidades que podem não ser imediatamente óbvias.

&emsp;&emsp;Neste projeto, foram priorizados dois principais aspectos de acessibilidade: a implementação de `Semantics` para leitores de tela e a disponibilização de temas de cores claros e escuros. Essas estratégias visam não apenas melhorar a usabilidade mas também promover a inclusão através de uma interface adaptável e compreensível por todos. Ao incorporar `Semantics` e temas ajustáveis, busca-se facilitar o uso do aplicativo sob diversas condições de visibilidade e compreensão.

#### Semantics

&emsp;&emsp;O widget `Semantics` do Flutter é crucial para melhorar a acessibilidade, permitindo aos desenvolvedores anotar a árvore de widgets com descrições para tecnologias assistivas. Esse widget foi implementado em todos os nossos componentes, sem exceção. Aqui estão alguns exemplos de sua aplicação:

<div align="center">
  <sub>Figura 53 - Categoria </sub>
  <img src="./assets/images/category.jpeg" width="100%" alt="Categoria">
  <sup>Fonte: Os autores (2024)</sup>
</div>

- **Category**: Incorpora-se `Semantics` para descrever as categorias dos projetos, ajudando usuários de leitores de tela a compreender o contexto sem necessidade de visualização.

<div align="center">
  <sub>Figura 54 - Cabeçalho </sub>
  <img src="./assets/images/header.jpeg" width="100%" alt="Cabeçalho">
  <sup>Fonte: Os autores (2024)</sup>
</div>
  
- **Header**: No cabeçalho, utiliza-se `Semantics` para ressaltar informações críticas da interface, como títulos e botões de navegação, facilitando a orientação de usuários com deficiência visual.

<div align="center">
  <sub>Figura 55 - Ícones </sub>
  <img src="./assets/images/icons.jpeg" width="100%" alt="Ícones">
  <sup>Fonte: Os autores (2024)</sup>
</div>

- **Icons**: Cada ícone interativo é envolto em `Semantics`, com descrições claras sobre sua função, garantindo que todos possam navegar com igualdade de condições.

#### Temas

&emsp;&emsp;A opção de escolher entre temas claros e escuros atende às necessidades de usuários com sensibilidade à luz e preferências de contraste, o que é essencial para a acessibilidade. A mudança de tema pode reduzir a fadiga ocular e melhorar a legibilidade, tornando a experiência do usuário mais confortável e personalizada.

<div align="center">
  <sub>Figura 56 - Temas </sub>
  <img src="./assets/images/themes.jpeg" width="100%" alt="Temas">
  <sup>Fonte: Os autores (2024)</sup>
</div>

&emsp;&emsp;Portanto, a acessibilidade do projeto não só cumpre com normas regulatórias mas também abraça a diversidade dos usuários, oferecendo uma experiência mais inclusiva e equitativa. Através destas práticas, aspira-se criar um ambiente digital acessível a todos, reforçando o compromisso com a inclusão e a igualdade de acesso a tecnologias.

# 8. Projeto de Banco de Dados

&emsp;&emsp;Um projeto de banco de dados é uma iniciativa fundamental na gestão e organização de dados para empresas e organizações de todos os tamanhos. A criação de um banco de dados bem estruturado não só facilita o armazenamento e a recuperação eficiente de informações, mas também apoia as operações de negócios, a tomada de decisões e a análise estratégica. Ao planejar um projeto de banco de dados, vários aspectos devem ser considerados para assegurar que o sistema final seja robusto, seguro e adaptável às necessidades em constante evolução da organização. Portanto, segue abaixo as especificidades do banco de dados da solução `Coffee Break`.

## 8.1 Especificação da Base de Dados para Modelo de Recomendação

&emsp;&emsp;Este tópico tem como objetivo explicar e detalhar os motivos das escolhas realizadas pelo grupo Spark em relação ao tratamento inicial do arquivo CSV e planejamento completo para melhor implementação do modelo de recomendação no sistema do aplicatico `Coffee Break`:

### **Arquivo CSV (Base de dados):**

&emsp;&emsp;Foram enviados um arquivo CSV com três planilhas internas para a preparação dos dados do modelo de recomendação. Inicialmente, foram realizadas análises estatísticas, incluindo desvio padrão, média, moda, identificação de dados nulos e outliers. Após esse tratamento inicial, realizamos um merge entre essas três tabelas e iniciamos a análise para obter um balanceamento adequado.

&emsp;&emsp;Após estas análises, a base de dados possui 9101 linhas e 19 colunas, incluindo: `projeto_id`, `projeto_nome`, `projeto_setor`, `projeto_macrossetor`, `projeto_impacto`, `projeto_status`, `projeto_alcance-geografico`, `projeto_publico-alvo`, `proponente_id`, `proponente_nome`, `proponente_empresa`, `proponente_atuacao`, `proponente_cargo`, `avaliador_id`, `avaliador_nome`, `avaliador_empresa`, `avaliador_atuacao`, `avaliador_cargo` e `avaliacao`.

### **Balanceamento dos dados e Modelo de recomendação:**

&emsp;&emsp;Após análise da base de dados, foi identificada uma discrepância nos dados de avaliação que seriam utilizados para o modelo de recomendação dos projetos. Em vez de optar pelo balanceamento tradicional para evitar viés no modelo de recomendação, decidimos manter o desbalanceamento, pois essa variável não é crítica para a modelagem proposta. Alterar essa variável poderia resultar na perda de precisão e qualidade do modelo de recomendação. Para o modelo de recomendação, será considerado o seguinte planejamento: quando um CEO entrar na plataforma com seu novo perfil e projeto, o modelo de recomendação trabalhará com métricas divididas em **Modelo de Recomendação por Conteúdo (MRC)** e **Modelo de Recomendação Colaborativa (MRCL)**. 

&emsp;&emsp;Um novo perfil na plataforma, sem atividades anteriores, será submetido apenas ao MRC, levando em consideração principalmente o tema e subtema do projeto. Após a primeira interação do CEO na plataforma, como curtir outro projeto, ambos os modelos serão ativados (MRC e MRCL), com suas métricas e pesos combinados. Isso resultará em recomendações que correspondam tanto ao perfil do CEO quanto ao projeto do CEO. Além disso, como forma de enriquecer o modelo e proporcionar novas experiências aos usuários, o modelo de recomendação fornecerá conteúdos exclusivos que não se encaixam diretamente no perfil do usuário ou nos projetos do CEO. O objetivo é promover novas experiências e despertar novas oportunidades para os usuários.

### Descrição da Base de Dados

&emsp;&emsp;A seguir, é apresentado uma descrição da base de dados utilizada para o modelo de recomendação:

```py
 #   Column                      Non-Null Count  Dtype
---  ------                      --------------  -----
 0   projeto_id                  9101 non-null   int64
 1   projeto_nome                9101 non-null   object
 2   projeto_setor               9101 non-null   object
 3   projeto_macrossetor         9101 non-null   object
 4   projeto_impacto             9101 non-null   object
 5   projeto_status              9101 non-null   object
 6   projeto_alcance-geografico  9101 non-null   object
 7   projeto_publico-alvo        9101 non-null   object
 8   proponente_id               9101 non-null   int64
 9   proponente_nome             9101 non-null   object
 10  proponente_empresa          9101 non-null   object
 11  proponente_atuacao          9101 non-null   object
 12  proponente_cargo            9101 non-null   object
 13  avaliador_id                9101 non-null   int64
 14  avaliador_nome              9101 non-null   object
 15  avaliador_empresa           9101 non-null   object
 16  avaliador_atuacao           9101 non-null   object
 17  avaliador_cargo             9101 non-null   object
 18  avaliacao                   9101 non-null   int64
dtypes: int64(4), object(15)
```

&emsp;&emsp;Conforme demonstrado acima, a base de dados utilizada para o modelo de recomendação é composta por 9101 linhas e 19 colunas (separadas entre colunas numéricas e colunas categóricas), contendo informações sobre os projetos, proponentes, avaliadores e avaliações. Esses dados serão utilizados para a construção do modelo de recomendação, que será implementado na plataforma Coffee Break.

&emsp;&emsp;As colunas estão nomeadas de forma a facilitar a identificação e compreensão dos dados, sendo que cada coluna representa uma variável específica, como o identificador do projeto, o nome do projeto, o setor do projeto, o impacto do projeto, o status do projeto, o alcance geográfico do projeto, o público-alvo do projeto, o identificador do proponente, o nome do proponente, a empresa do proponente, a atuação do proponente, o cargo do proponente, o identificador do avaliador, o nome do avaliador, a empresa do avaliador, a atuação do avaliador, o cargo do avaliador e a avaliação do projeto. Por fim, a base processada está localizada no arquivo `base-de-dados-mesclada.csv`, dentro de `src/bi/data/processed`. A base original, por sua vez, está localizada em `src/bi/data/raw`, no arquivo `base-de-dados.xlsx`.

## 8.2 Modelo Conceitual

&emsp;&emsp;Um modelo conceitual em um banco de dados relacional representa uma visão de alto nível da estrutura organizacional e dos relacionamentos entre as entidades e seus atributos. Esse modelo descreve os tipos de dados que serão armazenados e como eles se inter-relacionam, porém sem mergulhar nos detalhes técnicos de como esses dados serão efetivamente manipulados. Essa abordagem simplificada torna o modelo altamente acessível e compreensível, o que é essencial para assegurar uma compreensão clara e facilitar o desenvolvimento da solução.

&emsp;&emsp;Para o sucesso deste projeto, o Modelo Conceitual desempenha um papel fundamental ao representar todas as entidades, seus atributos e os relacionamentos entre os serviços. Este modelo oferece uma perspectiva detalhada da estrutura e da lógica direcionada à solução mobile, proporcionando uma base sólida para análise. Através dele, a implementação das funcionalidades propostas se torna mais eficiente, assegurando uma integração sistemática e funcional. Abaixo, apresenta-se o diagrama do Modelo Conceitual especialmente desenvolvido para este projeto:

<div align="center">
  <sub>Figura 57 - Modelo Conceitual</sub>
  <img src="./assets/images/modelo-conceitual.jpg" width="100%" alt="Modelo Conceitual">
  <sup>Fonte: Os autores (2024)</sup>
</div>

&emsp;&emsp;No modelo conceitual proposto, a entidade **CEO** ocupa uma posição central e interage com diversas outras entidades. Através de informações como `nome`, `email`, `senha`, `cargo`, entre outros, e relacionamentos como receber **Notificações**, **Recomendações**, **Projetos**, e **Atualizações**, o modelo detalha a organização e funcionamento das interações entre as entidades, atributos e relações de cardinalidade, permitindo assim que as funcionalidades relacionadas aos serviços sejam executadas da melhor maneira possível.

&emsp;&emsp;A entidade **Projeto**, diretamente vinculada ao CEO, ilustra como iniciativas específicas são estruturadas e monitoradas, com cada projeto podendo incluir **Macrotemas** e **Subtemas**, estando sujeito a **Interações** e **Atualizações** que documentam o progresso e o engajamento com os stakeholders. Essa inter-relação é fundamental para manter uma visão clara do estado e evolução dos projetos, facilitando o desenvolvimento e acompanhamento dos projetos em sinergia, tanto pelos CEOs, como também para a Fundação.

&emsp;&emsp;O uso de **Subtemas** e **Macrotremas** permite uma categorização eficiente dos projetos. Essa organização melhora significativamente a navegação e a apresentação de informações relevantes, sendo essencial para uma experiência de usuário otimizada em dispositivos móveis. Integrando essas entidades de maneira estruturada, o modelo conceitual facilita não apenas a compreensão da estrutura conceitual do sistema, mas também auxília em uma solução bem mais robusta e focada em colaborar para mais legados serem contruídos, o que é o objetivo principal dessa proposta da FDC.

## 8.3 Modelo Lógico

&emsp;&emsp;O modelo lógico de um banco de dados é uma etapa crucial no processo de design de banco de dados, servindo como a ponte entre o modelo conceitual abstrato e o modelo físico que será implementado no sistema de gerenciamento de banco de dados. Esse modelo é importante por proporcionar uma representação mais concreta de como os dados serão organizados, incluindo as estruturas de tabelas e suas relações, atributos, tipos de dados... Neste modelo, baseado no Conceitual, é retratado o banco de dados de forma mais alinhada com a visão do sistema de gerenciamento de banco de dados. Nele, as entidades conceituais são transformadas em tabelas, cada uma com suas chaves primárias próprias. Essas tabelas têm relacionamentos entre si e podem conter chaves estrangeiras. Além disso, os tipos de dados são definidos para cada coluna, como inteiro, string, data, entre outros.

<div align="center">
  <sub>Figura 58 - Modelo Lógico</sub>
   <img src='./assets/images/modelo-logico.jpeg' width="100%" alt='Modelo lógico'>
  <sup>Fonte: Os autores (2024)</sup>
</div>

### Relação entre as tabelas

&emsp;&emsp;Sobre as relações entre tabelas, dentro de um modelo lógico de banco de dados, a chave estrangeira (foreign key) desempenha um papel fundamental ao conectar diferentes tabelas. Essa chave é composta por uma coluna ou conjunto de colunas em uma tabela, estabelecendo uma relação referencial com uma chave primária ou única em outra tabela. Essa conexão é essencial para manter a integridade referencial dos dados compartilhados entre as tabelas. Segue abaixo uma tabela com mais informações referentes a essas relações do modelo lógico:

<div align="center">
  <sub>Quadro X - Relações de Tabelas Modelo Lógico</sub>
	
| **Tabela**   | **Atributo(s)**                                                                                              |
| ------------ | ------------------------------------------------------------------------------------------------------------ |
| Notificação  | **ceo_id:** Identificador do CEO destinatário.                                                               |
| Atualização  | **ceo_id:** Identificador do CEO que atualizou;<br>**projeto_id:** Identificador do projeto atualizado.      |
| Recomendação | **ceo_id:** Identificador do CEO destinatário;<br>**projeto_id:** Identificador do projeto recomendado.      |
| Interação    | **ceo_id:** Identificador do CEO que interagiu;<br>**projeto_id:** Identificador do projeto interagido.      |
| Projeto      | **ceo_id:** Identificador do CEO criador do projeto;<br>**subtema_id:** Identificador do subtema do projeto. |
| Subtema      | **macrotema_id:** Identificador do macrotema. |

<sup>Fonte: Os autores (2024)</sup>
</div>

# 9. Construção da Solução

&emsp;&emsp;O projeto "Coffee Break" para a FDC, teve como foco construir uma solução robusta que integra um modelo de recomendação avançado para personalizar a experiência do usuário. Este modelo analisa as interações e preferências passadas para fornecer sugestões precisas e relevantes. A aplicação, desenvolvida com a abordagem "Mobile First", é otimizada para dispositivos móveis antes de ser adaptada para desktops, garantindo consistência e eficiência em todas as plataformas. O projeto utiliza tecnologias como Flutter, Flask, entre outros para suportar uma estrutura flexível e escalável, capaz de se adaptar às necessidades dinâmicas da FDC e de seus parceiros.

## 9.1 Modelo de Recomendação

&emsp;&emsp;Um modelo de recomendação é uma ferramenta extremamente útil que analisa dados para prever as preferências dos usuários e sugerir itens que possam ser de seu interesse. No contexto da solução "Coffee Break", este modelo é essencial para personalizar a experiência dos CEOs ao utilizarem o aplicativo pela primeira vez. Inicialmente, o modelo recomenda projetos de maneira aleatória, sobre vários macrotemas e subtemas, para oferecer uma variedade de opções e coletar dados iniciais sobre as preferências dos usuários, ou seja, CEOs parceiros da Fundação Dom Cabral.

&emsp;&emsp;A importância desse modelo se estende para além das recomendações iniciais. Com base nas interações e nos interesses registrados pelos CEOs, especialmente quando criam projetos dentro de determinados macrotemas, o modelo de recomendação evolui. Esse aprendizado contínuo permite o desenvolvimento de um segundo modelo mais sofisticado e adaptativo. Esse novo modelo pode então oferecer recomendações mais precisas e alinhadas com os interesses específicos dos CEOs, melhorando significativamente a relevância e a eficácia das sugestões apresentadas, e consequentemente, potencializando a engajamento e a satisfação dos usuários com a plataforma.

&emsp;&emsp; O modelo de recomendação, peça fundamental para o sucesso desta solução, provou ser fundamental não apenas para engajar os usuários desde o primeiro contato, sendo os testes de usabilidade realizados, mas também para refinamento contínuo das recomendações à medida que mais dados sobre as preferências sobre os macro e subtemas de projetos dos usuários são coletados. Nas seções "8.1 Especificação da Base de Dados para Modelo de Recomendação" e "10. Testes de Software" deste documento, encontram-se mais informações sobre os modelos de recomendações do aplicativo `Coffee Break`, desenvolvido pelo Grupo Spark.

## 9.2 Estrutura da Solução

&emsp;&emsp;A solução "Coffee Break" é um projeto composto por um aplicativo móvel e um dashboard para desktop, desenvolvido em colaboração com a FDC. Para a implementação desta solução, a equipe escolheu uma variedade de tecnologias e ferramentas modernas, adequando-se às necessidades específicas do projeto. No front-end, utilizamos Flutter e Dart, que permitiram uma experiência de usuário coesa e fluida em ambos os dispositivos móveis e desktops. Já no back-end, optamos por Flask devido à sua flexibilidade e facilidade de integração com outras tecnologias, como detalhado na seção 6.4 deste documento. Este conjunto de escolhas tecnológicas facilitou o desenvolvimento de uma solução robusta e escalável.

&emsp;&emsp;Além disso, o projeto foi construído utilizando a arquitetura SOA (Service-Oriented Architecture), uma escolha estratégica que desempenhou um papel fundamental no aprendizado da equipe e na facilitação dos serviços ofertados pela solução. A arquitetura SOA permitiu uma integração eficiente e flexível de diferentes serviços, como sistemas de recomendação, gerenciamento de perfis de CEOs e projetos específicos. Essa abordagem não apenas melhorou a modularidade e a manutenibilidade do sistema, mas também otimizou a entrega de funcionalidades específicas, garantindo uma experiência de usuário mais rica e adaptada às necessidades dos parceiros da FDC.

# 10. Testes de Software

&emsp;&emsp;Os testes de software são uma parte essencial do processo de desenvolvimento de software, pois garantem que o sistema funcione conforme o esperado e atenda aos requisitos do usuário. Eles ajudam a identificar erros, falhas e problemas de desempenho, permitindo que sejam corrigidos antes que o software seja implantado em produção. Existem vários tipos de testes de software, incluindo testes de unidade, testes de integração, testes de aceitação e testes de desempenho, cada um com seu próprio propósito e escopo.

&emsp;&emsp;Neste capítulo, exploraremos detalhadamente os testes conduzidos na solução `Coffee Break`, abrangendo desde testes de usabilidade do mockup até testes de integração, avaliação da API externa e análise do modelo de recomendação. Cada categoria de teste segue rigorosamente o plano de testes estabelecido, tendo objetivos claros que contribuem significativamente para assegurar a qualidade e a confiabilidade da aplicação. Esses testes são essenciais para identificar e resolver rapidamente quaisquer problemas, otimizando o desempenho e a eficiência da solução.

## 10.1 Plano de Testes

&emsp;&emsp;O Plano de Testes para o projeto "Coffee Break" é essencial para garantir a robustez e a eficácia da aplicação. Este plano detalha procedimentos específicos para validar a integração entre o front-end e o back-end, bem como a comunicação do back-end com o banco de dados. Através de testes meticulosos, incluindo vídeos e capturas de tela, garantimos que todas as funcionalidades principais, especialmente as operações de CRUD, operem conforme esperado em todos os componentes da aplicação.

### Integração do Front-end com o Back-end (vídeo)

- **Objetivo**: Verificar a comunicação correta entre o front-end e o back-end da aplicação.

- **Escopo**: Testar todas as funcionalidades principais do front-end, incluindo operações de CRUD.

- **Ferramentas**:

  - Front-end: Aplicação web (React, Angular, etc.)
  - Back-end: API REST (FastAPI, Django, etc.)
  - Ferramenta de gravação de tela (Screen Recorder, Google Meet, Slack, etc.)

#### Passos

- Vídeo mostrando as funcionalidades.
- Imagens capturadas do vídeo para o Markdown do GitHub.

### Integração do Back-end com o Banco de Dados

- **Objetivo**: Verificar a comunicação correta entre o back-end e o banco de dados.

- **Escopo**: Testar operações de CRUD em todas as entidades principais.

- **Ferramentas**:
  - Postman ou Insomnia para testar a API.
  - Python com `pytest` para testar a integração.

#### Passos:

- Teste de Consulta (GET):

  - Pré-condição: Dados existentes no banco de dados.
  - Pós-condição: Dados retornados corretamente pela API.
  - Teste: Enviar requisição GET para listar todos os registros.

- Teste de Inserção (POST):

  - Pré-condição: Estrutura do banco de dados pronta para receber novos registros.
  - Pós-condição: Novo registro salvo no banco de dados.
  - Teste: Enviar requisição POST com dados válidos para criar um novo registro.

- Teste de Atualização (PUT):

  - Pré-condição: Registro existente no banco de dados.
  - Pós-condição: Registro atualizado no banco de dados.
  - Teste: Enviar requisição PUT para atualizar um registro existente.

- Teste de Exclusão (DELETE):
  - Pré-condição: Registro existente no banco de dados.
  - Pós-condição: Registro removido do banco de dados.
  - Teste: Enviar requisição DELETE para excluir um registro existente.

#### Evidências:

- Capturas de tela das requisições e respostas no Postman.
- Logs da aplicação mostrando a interação com o banco de dados.
- Resultados registrados no Markdown do GitHub.

### Integração do Back-end com API Externa

- **Objetivo**: Verificar a comunicação correta entre o back-end e uma API externa.

- **Escopo**: Testar requisições feitas pelo back-end a uma API externa.

- **Ferramentas**:
  - Postman ou Insomnia para simular as requisições.
  - Python com `pytest` para testar a integração.

#### Passos:

- Requisição GET:

  - Pré-condição: API externa disponível.
  - Pós-condição: Dados retornados corretamente pela API externa.
  - Teste: Enviar requisição GET para a API externa e processar a resposta.

- Requisição POST:
  - Pré-condição: API externa disponível.
  - Pós-condição: Dados enviados corretamente para a API externa.
  - Teste: Enviar requisição POST com dados válidos para a API externa.

#### Evidências:

- Capturas de tela das requisições e respostas no Postman.
- Logs da aplicação mostrando a interação com a API externa.
- Resultados registrados no Markdown do GitHub.

### Integração do Back-end com o Modelo de Recomendação

- **Objetivo**: Verificar a comunicação correta entre o back-end e o modelo de recomendação. Assegurar que os dados são processados corretamente e que as recomendações são devolvidas de acordo com o esperado.

- **Escopo**: Testar a integração entre o back-end e o modelo de recomendação.

- **Ferramentas**:
  - Python com `pytest` para testar a integração.
  - Postman ou Insomnia para testar a API.

#### Passos:

- Requisição GET:
  - Pré-condição: Modelo de recomendação disponível. Serviço de recomendação disponível. Banco de dados com dados de teste. Usuário com ID de teste existente.
  - Pós-condição: Dados retornados corretamente pelo modelo de recomendação.
  - Teste: Enviar requisição GET para o modelo de recomendação e processar a resposta.

#### Evidências:

![Print da tela do Postman com o retorno das recomendações para o usuário de id 1000](./assets/images/evidencia-recomendacao.png)

## 10.2 Testes de Usabilidade para Mockup

&emsp;&emsp;O teste de usabilidade é uma técnica essencial para avaliar como os usuários reais interagem com um mockup de aplicativo móvel, com o objetivo de observar e identificar quaisquer dificuldades ou problemas de usabilidade que eles possam enfrentar ao tentar completar tarefas específicas. Este tipo de teste geralmente é bastante utilizado por ser de baixo custo e por ser importante para garantir que o aplicativo seja intuitivo e fácil de usar, identificando problemas de design que podem não ser evidentes para os desenvolvedores e designers durante a fase inicial de desenvolvimento.

&emsp;&emsp;A importância de realizar testes de usabilidade em mockups de aplicativos móveis reside na capacidade de melhorar significativamente a experiência do usuário, aumentando a satisfação e reduzindo as taxas de abandono. Ao coletar feedbacks direto dos usuários, os desenvolvedores e designers podem fazer ajustes informados no design antes da programação final, evitando custos adicionais de revisões pós-lançamento e garantindo que o aplicativo atenda às expectativas dos usuários finais, resultando em um produto mais bem-sucedido no mercado.

&emsp;&emsp;Para o desenvolvimento dos testes de usabilidade para a solução Coffee Break, utilizou-se o SUS (System Usability Scale), um instrumento, apresentado em sala de aula, e reconhecido por sua eficácia e solidificação comprovada em avaliar a usabilidade de sistemas. A escolha do SUS é estratégica, pois oferece parâmetros claros e objetivos que facilitam a identificação de aspectos do design que precisam ser aprimorados, por meio de uma metodologia quantitativa que utiliza notas fornecidas pelos usuários que estão testando a aplicação.

&emsp;&emsp;Essa avaliação é baseada em 10 frases específicas, e os usuários atribuem notas em uma escala de 0 (Discordo totalmente) a 5 (Concordo totalmente) e seu objetivo é determinar o nível de qualidade do sistema. As 10 afirmações utilizadas permitem um mapeamento detalhado e abrangente de várias dimensões críticas, como usabilidade, funcionalidade e satisfação do usuário. Essa abordagem padronizada transforma percepções subjetivas em dados quantificáveis, facilitando comparações objetivas e a identificação de áreas específicas para melhorias, garantindo assim uma avaliação holística.

<div align="center">
  <sub>Quadro X - Perguntas SUS</sub>
	
| Número | Descrição da Pergunta | 
| ------ | --------------------- |
| #1 | Eu acho que gostaria de usar esse sistema com frequência. | 
| #2 | Eu acho o sistema desnecessariamente complexo. | 
| #3 | Eu achei o sistema fácil de usar. | 
| #4 | Eu acho que precisaria de ajuda de uma pessoa com conhecimentos técnicos para usar o sistema. |
| #5 | Eu acho que as várias funções do sistema estão muito bem integradas. | 
| #6 | Eu acho que o sistema apresenta muita inconsistência. |
| #7 | Eu imagino que as pessoas aprenderão como usar esse sistema rapidamente. |
| #8 | Eu achei o sistema atrapalhado de usar. |
| #9 | Eu me senti confiante ao usar o sistema. |
| #10 | Eu precisei aprender várias coisas novas antes de conseguir usar o sistema. |

<sup>Fonte: Os autores (2024)</sup>

</div>

&emsp;&emsp;Abaixo, você encontrará um gráfico em formato de imagem que apresenta as pontuações atribuídas por todos os usuários que testaram a aplicação, em resposta a uma das perguntas do SUS. Este gráfico visualmente representa a avaliação específica dentro do contexto mais amplo do teste de usabilidade. Para acessar todas as respostas e registros detalhados deste teste, incluindo informações adicionais, consulte a [planilha completa](https://docs.google.com/spreadsheets/d/1s1-W4sLhXfBdV5Eho46pUD9zG_Wfo_Z8QnEPY5PYHno/edit?usp=sharing).

<div align="center">
  <sub>Figura 59 - Exemplo Resposta SUS </sub>
   <img src='./assets/images/resposta-sus.png' width="100%" alt='Exemplo Resposta SUS'>
  <sup>Fonte: Os autores (2024)</sup>
</div>

&emsp;&emsp;Para realizar o teste de usabilidade do [Mockup](https://www.figma.com/design/Xx3xcFOitGUQClVQiAqSPw/Style-Guidelines?node-id=528-373&t=7cMjTRNsqHsRirZO-1) do Coffee Break, utilizando o [SUS](https://brasil.uxdesign.cc/o-que-%C3%A9-o-sus-system-usability-scale-e-como-us%C3%A1-lo-em-seu-site-6d63224481c8) (System Usability Scale), foi necessário identificar o público-alvo que se beneficiará com a solução em desenvolvimento. Este grupo é composto principalmente por CEOs parceiros da Fundação Dom Cabral, executivos que utilizarão o aplicativo móvel com frequência para promover e monitorar projetos colaborativos de ESG (Environmental, Social and Governance). Portanto, a equipe mapeou e convidou cinco CEOs, representando diversos setores, que potencialmente correspondem ao perfil desejado para o teste:

<div align="center">
  <sub>Quadro X - Perfil de Testers</sub>
	
| id | Nome | Idade | Cargo | Empresa | Uso Diário Celular | Uso Diário Redes Sociais | 
| --- | ---- | ----- | ----- | ------- | ------------------ | ------------------------- | 
| #1 | Romulo Prudente | 54 | CEO | Implanta | 2h40 | 40min |
| #2 | Vinicius Freitas | 50 | CEO | DVF | 10h | 8h |
| #3 | Verônica Caricati | 26 | CEO | Mapa Educação | 4h | 1h |
| #4 | Maira Habimorad | 44 | CEO | Inteli | 8h | 4h  |
| #5 | Frederico Comério | 41 | CTO | Intelliway | 5h | 1h |

<sup>Fonte: Os autores (2024)</sup>

</div>

&emsp;&emsp;Por meio deste mapeamento, é possível dizer que, em relação a idade, existe uma variação entre 26 a 54 anos, todos ocupam principalmente o cargo de CEO, com exceção de um que é CTO. Os executivos mapeados lideram uma variedade de empresas, incluindo a "Implanta", "DVF", "Mapa Educação", "Inteli" e "Intelliway", respectivamente. Além disso, foi mapeado também que a média de uso diário de celular entre os indivíduos é de aproximadamente 5 horas e 56 minutos, enquanto a média de uso diário de redes sociais é cerca de 2 horas e 56 minutos.

&emsp;&emsp;Com base nas informações registradas, a equipe planejou como o teste de usabilidade seria conduzido, seguindo as especificações do SUS (System Usability Scale). Para isso, foram desenvolvidas cinco tarefas principais que os CEOs, usuários-alvo do teste, utilizariam frequentemente no aplicativo. Essas tarefas foram projetadas para que os executivos demonstrassem como empregariam a solução em situações reais. Durante o teste, foi possível registrar o desempenho de cada participante, observando dificuldades, facilidades, obstáculos e possíveis sugestões de melhorias.

<div align="center">
  <sub>Quadro X - Resultados Tarefas</sub>

| Tarefa | Descrição                                                                                        | Resultado Obtido                                                                    |
| ------ | ------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------- |
| 1      | Acessar um projeto de Redução do Impacto Ambiental.                                              | 100% dos CEOs conseguiram realizar essa tarefa com facilidade.                      |
| 2      | Acessar suas notificações.                                                                       | 100% dos CEOs conseguiram realizar essa tarefa com facilidade.                      |
| 3      | Acessar seus projetos salvos.                                                                    | 60% dos CEOs conseguiram realizar essa tarefa com facilidade e 40% com dificuldade. |
| 4      | Criar um projeto de Diversidade e Inclusão.                                                      | 20% dos CEOs conseguiram realizar essa tarefa com facilidade e 80% com dificuldade. |
| 5      | Solicitar uma sinergia no projeto “Apoio na agenda de descarbonização na cadeia de suprimentos”. | 60% dos CEOs conseguiram realizar essa tarefa com facilidade e 60% com dificuldade. |

<sup>Fonte: Os autores (2024)</sup>

</div>

&emsp;&emsp;O resultado geral do teste foi bastante positivo, uma vez que as tarefas foram organizadas com dificuldade gradativa, começando da mais fácil para a mais desafiadora. Conforme esperado, as duas primeiras tarefas foram completadas com sucesso por todos os usuários. A partir da terceira tarefa, o nível de dificuldade aumentou, e os testers começaram a enfrentar alguns obstáculos. No entanto, todos os usuários conseguiram realizar as tarefas com sucesso, sugerindo que apenas pequenos ajustes são necessários, principalmente em relação à disposição e à implementação de funcionalidades.

<div align="center">
  <sub>Figura 60 - Gráfico Tarefa 4</sub>
   <img src='./assets/images/tarefa-1.png' width="100%" alt='Tarefa 1'>
  <sup>Fonte: Os autores (2024)</sup>
</div>

<div align="center">
  <sub>Figura 61 - Gráfico Tarefa 4</sub>
   <img src='./assets/images/tarefa-1.png' width="100%" alt='Tarefa 1'>
  <sup>Fonte: Os autores (2024)</sup>
</div>

<div align="center">
  <sub>Figura 62 - Gráfico Tarefa 4</sub>
   <img src='./assets/images/tarefa-2.png' width="100%" alt='Tarefa 2'>
  <sup>Fonte: Os autores (2024)</sup>
</div>

<div align="center">
  <sub>Figura 63 - Gráfico Tarefa 4</sub>
   <img src='./assets/images/tarefa-3.png' width="100%" alt='Tarefa 3'>
  <sup>Fonte: Os autores (2024)</sup>
</div>

<div align="center">
  <sub>Figura 64 - Gráfico Tarefa 4</sub>
   <img src='./assets/images/tarefa-4.png' width="100%" alt='Tarefa 4'>
  <sup>Fonte: Os autores (2024)</sup>
</div>

<div align="center">
  <sub>Figura 65 - Gráfico Tarefa 4</sub>
   <img src='./assets/images/tarefa-5.png' width="100%" alt='Tarefa 5'>
  <sup>Fonte: Os autores (2024)</sup>
</div>

&emsp;&emsp;Além dos resultados mencionados, baseados no SUS e nas tarefas designadas para o teste, também foram coletados feedbacks e sugestões de melhorias dos usuários. Conforme discutido anteriormente, foi identificado a necessidade de pequenos ajustes nas funcionalidades do sistema. Estas sugestões abaixo, serão implementadas com o objetivo de tornar o aplicativo o mais intuitivo e prático possível, visando proporcionar uma excelente experiência ao usuário. Assim, espera-se que a solução se torne um serviço que faça a diferença em relação aos legados dos CEOs, conforme desejado pela FDC.

<div align="center">
  <sub>Quadro X - Sugestões de Melhorias dos Testers</sub>
	
| id | Sugestão de Melhoria |
| -- | -------------------- |
| #1 | Dar um destaque para o navbar, está escondido. Na home, separar melhor a parte de macrotemas e recomendações. | 
| #2 | Poderia ter a explicação de sinergia, ícone de adição de projetos e busca mais específica. |
| #3 | Adicionar filtros na "Busca" por setor empresarial e localidade; Adicionar mais informações na descrição do projeto, como tempo de início, objetivos mais definidos, potencial de impacto, exemplo "vai atingir uma comunidade de x pessoas"... |
| #4 | Em "Projetos recomendados" adicionar "para você". |
| #5 | Atalhos para as principais funções na tela inicial. Exemplo:Atalho para meus projetos na página inicial e o ícone de adicionar projetos na home.
 
 <sup>Fonte: Os autores (2024)</sup>
</div>

&emsp;&emsp;As sugestões de melhorias identificadas estão atualmente sob análise para implementação antes da entrega final do projeto. A equipe chegou ao consenso de que todas são extremamente úteis e relevantes para garantir ótima usabilidade e aprimorar a experiência do usuário com as funcionalidades do sistema. Além disso, por meio de cinco tarefas específicas propostas aos CEOs que participaram dos testes no mockup da solução, foi possível registrar o nível de dificuldade enfrentado por eles. Vale ressaltar que é importante visualizar a [planilha](https://docs.google.com/spreadsheets/d/1s1-W4sLhXfBdV5Eho46pUD9zG_Wfo_Z8QnEPY5PYHno/edit?usp=sharing) com as respostas completas.

&emsp;&emsp;Para concluir, a avaliação final do sistema, baseada no modelo do [SUS](https://brasil.uxdesign.cc/o-que-%C3%A9-o-sus-system-usability-scale-e-como-us%C3%A1-lo-em-seu-site-6d63224481c8) (System Usability Scale), com tarefas e perguntas planejadas para o teste, foi possível calcular em qual escala o projeto se encontra, e o resultado foi a pontuação de 85.5. Na escala do SUS, isso indica que o sistema está classificado como "Excelente", representando uma pontuação quantitativamente elevada e muito positiva para o projeto. Essas parâmetros são essenciais para avaliar a experiência do usuário e o possível potencial para uso real desse aplicativo mobile.

&emsp;&emsp;Portanto, os testes de usabilidade do Mockup do projeto Coffeebreak, com base nas informações e resultados apresentados, fica evidente que a solução em questão tem demonstrado um desempenho promissor em termos de usabilidade e aceitação pelo público-alvo, que são CEOs. Para continuação do desenvolvimendo do aplicativo, o processo de refinamento é fundamental para garantir que o sistema não apenas atenda às expectativas dos usuários, mas também contribua significativamente para a melhoria contínua da usabilidade e da experiência geral do usuário.

## 10.3 Testes de Integração

&emsp;&emsp;Os testes de integração verificam a eficácia e a confiabilidade das interações entre os módulos individuais que compõem a aplicação. O objetivo é detectar falhas na interface e na integração entre os componentes do sistema, garantindo que eles funcionem juntos conforme o esperado. Na solução `Coffee Break`, os testes de integração são essenciais para assegurar que todas as partes do sistema, desde o back-end até as integrações com APIs externas e bancos de dados, operem harmoniosamente.

&emsp;&emsp;Além disso, o **Test-Driven Development (TDD)** é uma metodologia de desenvolvimento que prioriza a escrita de testes antes do desenvolvimento de funcionalidades propriamente ditas. Essa abordagem é amplamente promovida por Robert C. Martin (também conhecido como Uncle Bob) e outros defensores dos métodos ágeis de desenvolvimento. TDD é caracterizado por um ciclo iterativo de três etapas: escrever um teste que falha, escrever o código mínimo necessário para fazer o teste passar e, por fim, refatorar o código para melhorar sua qualidade e eficiência.

&emsp;&emsp;Dessa forma, adotando o TDD, a equipe segue um processo rigoroso onde os testes de integração são escritos antes do código de produção. Isso não só ajuda a definir claramente os requisitos do sistema antes do desenvolvimento, mas também facilita a detecção precoce de erros, contribuindo para um ciclo de desenvolvimento mais eficiente e menos propenso a falhas dispendiosas no futuro.

&emsp;&emsp;Para implementar e executar testes de integração, a equipe utiliza frameworks como `pytest` para Python, que oferece suporte robusto para testar exceções, falhas e comportamentos esperados. Além disso, utiliza-se a biblioteca `unittest.mock` para simular e controlar as interações com recursos externos, como bancos de dados e APIs de terceiros, permitindo que os testes sejam executados de maneira isolada e controlada.

### Estratégia de Teste

&emsp;&emsp;A estratégia de testes de integração abrange diversos cenários e combinações de uso para garantir a abrangência e a profundidade dos testes:

- **Interações com o Banco de Dados**: Testes que verificam se as operações de CRUD estão sendo executadas corretamente, considerando a persistência e recuperação de dados.

- **Integração com APIs Externas**: Testes que asseguram que a aplicação lida corretamente com as requisições e respostas de APIs externas, incluindo o manejo adequado de erros de rede e dados incorretos. Esses testes serão implementados a partir da sprint 3.

- **Fluxos de Trabalho Completos**: Cenários que simulam o uso completo do sistema para garantir que todos os módulos interagem corretamente sob condições operacionais normais e de estresse.

### Exemplo de Teste de Integração

&emsp;&emsp;A seguir, é apresentado um exemplo de teste de integração para a operação de cadastro de um usuário, a partir do serviço de CEO do sistema `Coffee Break`:

<div align="center">
  <sub>Figura 66 - Exemplo de Teste de Integração</sub>
  <img src="./assets/images/teste-integracao.png" width="100%" alt="Teste de Integração">
  <sup>Fonte: Os autores (2024)</sup>
</div>

### Resultados dos Testes

#### Testes de Projetos

- **Evidências**: Relatório de teste em formato XML: [test_projeto_integration.xml](../src/tests/integration/test_projeto_integration.xml)

**Teste de Consulta (GET `/projetos/`)**

- **Pré-condição:** Existem projetos cadastrados no banco de dados.

- **Pós-condição:** A lista de projetos é retornada com sucesso pela API, e o banco de dados permanece inalterado.

- Requisição HTTP

  ```http
  GET /projetos/ HTTP/1.1
  Host: localhost:80
  ```

- Resposta HTTP

  ```http
  HTTP/1.1 200 OK
  Content-Type: application/json

  [
      {
          "id": 1,
          "ceo_id": 1,
          "subtema_id": 1,
          "nome": "Projeto Existente",
          "descricao": "Descrição do Projeto Existente",
          "data_criacao": "2024-06-08T12:34:56",
          "estado": "ativo"
      },
      ...
  ]
  ```

- Execução do Teste

  ```python
  import os
  import unittest
  import json
  import psycopg2
  import requests
  from dotenv import load_dotenv
  from xmlrunner import XMLTestRunner

  load_dotenv()

  class ProjetoIntegrationTest(unittest.TestCase):
      def setUp(self):
          self.base_url = 'http://localhost:80/projetos/'
          self.conn = psycopg2.connect(
              dbname="coffee-break-database",
              user=os.getenv('DB_USER'),
              password=os.getenv('DB_PASS'),
              host=os.getenv('DB_HOST'),
          )
          self.cur = self.conn.cursor()
          self.dir = os.path.dirname(__file__)

      def tearDown(self):
          self.cur.close()
          self.conn.close()

      def test_get_projetos(self):
          response = requests.get(self.base_url)
          self.assertEqual(response.status_code, 200,  f"O status code foi diferente de 200: {response.status_code}")
          data = response.json()
          self.assertIsInstance(data, list, f"O tipo de retorno foi diferente de list: {type(data)}")
          self.assertGreater(len(data), 0, f"O tamanho da lista foi menor ou igual a 0: {len(data)}")

          # Pega o ID do primeiro projeto retornado
          primeiro_projeto_id = data[0]['id']

          # Verifica se o primeiro projeto no banco de dados está na resposta
          self.cur.execute("SELECT nome FROM Projeto WHERE id = %s", (primeiro_projeto_id,))
          projeto_nome = self.cur.fetchone()[0] # type: ignore
          self.assertEqual(data[0]['nome'], projeto_nome, f"O nome do projeto retornado foi diferente do nome do projeto no banco de dados")

          # Conta quantos projetos existem no banco de dados
          # E compara com a quantidade de projetos retornados
          self.cur.execute("SELECT COUNT(*) FROM Projeto")
          quantidade_projetos = self.cur.fetchone()[0] # type: ignore
          self.assertEqual(len(data), quantidade_projetos, f"A quantidade de projetos retornados foi diferente da quantidade de projetos no banco de dados")

  if __name__ == '__main__':
      # cria um xml no mesmo diretório do arquivo de teste
      path = os.path.join(os.path.dirname(__file__), 'test_projeto_integration.xml')
      with open(path, 'wb') as output:
          runner = XMLTestRunner(output=output)
          unittest.main(testRunner=runner)
  ```

**Teste de Inserção (POST `/projetos/`)**

- **Pré-condição**: O banco de dados não possui um projeto com os dados fornecidos.

- **Pós-condição**: Um novo projeto é inserido no banco de dados e é retornado um identificador válido pela API. Todavia, o projeto é removido após a execução do teste para manter a integridade do banco de dados.

- Requisição HTTP

  ```http
  POST /projetos/ HTTP/1.1
  Host: localhost:80
  Content-Type: application/json

  {
      "ceo_id": 1,
      "subtema_id": 1,
      "nome": "Novo Projeto Unittest",
      "descricao": "Descrição do Novo Projeto Unittest"
  }
  ```

- Resposta HTTP

  ```http
  HTTP/1.1 200 OK
  Content-Type: application/json

  {
      "id": 1429
  }
  ```

- Execução do Teste

  ```python
  import os
  import unittest
  import json
  import psycopg2
  import requests
  from dotenv import load_dotenv
  from xmlrunner import XMLTestRunner

  load_dotenv()

  class ProjetoIntegrationTest(unittest.TestCase):
      def setUp(self):
          self.base_url = 'http://localhost:80/projetos/'
          self.conn = psycopg2.connect(
              dbname="coffee-break-database",
              user=os.getenv('DB_USER'),
              password=os.getenv('DB_PASS'),
              host=os.getenv('DB_HOST'),
          )
          self.cur = self.conn.cursor()
          self.dir = os.path.dirname(__file__)

      def tearDown(self):
          self.cur.execute("DELETE FROM Projeto WHERE nome = %s", ('Novo Projeto Unittest',))
          self.conn.commit()
          self.cur.close()
          self.conn.close()

      def test_post_projeto(self):
          projeto_data = {
              "ceo_id": 1,
              "subtema_id": 1,
              "nome": "Novo Projeto Unittest",
              "descricao": "Descrição do Novo Projeto Unittest",
          }
          response = requests.post(self.base_url, data=json.dumps(projeto_data), headers={'Content-Type': 'application/json'})
          self.assertEqual(response.status_code, 200, f"O status code foi diferente de 200: {response.status_code}")
          data = response.json()
          self.assertIsNotNone(data, f"O retorno foi None")
          self.assertIsInstance(data, int, f"O tipo de retorno foi diferente de int: {type(data)}")

          # Verifica se o projeto foi inserido no banco de dados
          self.cur.execute("SELECT nome FROM Projeto WHERE id = %s", (data,))
          projeto_nome = self.cur.fetchone()[0] # type: ignore
          self.assertEqual(projeto_nome, "Novo Projeto Unittest", f"O nome do projeto inserido foi diferente do nome do projeto no banco de dados")

  if __name__ == '__main__':
      # cria um xml no mesmo diretório do arquivo de teste
      path = os.path.join(os.path.dirname(__file__), 'test_projeto_integration.xml')
      with open(path, 'wb') as output:
          runner = XMLTestRunner(output=output)
          unittest.main(testRunner=runner)

  ```

#### Testes de CEOs

- **Evidências**: Relatório de teste em formato XML: [test_ceo_integration.xml](../src/tests/integration/test_ceo_integration.xml)

**Teste de Consulta (GET `/ceos/`)**

- **Pré-condição**: Existem CEOs cadastrados no banco de dados.

- **Pós-condição**: A lista de CEOs é retornada com sucesso pela API, e o banco de dados permanece inalterado.

- Requisição HTTP

  ```http
  GET /ceos/ HTTP/1.1
  Host: localhost:80
  ```

- Resposta HTTP

  ```http
  HTTP/1.1 200 OK
  Content-Type: application/json

  {
      "quantidade": 1446,
      "ceos": [
          {
              "id": 1,
              "nome": "CEO Existente",
              "cargo": "CEO",
              "empresa_nome": "Empresa Existente",
              "estado": "ativo",
              "biografia": "Biografia do CEO Existente",
              "celular": "123456789",
              "email_contato": "contato@empresa.com",
              "empresa_link": "http://empresa.com",
              "foto": "http://empresa.com/foto.jpg",
              "linkedin": "http://linkedin.com/in/existente",
              "email": "ceo@existente.com",
              "senha": "senha123"
          },
          ...
      ]
  }

  ```

- Execução do Teste

  ```python
  import os
  import unittest
  import psycopg2
  import requests
  from dotenv import load_dotenv
  from xmlrunner import XMLTestRunner

  load_dotenv()

  class CeoIntegrationTest(unittest.TestCase):
      def setUp(self):
          self.base_url = 'http://localhost:80/ceos/'
          self.conn = psycopg2.connect(
              dbname="coffee-break-database",
              user=os.getenv('DB_USER'),
              password=os.getenv('DB_PASS'),
              host=os.getenv('DB_HOST'),
          )
          self.cur = self.conn.cursor()

      def tearDown(self):
          self.cur.close()
          self.conn.close()

      def test_get_ceos(self):
          response = requests.get(self.base_url)
          self.assertEqual(response.status_code, 200, f"O status code foi diferente de 200: {response.status_code}")
          data = response.json()
          self.assertIsInstance(data['ceos'], list, f"O tipo de retorno foi diferente de list: {type(data['ceos'])}")
          self.assertGreater(len(data['ceos']), 0, f"O tamanho da lista foi menor ou igual a 0: {len(data['ceos'])}")

          # Pega o ID do primeiro CEO retornado
          primeiro_ceo_id = data['ceos'][0]['id']

          # Verifica se o primeiro CEO no banco de dados está na resposta
          self.cur.execute("SELECT nome FROM Ceo WHERE id = %s", (primeiro_ceo_id,))
          ceo_nome = self.cur.fetchone()[0] # type: ignore
          self.assertEqual(data['ceos'][0]['nome'], ceo_nome, f"O nome do CEO retornado foi diferente do nome do CEO no banco de dados")

          # Conta quantos CEOs existem no banco de dados
          # E compara com a quantidade de CEOs retornados
          self.cur.execute("SELECT COUNT(*) FROM Ceo")
          quantidade_ceos = self.cur.fetchone()[0] # type: ignore
          self.assertEqual(data['quantidade'], quantidade_ceos, f"A quantidade de CEOs retornados foi diferente da quantidade de CEOs no banco de dados")

  if __name__ == '__main__':
      # cria um xml no mesmo diretório do arquivo de teste
      path = os.path.join(os.path.dirname(__file__), 'test_ceo_integration.xml')
      with open(path, 'wb') as output:
          runner = XMLTestRunner(output=output)
          unittest.main(testRunner=runner)

  ```

**Teste de Inserção (POST `/ceos/`)**

- **Pré-condição**: O banco de dados não possui um CEO com os dados fornecidos.

- **Pós-condição**: Um novo CEO é inserido no banco de dados e é retornado um identificador válido pela API. Todavia, o CEO é removido após a execução do teste para manter a integridade do banco de dados.

- Requisição HTTP

  ```http
  POST /ceos/ HTTP/1.1
  Host: localhost:80
  Content-Type: application/json

  {
      "nome": "Novo CEO Unittest",
      "cargo": "CEO",
      "empresa_nome": "Empresa Teste",
      "estado": "ativo",
      "biografia": "Biografia do Novo CEO Unittest",
      "celular": "123456789",
      "email_contato": "teste@empresa.com",
      "empresa_link": "http://empresa.com",
      "foto": "http://empresa.com/foto.jpg",
      "linkedin": "http://linkedin.com/in/teste",
      "email": "novoceo@teste.com",
      "senha": "senha123"
  }

  ```

- Resposta HTTP

  ```http
  HTTP/1.1 201 Created
  Content-Type: application/json

  {
    1429
  }
  ```

- Execução do Teste

  ```python
  import os
  import unittest
  import psycopg2
  import requests
  from dotenv import load_dotenv
  from xmlrunner import XMLTestRunner

  load_dotenv()

  class CeoIntegrationTest(unittest.TestCase):
      def setUp(self):
          self.base_url = 'http://localhost:80/ceos/'
          self.conn = psycopg2.connect(
              dbname="coffee-break-database",
              user=os.getenv('DB_USER'),
              password=os.getenv('DB_PASS'),
              host=os.getenv('DB_HOST'),
          )
          self.cur = self.conn.cursor()

      def tearDown(self):
          self.cur.execute("DELETE FROM Ceo WHERE nome = %s", ('Novo CEO Unittest',))
          self.conn.commit()
          self.cur.close()
          self.conn.close()

      def test_post_ceo(self):
          ceo_data = {
              "nome": "Novo CEO Unittest",
              "cargo": "CEO",
              "empresa_nome": "Empresa Teste",
              "estado": "ativo",
              "biografia": "Biografia do Novo CEO Unittest",
              "celular": "123456789",
              "email_contato": "teste@empresa.com",
              "empresa_link": "http://empresa.com",
              "foto": "http://empresa.com/foto.jpg",
              "linkedin": "http://linkedin.com/in/teste",
              "email": "novoceo@teste.com",
              "senha": "senha123"
          }
          response = requests.post(self.base_url, data=json.dumps(ceo_data), headers={'Content-Type': 'application/json'})
          self.assertEqual(response.status_code, 201, f"O status code foi diferente de 201: {response.status_code}")
          data = response.json()
          self.assertIsNotNone(data, f"O retorno foi None")
          self.assertIsInstance(data, dict, f"O tipo de retorno foi diferente de dict: {type(data)}")
          self.assertIn('id', data, "A chave 'id' não está presente no retorno")

          # Verifica se o CEO foi inserido no banco de dados
          self.cur.execute("SELECT nome FROM Ceo WHERE id = %s", (data['id'],))
          ceo_nome = self.cur.fetchone()[0] # type: ignore
          self.assertEqual(ceo_nome, "Novo CEO Unittest", f"O nome do CEO inserido foi diferente do nome do CEO no banco de dados")

  if __name__ == '__main__':
      # cria um xml no mesmo diretório do arquivo de teste
      path = os.path.join(os.path.dirname(__file__), 'test_ceo_integration.xml')
      with open(path, 'wb') as output:
          runner = XMLTestRunner(output=output)
          unittest.main(testRunner=runner)
  ```

#### Testes de Recomendações

- **Evidências**: Relatório de teste em formato XML: [test_recomendacao_integration.xml](../src/tests/integration/test_recomendacao_integration.xml)

**Teste de Consulta (GET `/recomendacoes/recomendar/int:usuario_id`)**

- **Pré-condição**: Existem recomendações geradas para o usuário no banco de dados.

- **Pós-condição**: A lista de recomendações é retornada com sucesso pela API, e o banco de dados permanece inalterado.

- Requisição HTTP

  ```http
  GET /recomendacoes/recomendar/1 HTTP/1.1
  Host: localhost:80
  ```

- Resposta HTTP

  ```http
  HTTP/1.1 200 OK
  Content-Type: application/json

  [
      {
          "projeto": {
              "id": 1,
              "nome": "Projeto Recomendado",
              "descricao": "Descrição do Projeto Recomendado",
              "subtema_id": 1,
              "macrotema_id": 1,
              "subtema_nome": "Subtema Teste",
              "macrotema_nome": "Macrotema Teste",
              "ceo_id": 1,
              "ceos": [
                  {
                      "id": 1,
                      "nome": "CEO Teste",
                      "empresa_nome": "Empresa Teste"
                  }
              ]
          }
      },
      ...
  ]
  ```

- Execução do Teste

  ```python
  import os
  import unittest
  import psycopg2
  import requests
  from dotenv import load_dotenv
  from xmlrunner import XMLTestRunner

  load_dotenv()

  class RecomendacaoIntegrationTest(unittest.TestCase):
      def setUp(self):
          self.base_url = 'http://localhost:80/recomendacoes/recomendar/'
          self.conn = psycopg2.connect(
              dbname="coffee-break-database",
              user=os.getenv('DB_USER'),
              password=os.getenv('DB_PASS'),
              host=os.getenv('DB_HOST'),
          )
          self.cur = self.conn.cursor()

      def tearDown(self):
          self.cur.close()
          self.conn.close()

      def test_gerar_recomendacao(self):
          # Escolhe um usuário existente para gerar recomendações
          usuario_id = 1

          response = requests.get(f"{self.base_url}{usuario_id}")
          self.assertEqual(response.status_code, 200, f"O status code foi diferente de 200: {response.status_code}")
          data = response.json()
          self.assertIsInstance(data, list, f"O tipo de retorno foi diferente de list: {type(data)}")
          self.assertGreater(len(data), 0, f"O tamanho da lista foi menor ou igual a 0: {len(data)}")

          # Pega o ID do primeiro projeto recomendado
          primeiro_projeto_id = data[0]['projeto']['id']

          # Verifica se o primeiro projeto recomendado está no banco de dados
          self.cur.execute("SELECT nome FROM Projeto WHERE id = %s", (primeiro_projeto_id,))
          projeto_nome = self.cur.fetchone()[0]  # type: ignore
          self.assertEqual(data[0]['projeto']['nome'], projeto_nome, f"O nome do projeto retornado foi diferente do nome do projeto no banco de dados")

          # Verifica se a recomendação foi inserida na tabela de Recomendacao
          self.cur.execute("SELECT ceo_id, projeto_id, pontuacao, tipo FROM Recomendacao WHERE ceo_id = %s AND projeto_id = %s", (usuario_id, primeiro_projeto_id))
          recomendacao = self.cur.fetchone()
          self.assertIsNotNone(recomendacao, "A recomendação não foi encontrada na tabela de Recomendacao")
          self.assertEqual(recomendacao[0], usuario_id, f"O ceo_id da recomendação não corresponde ao esperado: {recomendacao[0]}")
          self.assertEqual(recomendacao[1], primeiro_projeto_id, f"O projeto_id da recomendação não corresponde ao esperado: {recomendacao[1]}")
          self.assertEqual(recomendacao[2], 0, f"A pontuacao da recomendação não corresponde ao esperado: {recomendacao[2]}")
          self.assertEqual(recomendacao[3], 'recomendacao', f"O tipo da recomendação não corresponde ao esperado: {recomendacao[3]}")

  if __name__ == '__main__':
      # cria um xml no mesmo diretório do arquivo de teste
      path = os.path.join(os.path.dirname(__file__), 'test_recomendacao_integration.xml')
      with open(path, 'wb') as output:
          runner = XMLTestRunner(output=output)
          unittest.main(testRunner=runner)
  ```

#### Testes de Sinergia

- **Evidências**: Relatório de teste em formato XML: [test_sinergia_integration.xml](../src/tests/integration/test_sinergia_integration.xml)

**Teste de Criação (POST `/projetos/sinergia`)**

- **Pré-condição**: Existem CEOs e projetos cadastrados no banco de dados. Não deve existir uma sinergia pré-existente entre o CEO e o projeto especificado.

- **Pós-condição**: Uma nova sinergia é criada no banco de dados com o status 'pendente' e é retornado um identificador válido pela API.

- Requisição HTTP

  ```http
  POST /projetos/sinergia/ HTTP/1.1
  Host: localhost:80
  Content-Type: application/json

  {
      "ceo_id": 1,
      "projeto_id": 1
  }
  ```

- Resposta HTTP

  ```http
  HTTP/1.1 200 OK
  Content-Type: application/json

  {
      "id": 5
  }
  ```

- Execução do Teste

  ```python
  import os
  import unittest
  import json
  import psycopg2
  import requests
  from dotenv import load_dotenv
  from xmlrunner import XMLTestRunner

  load_dotenv()

  class SinergiaIntegrationTest(unittest.TestCase):
      def setUp(self):
          self.base_url = 'http://localhost:80/projetos/sinergia/'
          self.conn = psycopg2.connect(
              dbname="coffee-break-database",
              user=os.getenv('DB_USER'),
              password=os.getenv('DB_PASS'),
              host=os.getenv('DB_HOST'),
          )
          self.cur = self.conn.cursor()

      def tearDown(self):
          self.cur.execute("DELETE FROM Interacao WHERE tipo = %s AND ceo_id = %s AND projeto_id = %s", ('sinergia', 1, 1))
          self.conn.commit()
          self.cur.close()
          self.conn.close()

      def test_post_sinergia(self):
          sinergia_data = {
              "ceo_id": 1,
              "projeto_id": 1
          }
          response = requests.post(self.base_url, data=json.dumps(sinergia_data), headers={'Content-Type': 'application/json'})
          self.assertEqual(response.status_code, 200, f"O status code foi diferente de 200: {response.status_code}")
          data = response.json()
          self.assertIsNotNone(data, f"O retorno foi None")
          self.assertIsInstance(data, int, f"O tipo de retorno foi diferente de int: {type(data)}")

          # Verifica se a sinergia foi inserida no banco de dados
          self.cur.execute("SELECT tipo, estado FROM Interacao WHERE id = %s", (data,))
          interacao = self.cur.fetchone()
          self.assertEqual(interacao[0], 'sinergia', f"O tipo da interação inserida foi diferente do esperado: {interacao[0]}")
          self.assertEqual(interacao[1], 'pendente', f"O estado da interação inserida foi diferente do esperado: {interacao[1]}")

  if __name__ == '__main__':
      # cria um xml no mesmo diretório do arquivo de teste
      path = os.path.join(os.path.dirname(__file__), 'test_sinergia_integration.xml')
      with open(path, 'wb') as output:
          runner = XMLTestRunner(output=output)
          unittest.main(testRunner=runner)

  ```

### Por Que os Testes Foram Além do Esperado

&emsp;&emsp;Os testes de integração foram além das expectativas previstas pelo artefato devido às seguintes razões:

1. `Verificações Detalhadas no Banco de Dados`: Além de verificar as respostas das requisições HTTP, os testes também incluem verificações detalhadas no banco de dados para garantir que as inserções e consultas estejam corretas. Isso assegura que o comportamento da API esteja de acordo com os dados persistidos.

2. `Cobertura Abrangente`: Os testes cobrem tanto operações de consulta quanto de inserção para múltiplas entidades (Projeto, CEO e Recomendacao), proporcionando uma cobertura abrangente das funcionalidades críticas da API.

3. `Documentação Completa`: A documentação dos testes é completa e detalhada, incluindo pré-condições, pós-condições, exemplos de requisições e respostas HTTP, bem como o estado do banco de dados antes e após a execução dos testes. Isso facilita a reprodução e entendimento dos testes, beneficiando a manutenção e evolução do sistema.

4. `Relatórios XML`: A utilização de relatórios XML gerados pelo unittest-xml-reporting permite a integração com ferramentas de CI/CD como Jenkins e Allure, promovendo uma visualização mais amigável e monitoramento contínuo dos resultados dos testes.

5. `Inclusão de Testes de Sinergia`: Embora a criação de sinergias faça parte do domínio de projetos, um teste específico foi implementado para esta funcionalidade devido à sua importância crítica. A sinergia entre projetos é um componente chave do sistema, e sua verificação meticulosa assegura a robustez e a integridade das interações entre CEOs e projetos.

&emsp;&emsp;Essas características demonstram um cuidado meticuloso com a qualidade do código e a confiabilidade das funcionalidades testadas, indo além do esperado para assegurar um sistema robusto e confiável.

## 10.4 Testes da API Externa

&emsp;&emsp;Uma API externa (_Application Programming Interface_) é um conjunto de regras e especificações que um software pode seguir para acessar e interagir com serviços externos. Essas APIs são oferecidas por terceiros e permitem que desenvolvedores integrem funcionalidades complexas sem ter que implementá-las do zero. Elas podem incluir serviços de dados, funcionalidades de redes sociais, soluções de pagamento, entre outros. O uso de APIs externas é comum para ampliar as capacidades de uma aplicação, permitindo uma integração eficiente com o ecossistema digital mais amplo.

### Escolhas de APIs para a Aplicação

**API de Notícias** (**News API**)

- Descrição: A News API é uma ferramenta simples e fácil de usar que retorna artigos de notícias ao vivo de várias fontes de notícias e blogs em todo o mundo. A API permite pesquisas com base em vários parâmetros, como tópicos, datas, idiomas, etc.

- Funcionalidades Utilizadas:

  **Busca de Artigos**: Permite pesquisar artigos globais usando palavras-chave, o que facilita a obtenção de notícias atualizadas sobre tópicos específicos.

  **Filtragem por Data**: Os artigos podem ser filtrados entre datas específicas, permitindo aos usuários acessar notícias de um período específico.

  **Ordenação por Relevância**: Os resultados podem ser ordenados por relevância em relação à palavra-chave, o que ajuda a trazer as notícias mais pertinentes ao topo.

- Justificativa da Escolha: Esta API foi escolhida para fornecer conteúdo dinâmico e relevante aos usuários, mantendo-os informados sobre os últimos acontecimentos relacionados a seus interesses. A capacidade de buscar por palavras-chave específicas e filtrar por datas ajuda a personalizar a experiência do usuário, tornando o app mais envolvente e útil.

**API de Avatar** (**DiceBear Avatars**)

- Descrição: DiceBear é uma API que permite a geração de avatares SVG baseados em sementes. Oferece vários estilos de avatar, que podem ser personalizados com diferentes sementes para criar imagens únicas.

- Funcionalidades Utilizadas:

  **Geração Baseada em Semente**: Cada avatar é único e é gerado a partir de uma semente específica, o que significa que a mesma semente sempre resultará no mesmo avatar.

  **Estilos Diversificados**: Diversos estilos estão disponíveis, como `miniavs`, `bottts`, `avataaars`, entre outros, permitindo uma personalização visual que pode se alinhar à estética do app.

- Justificativa da Escolha: A capacidade de gerar avatares personalizados e consistentes é vital para identificar visualmente os usuários em uma plataforma. Os avatares gerados ajudam a estabelecer uma identidade digital no aplicativo, melhorando a experiência do usuário e fornecendo uma forma de expressão pessoal.

**API de Login com Google** (**Google Sign-In**)

- Descrição: Google Sign-In é uma forma segura e conveniente de permitir que os usuários acessem aplicativos usando sua conta Google. Ele simplifica o processo de autenticação, eliminando a necessidade de criar e lembrar uma nova senha.

- Funcionalidades Planejadas:

  **Autenticação Rápida e Segura**: Permite que os usuários façam login com suas contas Google existentes, garantindo um processo de login rápido e seguro.

  **Integração com Serviços Google**: Uma vez autenticados, os usuários podem integrar-se facilmente a outros serviços Google, como Google Drive, Gmail, etc.

  **Gerenciamento de Sessão**: A API cuida do gerenciamento de sessão, mantendo os usuários conectados ou facilitando o logout conforme necessário.

- Justificativa da Escolha para Sprint 4: Implementar o Google Sign-In simplificará o acesso dos usuários ao aplicativo, reduzindo barreiras para novos usuários e aumentando a segurança. A autenticação via Google também confere um nível de confiabilidade e reconhecimento de marca, o que pode ajudar na adoção do app por novos usuários.

### Detalhes Técnicos dos Testes

&emsp;&emsp;Os testes da API externa são essenciais para garantir que a aplicação interaja corretamente com os serviços de terceiros, como a News API e a DiceBear Avatars. Esses testes verificam se as requisições são feitas corretamente, se as respostas são processadas adequadamente e se os dados são exibidos corretamente na aplicação. Além disso, os testes da API externa ajudam a identificar e corrigir problemas de integração, como erros de autenticação, problemas de rede e respostas inválidas.

&emsp;&emsp;Para realizar os testes da API externa, a equipe utiliza a biblioteca `unittest` para simular as respostas dos serviços de terceiros. Isso permite que os testes sejam executados de forma isolada e controlada, sem depender da disponibilidade ou do estado atual dos serviços reais. Além disso, a equipe utiliza a biblioteca `pytest` para escrever e executar os testes de forma eficiente e organizada, garantindo a cobertura adequada dos cenários de teste.

&emsp;&emsp;As funções de abstrações das APIs externas são testadas de forma isolada, verificando se as requisições são feitas corretamente e se as respostas são processadas adequadamente. Por fim, essas funções podem ser encontradas em `src/backend/external`.

### Resultados dos Testes

#### Testes da API de notícias

**Teste de Consulta (GET `/noticias/<string:tema>/`)**

- **Pré-condição:** Existam notícias geradas no dia relacionadas a palavra chave enviada na requisição `<string:tema>`.

- **Pós-condição:** A lista de notícias é retornada com sucesso pela API.

- Requisição HTTP

  ```http
  GET /noticias/tema?=saude HTTP/1.1
  Host: localhost:80
  ```

- Resposta HTTP

  ```http
  HTTP/1.1 200 OK
  Content-Type: application/json

  {
    data: [
      {
        "author": "Boa Forma",
        "content": "Você já ouviu falar que pegar friagem ou tomar chuva causa gripe ou resfriado? Ou então que andar descalço também pode fazer mal? De acordo com o Dr. Bruno Borges de Carvalho Barros, otorrinolaringol… [+3667 chars]",
        "description": "Você já ouviu falar que pegar friagem ou tomar chuva causa gripe ou resfriado ? Ou então que ...",
        "publishedAt": "2024-06-07T17:15:14Z",
        "source": {
          "id": null,
          "name": "Abril.com.br"
        },
        "title": "Tomar chuva causa gripe ou resfriado? Mitos e verdades sobre o tema",
        "url": "https://boaforma.abril.com.br/equilibrio/tomar-chuva-da-gripe-resfriado/",
        "urlToImage": "https://p2.trrsf.com/image/fget/cf/1200/630/middle/images.terra.com/2024/06/07/791710584-tomar-chuva-causa-gripe-ou-resfriado.jpg"
      },
      ...
    ],
    status: 'success'
  }
  ```

- Execução do Teste

  ```
  import unittest
  from backend.external.noticias.app import consumir_API_noticias

  # Teste unitários da API de Notícias
  class TesteNoticias(unittest.TestCase):
      def teste_obter_todos_noticias(self):
          resposta = consumir_API_noticias('saude')
          self.assertIn('status', resposta, "Resposta não contém o campo 'status'")
          self.assertEqual(resposta['status'], 'success', f"Esperado status 'success', mas recebeu {resposta['status']}")
          self.assertIn('data', resposta, "Resposta não contém o campo 'data'")

      def teste_obter_todos_noticias_erro(self):
          resposta = consumir_API_noticias('')
          self.assertIn('status', resposta, "Resposta não contém o campo 'status'")
          self.assertEqual(resposta['status'], 'error', f"Esperado status 'error', mas recebeu {resposta['status']}")
          self.assertIn('message', resposta, "Resposta não contém o campo 'message'")

  if __name__ == '__main__':
      unittest.main()
  ```

**Teste de Consulta (`https://api.dicebear.com/8.x/miniavs/svg?seed=avatar{numero}>/`)**

- **Pré-condição:** Uma semente fixa é fornecida para gerar um avatar.

- **Pós-condição:** Um avatar é gerado com sucesso a partir da semente fixa.

- **Resposta:** SVG do avatar

- Execução do Teste

  ```
  # pip install requests
  import requests
  import random
  import string


  class AvatarGenerator:
      def __init__(self, estilo='miniavs'):
          self.base_url = "https://api.dicebear.com/8.x"
          self.estilo = estilo

      def gerar_avatar(self, semente):
          url = f"{self.base_url}/{self.estilo}/svg?seed={semente}"
          response = requests.get(url)
          if response.status_code == 200:
              return url
          else:
              raise Exception("Erro ao gerar o avatar")

      def gerar_avatares_fixos(self, num_avatares):
          avatares = {}
          for i in range(num_avatares):
              semente = f"avatar{i}"
              avatares[semente] = self.gerar_avatar(semente)
          return avatares
      
      def gerar_avatares_aleatorios(self, num_avatares):
          avatares = {}
          for _ in range(num_avatares):
              semente = ''.join(random.choices(string.ascii_letters + string.digits, k=10))
              avatares[semente] = self.gerar_avatar(semente)
          return avatares

  # Exemplo de uso
  if __name__ == "__main__":
      avatar_generator = AvatarGenerator()
      avatar_url = avatar_generator.gerar_avatar("exemplo")
      print(avatar_url)
      avatares = avatar_generator.gerar_avatares_fixos(5)
      print(avatares)
      avatares_aleatorios = avatar_generator.gerar_avatares_aleatorios(5)
      print(avatares_aleatorios)
  ```

## 10.5 Testes de Integração do Modelo de Recomendação

### Diagrama de Sequência

&emsp;&emsp;Um diagrama de sequência é uma representação gráfica utilizada na modelagem de sistemas de software que mostra como os processos interagem entre si e em que ordem, sendo parte da Unified Modeling Language (UML). Este tipo de diagrama detalha a sequência de mensagens e interações entre objetos ou componentes ao longo do tempo, ajudando a visualizar o fluxo de execução de um cenário específico. Além disso, ele esclarece as condições necessárias para a execução das interações e a ordem das chamadas e respostas entre os componentes.

&emsp;&emsp;A importância dos diagramas de sequência reside na clareza que eles trazem para o planejamento e desenvolvimento de sistemas. Eles facilitam a comunicação entre diferentes stakeholders, como desenvolvedores, designers e gerentes de projeto, permitindo uma compreensão comum das funcionalidades do sistema e das interações entre seus componentes. Isso é crucial não apenas para a detecção e correção de erros antes da fase de codificação, mas também para a otimização de processos e para a documentação eficiente das interações sistêmicas, essenciais para a manutenção e atualizações futuras do sistema.

&emsp;&emsp;Para o desenvolvimento e integração do aplicativo CoffeeBreak em parceria com a Fundação Dom Cabral, foi necessário elaborar, por meio de diagramas UML, como está funcionando o modelo de recomendação e APIs utilizadas para complementar a solução. No caso do diagrama delacionado ao Modelo de Recomendação, foi construído com base no fluxo de uso do sistema. Primeiro, o usuário que ingressa no aplicativo pela primeira vez recebe projetos de temas aleatórios, sugeridos como conteúdos de um possível interesse, sendo esse o primeiro modelo de recomendação. O segundo, funciona após as primeiras criações de projetos, o sistem começa a recomendar conteúdos relacionados aos temas dos projetos pessoais.

&emsp;&emsp;Nesse modelo de recomendação foi implementado visando alguns conceitos de programação e UX, que permitem mais interatividade e personalização para os usuários. Por exemplo, com base no modelo de recomendação do aplicativo Instagram, a equipe chegou na conclusão que seria melhor seguindo parecido com esse sistema. Essa estratégia permite que o próprio usuário defina por meio de interesses registrados, quais serão os assuntos mais apresentados para eles, que serão os CEOs parceiros da Fundação Dom Cabral. Os benefícios desses modelos são diversos, como experiência de uso mais aprimorada, economia de tempo e como já dito anteriormente, um sistema personalizado.

<div align="center">
  <sub>Figura 65 - Exemplo de Teste de Integração</sub>
  <img src="./assets/images/diagrama-recomendacao.png" width="100%" alt="Teste de Integração">
  <sup>Fonte: Os autores (2024)</sup>
</div>

&emsp;&emsp;Na imagem acima, é possível compreender como funciona o modelo de recomendação. Quando o usuário acessa a `Home`, com projetos recomendados, o frontend faz uma requisição ao BFF, que então solicita os dados ao serviço de recomendação. Este serviço consulta o modelo, que retorna todos os projetos ordenados dos mais recomendados para os menos. O serviço de recomendação reduz a lista para os 50 principais projetos e, em seguida, verifica no banco de dados todos os projetos que já foram recomendados anteriormente, inserindo aqueles que estão sendo recomendados pela primeira vez. Depois de juntar todas as informações, o serviço envia os dados para o BFF, que por sua vez, retorna ao frontend, que exibe as recomendações ao usuário.

&emsp;&emsp;Para completar, na solução Coffee Break está sendo utilizadas algumas APIs. Uma API (Interface de Programação de Aplicações, do inglês "Application Programming Interface") é um conjunto de definições e protocolos usado no desenvolvimento e na integração de software, permitindo que diferentes sistemas e aplicações se comuniquem entre si. A primeira a ser citada, é a API NEWS, utiliza no sistema para apresentar notícias relacionadas aos assuntos dos projetos. No diagrama de sequência abaixo, o usuário logado acessa a aba de notícias na `Home`, assim o BFF é acionado, envia uma requisição para a API News, que recebe essa requisição, que retorna para o BFF e assim apresenta as notícias na tela para o usuário.

<div align="center">
  <sub>Figura 68 - Exemplo de Teste de Integração</sub>
  <img src="./assets/images/diagrama-news.png" width="100%" alt="Teste de Integração">
  <sup>Fonte: Os autores (2024)</sup>
</div>

&emsp;&emsp;Agora, uma outra API externa utilizada é a API DiceBear. A API DiceBear é uma biblioteca de código aberto que permite gerar avatares personalizados e dinâmicos através de uma API. Com isso, ela é utilizada para aparecer um avatar na foto de perfil de usuário, de forma automática. Caso o usuário queira, ele pode adicionar uma imagem pessoal, mas por meio dessa API, é gerado um avatar aleatório como ícone de usuário. Como visto no diagrama abaixo, o usuário logado acessa a tela de ´Perfil´, em seguida o sistema envia uma requisição para o BFF, que envia para a API que recebe e retorna com uma avatar na imagem de usuário. Após isso, a API retorna para o BFF que retorna na tela de ´Perfil´.

<div align="center">
  <sub>Figura 69 - Exemplo de Teste de Integração</sub>
  <img src="./assets/images/diagrama-dicebear.png" width="100%" alt="Teste de Integração">
  <sup>Fonte: Os autores (2024)</sup>
</div>

&emsp;&emsp;Para finalizar, em relação ao autenticação do sistema, está sendo utilizado a API Google Auth. A API Google Auth é um serviço que permite a autenticação de usuários usando as contas do Google. Esse serviço é parte da Google Identity Platform e é amplamente utilizado para autenticar usuários em aplicações web e móveis. Ele oferece um processo seguro e eficiente de login, aproveitando a infraestrutura de autenticação do Google. Como visto no diagrama de sequência abaixo, o usuário não logado acessa a tela de login, preenche as informações de email e senha, isso é enviado para o BFF, que envia a requisição para a API do Google, que valida os dados do CEO, que retorna para o BFF e aprova o acesso do usuário.

<div align="center">
  <sub>Figura 70 - Exemplo de Teste de Integração</sub>
  <img src="./assets/images/diagrama-google.png" width="100%" alt="Teste de Integração">
  <sup>Fonte: Os autores (2024)</sup>
</div>

# 11. Procedimento de Implantação da Solução
&emsp;&emsp;Esta seção da documentação aborda o processo detalhado para a implantação da solução, incluindo o sistema (frontend e backend) e o banco de dados. Aqui serão detalhados os passos necessários para configurar e executar os componentes de software em um ambiente de desenvolvimento, preparando-os para uso em produção.

## 11.1 Procedimento de Implantação do Sistema
&emsp;&emsp;A implantação do sistema é dividida em duas partes principais: o backend e o frontend. Esta subseção descreve os passos para a configuração e execução do backend.


### 11.1.1 Backend
&emsp;&emsp;Para iniciar a implantação do backend do projeto, que utiliza Python com Flask e segue uma arquitetura SOA (Service-Oriented Architecture), siga estes passos:

1. **Clonar o Repositório:**
   - Clone este repositório do GitHub para sua máquina local:
     ```
     git clone https://github.com/Inteli-College/2024-1B-T09-ES06-G01.git
     ```

2. **Instalação de Dependências:**
   - No diretório raiz do projeto, instale as dependências necessárias listadas no arquivo `requirements.txt`:
     ```
     pip install -r requirements.txt
     ```

3. **Configuração das Variáveis de Ambiente:**
   - Crie um arquivo `.env` na raiz do projeto e preencha-o com as seguintes variáveis necessárias:
     ```
     DB_HOST=coffee-break-database.csqxoej1sykc.us-east-1.rds.amazonaws.com
     DB_USER=admin_coffee
     DB_PASS=coffee1234
     DB_PORT=5432
     DB_URL=postgres://admin_coffee:coffee1234@coffee-break-database.csqxoej1sykc.us-east-1.rds.amazonaws.com:5432/coffee-break-database
     CEO_PORTA=6000
     PROJETO_PORTA=6001
     RECOMENDACAO_PORTA=6002
     NOTICIA_URL_PORTA=6003
     CEO_URL=http://0.0.0.0:6000/api
     PROJETO_URL=http://0.0.0.0:6001/api
     RECOMENDACAO_URL=http://0.0.0.0:6002/api
     NOTICIA_URL=http://0.0.0.0:6003/api
     ```


4. **Execução do Backend:**
   - Navegue até a pasta `src` dentro do diretório clonado.
   - Execute o script `run_backend.py` para iniciar todos os serviços definidos na arquitetura SOA:
     ```
     python3 backend/run_backend.py
     ```
   - Este script inicia os quatro serviços (CEOs, Projetos, Recomendação e BFF Mobile), utilizando múltiplos processos, cada um em sua respectiva porta configurada no arquivo `.env`.

&emsp;&emsp;Esta configuração inicial assegura que todos os serviços necessários para o backend estão em execução e prontos para interação com o frontend ou para testes diretos via API.

### 11.1.2 Frontend

&emsp;&emsp;Com o backend devidamente configurado, comece a configuração do frontend. O desenvolvimento do frontend é feito utilizando Flutter. Siga as instruções detalhadas na [documentação oficial do Flutter](https://docs.flutter.dev/get-started/install) para instalar e configurar o Flutter em seu sistema operacional específico.

Após a instalação do Flutter:

- Navegue até a pasta `/src/frontend/coffeebreak`.
- Execute o comando `flutter run`.

Existem várias opções para visualizar o aplicativo:

- **Web:** Execute o app diretamente em um navegador e ajuste as dimensões da janela para simular uma experiência móvel.
- **Emuladores:** Utilize o Android Studio ou Xcode (para usuários de macOS) para emular um dispositivo Android ou iOS.
- **Dispositivo físico:** Conecte um dispositivo móvel ao computador via cabo USB e ative o modo desenvolvedor. Alternativamente, conecte-se sem fio estando na mesma rede que o computador. Altere todos os IP's `127.0.0.1` no código pelo IP da sua rede, se desejar se conectar de forma remota.

&emsp;&emsp;É crucial que o backend esteja em execução em um terminal separado para que o aplicativo funcione corretamente, assegurando a comunicação entre o frontend e os serviços backend.


## 11.2 Procedimento de Implantação do Banco de Dados
&emsp;&emsp;A replicação exata do banco de dados em uma instância da Amazon RDS é crucial para garantir a consistência e o funcionamento adequado da aplicação em diferentes ambientes. Isso permite que todas as funcionalidades e interações do sistema sejam testadas em um ambiente que simula o ambiente de produção, minimizando riscos de erros e inconsistências que poderiam afetar os usuários finais. Além disso, ao utilizar a RDS, beneficia-se da escalabilidade, segurança e facilidade de manutenção que a infraestrutura da AWS oferece, otimizando o desempenho e a gestão do banco de dados.

### Criação do Banco de Dados na Amazon RDS
&emsp;&emsp;Para configurar um banco de dados PostgreSQL na Amazon RDS, siga estes passos:

1. **Acesse o AWS Management Console** e selecione RDS.
2. **Criar Instância de Banco de Dados**:
   - Escolha "Standard Create" e PostgreSQL.
   - Defina a edição, versão e tipo de instância.
   - Nomeie o banco de dados como `coffee-break-database` e defina as credenciais de acesso.
3. **Configurações de Rede e Segurança**:
   - Selecione a VPC apropriada e configure o grupo de segurança para permitir conexões.
4. **Backup e Manutenção**:
   - Configure as políticas de backup e janelas de manutenção.
5. **Lançar a Instância** e anote o endpoint para conexões.

### Configuração e Execução de Migrations
&emsp;&emsp;Com o banco pronto, configure o esquema:

1. **Clonar o Repositório** e acessar o diretório `src/bi/database`.
2. **Executar Scripts de Migration** sequencialmente:
   - Abra o terminal e navegue até o diretório onde estão os scripts.
   - Execute os scripts de migration com o seguinte comando Python, ajustando o nome do arquivo para cada script:
     ```
     python 001_cria_banco_de_dados_e_tabelas.py
     ```
   - Repita o processo para cada arquivo de script na pasta, ajustando o número do arquivo conforme necessário.

3. **Verificação**:
   - Confira no console da AWS RDS ou diretamente no banco de dados via terminal se as tabelas e estruturas foram criadas corretamente.
   - Utilize o comando a seguir para verificar as tabelas existentes no banco de dados:
     ```
     psql -h [endpoint_do_banco_de_dados] -U [nome_de_usuario] -d coffee-break-database -c "\dt"
     ```

&emsp;&emsp;Este processo assegura que o banco de dados está preparado para suportar a aplicação.

## 11.3 Infográfico

&emsp;&emsp;O infográfico fornecido é uma ferramenta crucial para entender o escopo e o impacto do aplicativo. Ele destaca os principais desafios, soluções e os benefícios que o CoffeeBreak oferece no contexto de responsabilidade social corporativa (RSC). A seguir, são detalhados os componentes-chave apresentados.

1. **Desafios da RSC**:
   - Destaca os principais desafios enfrentados pelas empresas ao iniciar projetos de RSC, como falta de experiência e investimento inicial.

2. **Rede de Apoio**:
   - Explica como a Fundação Dom Cabral identificou que uma rede de apoio entre CEOs poderia facilitar a troca de informações e experiências, como se estivessem em uma pausa para o café.

3. **Conexão**:
   - Descreve como o aplicativo CoffeeBreak facilita a criação de conexões em um ambiente totalmente digital, permitindo aos usuários curtir, salvar e gerenciar projetos, além de interagir com outros perfis.

4. **Sinergias**:
   - Mostra como os usuários podem solicitar sinergia em projetos específicos para trabalhar em colaboração e dobrar o potencial alcançado.

5. **Impactos**:
   - Menciona que os projetos são divididos em seis categorias diferentes como Conservação, Diversidade e Bem-Estar, e como o objetivo é aumentar o impacto positivo que as grandes empresas podem ter no planeta.

### Importância

- **Visão Holística**: Fornece uma visão holística e rápida do projeto CoffeeBreak, enfatizando como ele pode facilitar e otimizar os esforços de RSC.
- **Ferramenta de Engajamento**: Serve como uma ferramenta de engajamento para novos usuários e stakeholders, ajudando-os a compreender rapidamente o valor e o propósito do CoffeeBreak.
- **Promove a Colaboração**: Encoraja a colaboração e o compartilhamento de ideias e recursos entre líderes empresariais, potencializando projetos de impacto social e ambiental.

### Como Acessar

&emsp;&emsp;Para visualizar o infográfico e explorar mais sobre o CoffeeBreak, acesse o link abaixo:

[Visualizar Infográfico](infografico/infografico.md)

&emsp;&emsp;É recomendável que todos os interessados no CoffeeBreak consultem o infográfico para uma compreensão mais completa de como a plataforma pode ser utilizada para promover a responsabilidade social corporativa efetivamente.

## 11.4 Documentação Automática do Sistema

&emsp;&emsp;A documentação automática de sistemas em software é uma prática essencial para manter todos os envolvidos no desenvolvimento e uso de uma aplicação alinhados quanto às funcionalidades e aos métodos de interação com o sistema. Esse tipo de documentação é gerada diretamente a partir do código fonte, utilizando ferramentas que analisam os métodos, parâmetros e comentários no código para criar uma documentação acessível e atualizada. Esta abordagem não apenas economiza tempo e esforço na manutenção manual da documentação, mas também reduz a probabilidade de discrepâncias entre o comportamento real do software e a sua documentação oficial.

&emsp;&emsp;Neste projeto, o Postman foi utilizado para validar os endpoints do backend, pois trata-se de um complemento poderoso à documentação automática. O Postman permite que desenvolvedores e testadores enviem requisições HTTP para os endpoints da API, verificando assim a precisão da documentação e a integridade das funcionalidades descritas. Isso é particularmente importante para garantir que a API se comporte conforme esperado em diferentes cenários, ajudando a identificar e corrigir erros rapidamente. Além disso, a validação através do Postman pode ser automatizada com scripts de testes, o que facilita a integração contínua e a entrega contínua (CI/CD).

<div align="center">
  <sub>Figura 71 - Mockup </sub>
  <img src="./assets/images/postman.png" width="100%" alt="Postman">
  <sup>Fonte: Os autores (2024)</sup>
</div>

&emsp;&emsp;A ["Coffee Break Backend Documentation"](https://documenter.getpostman.com/view/33623818/2sA3JM7MjM) é uma documentação detalhamente preparada no Postman que aborda a execução dos endpoints desta solução em desenvolvimento. Essa documentação é essencial para assegurar que todas as funcionalidades do backend estão operando conforme o esperado. Por meio do uso do Postman, os testes desses endpoints são realizados de forma mais eficiente e organizada, permitindo uma verificação sistemática e detalhada de cada funcionalidade. A ferramenta facilita a execução de chamadas API e a visualização das respostas, o que é essencial para confirmar a integridade e a performance do sistema.

&emsp;&emsp;Dentro da documentação, são destacados os testes de endpoints relacionados aos serviços de CEO, projeto e recomendação. Cada um desses serviços envolve complexas relações entre entidades e atributos, conforme delineado no Modelo Conceitual apresentado na seção 3. Para cada serviço, a documentação detalha os comandos disponíveis, incluindo `POST` para cadastro, `GET` para listar todos os registros, `PUT` para atualização, `DEL` para remoção, e `GET` para busca por ID específico. Essa estrutura organizada não apenas facilita o desenvolvimento e manutenção do sistema, mas também assegura que todas as operações possam ser validadas individualmente, garantindo o sucesso e a confiabilidade do backend.

# Referências

\[referencia_workfellow\] Workfellow AI, "Business Process Analysis Guide – Methods, Benefits, Tools & FAQ". Disponível em: <https://www.workfellow.ai/guides/process-analysis-demystified>. Acesso em: 23 abr. 2024.

\[referencia_integrify\] Integrify, "Importance of Business Process Modeling for Your Organization". Disponível em: <https://www.integrify.com/learning-center/business-process-modeling/>. Acesso em: 23 abr. 2024.

3. Conceito de. **"CASO DE USO"** Disponível em: <https://conceito.de/caso-de-uso>. Acesso em: 25 abr. 2024.

# Apêndice
