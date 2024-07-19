# Diagrama de Classes de Domínio

&emsp;&emsp;Um Diagrama de Classes é uma representação visual das classes que compõem um sistema e seus relacionamentos. Este tipo de diagrama é fundamental no desenvolvimento de software, pois oferece uma visão clara da estrutura de dados e da organização do sistema, facilitando a comunicação entre os desenvolvedores e o alinhamento com os requisitos do projeto. Além disso, ajuda a identificar as funcionalidades do sistema e como as diferentes partes interagem entre si.

<div align="center">
  <sub>Figura 1 - Diagrama de CLasses de Domínio</sub>
  <img src="../assets/images/diagrama-de-classes-de-dominio.png" width="100%" alt="Diagrama de Classes de Domínio">
  <sup>Fonte: Os autores (2024)</sup>
</div>

&emsp;&emsp;Conforme demonstrado na figura acima, o diagrama de classes do projeto `Coffee Break` foi elaborado com base nas entidades e relacionamentos previstos para o sistema. Dessa forma, as classes identificadas, bem como seus atributos, métodos e relacionamentos, foram representadas no diagrama em questão. A seguir, é apresentada uma descrição detalhada de cada classe identificada no diagrama de classes do projeto `Coffee Break`.

1. ``Usuário``
  - __Atributos__: Identificador único, nome, email, cargo, senha, tipo de usuário (como CEO ou Administrador da FDC), link do LinkedIn, email de contato, nome da empresa, foto da empresa, foto de perfil, celular, link do site da empresa e biografia.
  - __Métodos__:
    - Receber notificações relacionadas à atividade do usuário no sistema.
    - Adicionar um novo projeto à lista de projetos que o usuário gerencia.
    - Remover um projeto específico da lista do usuário.

2. ``Grupo``
  - __Atributos__: Identificador único, nome e descrição do grupo.
  - __Métodos__:
    - Incluir um usuário no grupo.
    - Remover um usuário do grupo.

3. ``Projeto``
  - __Atributos__: Identificador único, nome, descrição detalhada, data de criação e identificador do usuário que é o CEO do projeto.
  - __Métodos__:
    - Atualizar as informações do projeto com novos dados.
    - Adicionar um interesse de um usuário no projeto.
    - Remover o interesse de um usuário no projeto.
    - Registrar que um usuário curtiu o projeto.
    - Registrar que um usuário retirou a curtida do projeto.
    - Marcar um projeto como favorito para fácil acesso posterior do usuário.
    - Remover um projeto da lista de favoritos do usuário.

4. ``Subtema``
  - __Atributos__: Identificador único, nome e descrição do subtema.
  - __Métodos__:
    - Associar um projeto a este subtema.
    - Desassociar um projeto deste subtema.

5. ``Macrotema``
  - __Atributos__: Identificador único, nome e descrição do macrotema.
  - __Métodos__:
    - Adicionar um subtema ao macrotema.
    - Remover um subtema do macrotema.

6. ``Interação (Classe Base)``
  - __Atributos__: Identificador único, identificador do usuário que realizou a interação, identificador do projeto alvo e data da interação.
  - __Métodos__:
    - Registrar uma interação geral no sistema.
    - Remover uma interação geral do sistema.

7. ``Favorito (Derivado de Interação)``
  - __Métodos__:
    - Registrar um projeto como favorito por um usuário.
    - Remover um projeto da lista de favoritos de um usuário.

8. ``Like (Derivado de Interação)``
  - __Métodos__:
    - Registrar que um usuário curtiu um projeto.
    - Remover a curtida de um usuário em um projeto.

9. ``Interesse (Derivado de Interação)``
  - __Métodos__:
    - Registrar o interesse de um usuário em um projeto.
    - Remover o interesse de um usuário em um projeto.

10. ``Notificação``
  - __Atributos__: Identificador único, identificador do usuário que deve receber a notificação, conteúdo da mensagem, data da notificação e status para indicar se foi lida.
  - __Métodos__:
    - Enviar uma notificação a um usuário.
    - Marcar a notificação como lida pelo usuário.

&emsp;&emsp;Essas classes representam a estrutura do sistema de gerenciamento do projeto Coffee Break, refletindo como os usuários interagem com os projetos e uns com os outros através de ações como curtidas, favoritos e expressão de interesse. As notificações servem para manter os usuários informados sobre atualizações e mudanças importantes.
