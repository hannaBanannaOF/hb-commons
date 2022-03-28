HB Commons
=====

Arquivos comuns para desenvolvimento interno

Quick start - DEVELOPMENT
-----------

1. Crie um ambiente virtual com ``python -m venv env`` e ative ele com ``.\env\Scripts\activate``::

2. Execute ``pip install -r requirements.txt`` para instalar as dependências::

3. Para gerar uma release nova, abra um PR para a main, quando for aprovado e feito merge basta executar um novo deploy nos sistemas dependentes::

Quick start - USAGE
-----------

1. Adicione o repositório git ao arquivo ``requirements.txt``::

2. Execute ``pip install -r requirements.txt`` para instalar as dependências::

3. Adicione o 'hbcommons' aos INSTALLED_APPS::
```python
    INSTALLED_APPS = [
        ...
        'hbcommons',
    ]
```

4. Configure suas settings no arquivo ``settings.py``::
```python
    AUTH_USER_MODEL = 'hbcommons.Usuario'
```

5. Para usar o consumidor, utilize a seguinte configuração::
```python
    SOCIAL_AUTH_HANNABANANNA_KEY = "<your_key>"
    SOCIAL_AUTH_HANNABANANNA_SECRET = "<your_secret>"

    HANNABANNA_AUTH_URL = "<your_hbauth_backend>"
```

6. Execute o comando ``python manage.py migrate`` para aplicar a migration.
