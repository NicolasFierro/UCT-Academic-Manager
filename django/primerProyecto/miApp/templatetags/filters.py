from django import template

register = template.Library()

@register.filter(name='saludo')
def saludo (value):
    largo=''
    if len(value)>=10:
        largo= '<p>Tu nombre es muy largo </p>'
    return f'<h1 style="background:green;color:white;">Bienvenido, {value}</h1>'+largo

@register.filter(name='trim')
def trim(value):
    return value.strip()

@register.filter(name='reemplazar')
def reemplazar(value, old, new):
    return value.replace(old, new)

@register.filter(name='titulo')
def titulo(value):
    return value.title()


