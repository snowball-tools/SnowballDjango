from django import template

register = template.Library()


@register.inclusion_tag("snowball_window.html")
def snowball_window(windowModel):
    return {"window": windowModel}
