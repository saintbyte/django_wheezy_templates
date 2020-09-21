# Django wheezy.templates
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fsaintbyte%2Fdjango_wheezy_templates.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2Fsaintbyte%2Fdjango_wheezy_templates?ref=badge_shield)


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


## License
[![FOSSA Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fsaintbyte%2Fdjango_wheezy_templates.svg?type=large)](https://app.fossa.com/projects/git%2Bgithub.com%2Fsaintbyte%2Fdjango_wheezy_templates?ref=badge_large)