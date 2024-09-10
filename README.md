# 🚗 Carros App

[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/Lucas-Espindola-dev/carros/blob/main/LICENSE)

## Descrição

Carros App é um projeto que visa gerenciar e listar veículos disponíveis para compra ou aluguel de forma eficiente e organizada. O sistema foi desenvolvido com foco na performance, usabilidade e integração com APIs modernas. A aplicação permite que usuários naveguem por diferentes opções de veículos, visualizem detalhes importantes, filtrem por características específicas e gerenciem transações, proporcionando uma experiência de uso amigável e prática.

## Funcionalidades

- **Cadastro de Veículos**: Permite o registro de novos veículos no sistema com informações detalhadas (marca, modelo, ano, cor, preço). Essa função é crucial para manter o banco de dados atualizado com a disponibilidade de novos automóveis.
  
- **Listagem e Filtro**: Os usuários podem visualizar uma lista completa dos veículos disponíveis, além de aplicar filtros para buscar veículos por marca, modelo, preço e ano. Isso melhora a experiência do usuário, facilitando encontrar o carro ideal rapidamente.
  
- **Gerenciamento de Transações**: Inclui funcionalidades para registrar e acompanhar transações de aluguel ou compra, fornecendo histórico detalhado para administradores e usuários.

- **Autenticação de Usuário**: Implementa sistema de login e gerenciamento de usuários, garantindo segurança e privacidade nas transações.

- **Painel Administrativo**: Fornece ferramentas para administradores gerenciarem os veículos cadastrados, transações e usuários do sistema, além de gerar relatórios de performance.

## Tecnologias Utilizadas

- **Python**: Linguagem principal do backend, escolhida por sua simplicidade, robustez e grande suporte de bibliotecas para integração com APIs e banco de dados.
  
- **Django**: Framework web que acelera o desenvolvimento, oferecendo um ambiente seguro e escalável para a criação de funcionalidades complexas, como o sistema de autenticação e gerenciamento de transações.
  
- **SQLite**: Banco de dados leve, ideal para armazenar informações de veículos e transações de forma local durante o desenvolvimento.
  
- **Bootstrap**: Biblioteca de frontend que garante um design responsivo, proporcionando uma experiência fluida em diferentes dispositivos.

## Importância das Funcionalidades
  
- **Eficiência**: A implementação de filtros e listagens otimizadas melhora a experiência do usuário, reduzindo o tempo necessário para encontrar informações relevantes.
  
- **Segurança**: Com o sistema de autenticação robusto e gerenciamento de usuários, o projeto garante a proteção dos dados dos usuários e das transações realizadas.

## Como Executar o Projeto

1. Clone o repositório:
    ```bash
    git clone https://github.com/Lucas-Espindola-dev/carros.git
    ```

2. Acesse o diretório do projeto:
    ```bash
    cd carros
    ```

3. Crie um ambiente virtual e ative-o:
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

4. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

5. Rode as migrações e inicie o servidor:
    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

## Contribuições

Contribuições são sempre bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests para melhorar o projeto.

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](https://github.com/Lucas-Espindola-dev/carros/blob/main/LICENSE) para mais detalhes.
