# Apoio Saúde

## Ideia do Projeto

O projeto "Apoio Saúde" tem como objetivo simplificar a vida de familiares e cuidadores ao oferecer uma solução organizada e acessível para o cuidado de pacientes. Através dessa aplicação, os usuários poderão gerenciar informações relacionadas ao cuidado de seus entes queridos de forma eficiente e intuitiva.

## Instalação

Para começar a trabalhar com o framework Django e iniciar o projeto "Apoio Saúde", siga os passos abaixo:

### Instalação do Django

1. Certifique-se de ter o Python instalado em seu sistema. Você pode baixá-lo e instalá-lo a partir do [site oficial do Python](https://www.python.org/downloads/).

2. Abra um terminal ou prompt de comando e instale o Django utilizando o pip, o gerenciador de pacotes do Python:

    ```
    pip install django
    ```

### Inicialização do Ambiente Virtual (venv)

1. Crie um ambiente virtual para isolar as dependências do seu projeto. No terminal, navegue até o diretório onde deseja criar o ambiente virtual e execute o seguinte comando:

    ```
    python -m venv myenv
    ```

    Substitua `myenv` pelo nome que desejar para o seu ambiente virtual.

2. Ative o ambiente virtual. No Windows, utilize o comando:

    ```
    .\myenv\Scripts\activate
    ```

    No macOS e Linux, utilize o comando:

    ```
    source myenv/bin/activate
    ```

### Inicialização do Projeto Django

1. Inicie o servidor de desenvolvimento. No terminal, dentro do diretório do seu projeto, execute o seguinte comando:

    ```
    python manage.py runserver
    ```

    Isso iniciará o servidor de desenvolvimento do Django. Você poderá acessar seu projeto em `http://localhost:8000/`.

3. Para acessar a interface de administração do Django, crie um superusuário executando o seguinte comando no terminal, dentro do diretório do seu projeto:

    ```
    python manage.py createsuperuser
    ```

    Siga as instruções para criar um superusuário com um nome de usuário, email e senha.

Pronto! Agora você tem um ambiente de desenvolvimento Django configurado e seu projeto "Apoio Saúde" está pronto para ser desenvolvido. A partir daqui, você pode começar a criar suas aplicações e modelos conforme necessário para atender aos requisitos do projeto.
