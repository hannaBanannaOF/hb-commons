HB Commons
=====

Arquivos comuns

Quick start - DEVELOPMENT
-----------

1. Generate python virtual env with ``python manage.py migrate`` and activate it::

2. Run ``pip install -r requirements.txt`` to install the dependencies::

3. Add 'hbcommons' to the INSTALLED_APPS::
```python
    INSTALLED_APPS = [
        ...
        'hbcommons',
    ]
```
4. Configure your settings.py::
```python
    AUTH_USER_MODEL = 'hbcommons.Usuario'
```
5. Run ``python manage.py migrate`` to create the models.