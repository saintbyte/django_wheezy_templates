__author__ = 'sb'
from django.conf import settings


def static(url):
    return "{}{}".format(settings.STATIC_URL, url)
