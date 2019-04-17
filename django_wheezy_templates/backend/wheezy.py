__author__ = 'sb'

from django.conf import settings

from wheezy.template.engine import Engine
from wheezy.template.ext.core import CoreExtension
from wheezy.template.loader import FileLoader

from django.template import TemplateDoesNotExist
from django.utils.module_loading import import_string
from django.template.backends.base import BaseEngine
from django.template.backends.utils import csrf_input_lazy, csrf_token_lazy
from django_wheezy_templates.filters.html import escape
from django_wheezy_templates.filters.static import static


class Wheezy(BaseEngine):
    app_dirname = 'wheezy_templates'

    def __init__(self, params):
        params = params.copy()
        options = params.pop('OPTIONS').copy()
        super().__init__(params)

        self.template_context_processors = options.pop('context_processors', [])
        if 'loader' not in options:
            options['loader'] = FileLoader(self.template_dirs)
        options.setdefault('autoescape', True)
        options.setdefault('auto_reload', settings.DEBUG)
        self.engine = Engine(
            loader=options['loader'],
            extensions=[CoreExtension()]
        )

        self.engine.global_vars.update({
            'e': escape,
            'escape': escape,
            'static': static
        })

    def get_template(self, template_name):
        try:
            return Template(self.engine.get_template(template_name), self)
        except OSError as exc:
            raise TemplateDoesNotExist(template_name, backend=self) from exc


class Template:
    def __init__(self, template, backend):
        self.template = template
        self.backend = backend

    def render(self, context=None, request=None):

        if context is None:
            context = {}
        if request is not None:
            context['request'] = request
            context['csrf_input'] = csrf_input_lazy(request)
            context['csrf_token'] = csrf_token_lazy(request)
        return self.template.render(context)
