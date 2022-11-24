# Django wheezy.templates

### Описание

У вас проблемы с производительностью шаблонов в Django тогда попробуйте этот шаблонизатор. По моим субьективным замерам скорость в 3 раза выше. Меньше фич -- зато СКОРОСТЬ

### Язык шаблонов
В качестве движка шаблонизатора используется wheezy.template и wheezy.html

#### wheezy.html
 - [Документация по  wheezy.html](https://wheezyhtml.readthedocs.io/en/latest/)
 - [Github wheezy.html](https://github.com/akornatskyy/wheezy.html)
 
 #### wheezy.template
 - [Документация по  wheezy.template](https://wheezytemplate.readthedocs.io/en/latest/) 
 - [Github wheezy.template](https://github.com/akornatskyy/wheezy.template)
 
### Установка
pip install git+https://github.com/saintbyte/django_wheezy_templates

### Настройка

1. Добавляем в INSTALLED_APPS ( settings.py ) 'django_wheezy_templates'

2. В settings.py добавляем
   ```
   TEMPLATES = [
   {
        'BACKEND': 'django_wheezy_templates.backend.wheezy.Wheezy',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {},
    },
    ```
3. В приложения джанго создаем папки wheezy_templates
