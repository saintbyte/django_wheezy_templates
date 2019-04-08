# Django wheezy.templates

### Описание

У вас проблемы с производительностью шаблонов в Django тогда попробуйте этот шаблонизатор. По моим субьективным замерам скорость в 3 раза выше. Меньше фич -- зато СКОРОСТЬ

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
