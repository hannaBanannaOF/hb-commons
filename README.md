HB Commons
=====

Arquivos comuns

Quick start
-----------

1. Add 'hbcommons' to the INSTALLED_APPS::
```python
    INSTALLED_APPS = [
        ...
        'hbcommons',
    ]
```
2. Configure your settings.py::
```python
    AUTH_USER_MODEL = 'hbcommons.Usuario'
```
3. Run ``python manage.py migrate`` to create the models.

Generating new dist
=====

Para gerar uma nova build::

1. Atualize a versão da dist no arquivo setup.cfg

2. Verifique as migrations

3. Execute o comando ``python setup.py sdist``