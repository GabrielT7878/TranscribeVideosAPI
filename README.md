# TranscribeVideosAPI

TranscribeVideosAPI é um projeto desenvolvido em Python utilizando o framework Flask, que permite a transcrição de vídeos de forma eficiente e escalável. Este projeto organiza a API em módulos bem definidos e facilita a manutenção e a expansão do sistema.

## Estrutura do Projeto

TranscribeVideosAPI/
├── .env
├── .git
├── .gitignore
├── README.md
├── api/
├── core/
├── main.py
├── requirements.txt
├── services/
├── tests/
├── tmp/
└── utils/


### Descrição dos Diretórios e Arquivos

- **.env**: Arquivo de configuração para variáveis de ambiente.
- **.git**: Diretório contendo dados do repositório Git.
- **.gitignore**: Arquivo que especifica quais arquivos/diretórios o Git deve ignorar.
- **README.md**: Documentação do projeto.
- **api/**: Contém os endpoints da API.
- **core/**: Contém a lógica principal e configurações do projeto.
- **main.py**: Arquivo principal para iniciar a aplicação Flask.
- **requirements.txt**: Lista de dependências necessárias para rodar o projeto.
- **services/**: Contém serviços auxiliares e lógica de negócio.
- **tests/**: Conjunto de testes para garantir a qualidade do código.
- **tmp/**: Diretório temporário para armazenamento de arquivos intermediários.
- **utils/**: Funções utilitárias e helpers.

## Requisitos

- Python 3.x
- Flask
- Outras dependências listadas no arquivo `requirements.txt`

## Instalação

1. **Clone o repositório:**

   ```sh
   git clone <URL-do-repositório>
   cd TranscribeVideosAPI

2. **Crie e ative um ambiente virtual:**
    ```sh
    python3 -m venv venv
    source venv/bin/activate

