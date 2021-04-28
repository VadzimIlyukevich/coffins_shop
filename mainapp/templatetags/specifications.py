from django import template

register = template.Library()


@register.filter
def breed_spec(breed):
    print(breed)
    pass
