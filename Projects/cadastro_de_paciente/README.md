<h1>Cadastro de paciente</h1>

<h2>Para executar o projeto siga os seguinte passos:</h2>
<ol>
    <li>Criação do banco de dados</li>
    <li>Instalação</li>
    <li>Ambiente de desenvolvimento</li>
</ol>

<h2>Criação do banco de dados</h2>

Para criar o Banco de dados:

Abrir SQL Server Management Studio.

#### No Windows:
> Acessar instância como localhost.

> Clicar com botão direito em cima da pasta 'Databases' e executar comando para criação de novo banco.

Dados para criação do banco:<br>
endereço: db_sql.be3.co<br>
porta: 1515<br>
usuário: teste.be3<br>
senha: ProcSeletivo#2020<br>
base de dados: DB<br>

> Na pasta 'Security' da raiz criar novo loggin

> No banco criado, no caminho 'Security/Users' adicionar novo usuário. 



<h2>Instalação</h2>

Versão do Python 3.9.2

Para criar o ambiente virtual Python digite:

> python -m venv venv

Para **ativar** o <strong>ambiente virtual</strong>, digite:

Observação: O ponto '.' no inicio do comando so deve ser usado em terminais 'bash'.

#### No Windows:
>. venv/Scripts/activate

#### No Linux ou MacOS:
>source venv/bin/activate 

Você vai observar que o ambientenvirtual está ativo pq vai aparecer o nome da maquina virtual assim: (venv) 

Em seguida, instale os requirements:
> pip install -r requirements.txt

Rode as migrations:
> python manage.py migrate



<h2>Ambiente de desenvolvimento</h2>

Para rodar o projeto:
> python manage.py runserver  

Agora vc pode acessar as rotas localmente pelo browser e criar uma reserva por algum aplicativo de serviços de API como o postman por exemplo.

E para acessar o admin, não pare o servidor, em outro terminal, ative a maquina virtual e rode o comando:
>
> (venv) $ python manage.py createsuperuser

```
    Username: <seu usuario>
    Email address: seuemail@email.com
    Password:
    Password (again):
```
Se tudo estiver okay, vai aparecer
```
    Superuser created successfully.
```


