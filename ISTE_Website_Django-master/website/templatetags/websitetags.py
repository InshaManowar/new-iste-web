
from django.template import Library

register=Library()

@register.filter(name='get')
def get(obj,key):
    return obj.get(key,None)