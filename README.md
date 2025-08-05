# Sistema de Gestão de Estoque (SGE)

Bem-vindo ao ERP, um projeto desenvolvido em Django e Django REST Framewrok para facilitar o gerenciamento de estoque. Este README fornece informações essenciais sobre como configurar e executar o projeto em seu ambiente local.

## Requisitos

Certifique-se de que você tenha os seguintes requisitos instalados em seu sistema:

- Docker
- Celery e Celery-beat
- Python (versão recomendada: 3.    7 ou superior)
- Django (instalado automaticamente ao seguir as instruções abaixo)
- Outras dependências listadas no arquivo `requirements.txt`


## Instalação das Dependências

Com o ambiente virtual ativado, instale as dependências do projeto usando o comando:
```bash
pip install -r requirements.txt
```

## Rodar o projeto

Git clone:
```bash
https://github.com/Joao-Batista-Dev/ERP---Sistema-de-Gestao/
```

Entre no diretório do projeto
```bash
cd erp
```

Exercute o docker:
```bash
docker-compose up --build
```

Criando um usuário admin:
```bash
docker-compose exec backend python manage.py createsuperuser
```

Após isso, o sistema estará pronto para ser acessado em:
[http://localhost:8000](http://localhost:8000)
